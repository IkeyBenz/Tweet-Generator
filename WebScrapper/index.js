const http = require('http');
const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

// Returns html content from webpage link
function getHtml(link) {
    return new Promise(function (resolve, reject) {
        http.get(link, (response) => {
            let data;
            response.on('data', (d) => data += d);
            response.on('close', () => resolve(data));
        });
    });
}

// Returns list of quotes by spongebob from webpage link
function getSpongeobQuotes(link) {
    return getHtml(link).then(html => {
        const $ = cheerio.load(html);
        const transcript = $('#mw-content-text ul').text();
        return transcript.split('\n').filter(line => {
            return line.startsWith('SpongeBob:') || line.startsWith('SpongeBob SquarePants:');
        }).map(quote => {
            const q = quote.replace('SpongeBob: ', '').replace('SpongeBob SquarePants: ', '');
            return removeBrackets(q).trim();
        });
    }).catch(console.error);
}
const brackets = /\s?\[.*?\]/g;
function removeBrackets(s) {
    return s.replace(brackets, '');
}
// Returns list of links that point to spongebob episode transcripts
function getTranscriptLinks() {
    return getHtml('http://spongebob.wikia.com/wiki/List_of_transcripts')
        .then(html => {
            const $ = cheerio.load(html);
            let routes = [];
            $('.tabbertab .wikitable a').each(function () {
                const route = $(this).attr('href');
                if (route.indexOf('transcript') > -1) {
                    routes.push('http://spongebob.wikia.com' + route);
                }
            });
            return routes;
        }).catch(console.error);
}
// Writes spongebob quotes (from given link) to a file in the
// transcripts folder, titled { episodeName }.txt
function storeQuotesFromLink(link, episodeName) {
    return new Promise(async (resolve, reject) => {
        const quotes = await getSpongeobQuotes(link)
        const filePath = path.join(__dirname, 'Transcripts', episodeName + '.txt');
        const text = quotes.join('\n');
        await fs.writeFileSync(filePath, text)
        resolve();
    });
}

const nameFrom = (link) => {
    let route = link.slice(link.indexOf('/wiki/') + 6);
    return route.slice(0, route.indexOf('/'));
}

async function main() {
    const transcriptLinks = await getTranscriptLinks();
    for (let i = 0; i <= transcriptLinks.length; i++) {
        const link = transcriptLinks[i];
        const name = nameFrom(link);
        await storeQuotesFromLink(link, name);
        console.log(`Stored episode ${i + 1}/${transcriptLinks.length} (${name})`);
    }
}

main();