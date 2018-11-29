const http = require('http');
const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

function getSpongeobQuotes(link) {
    return getHtml(link).then(html => {
        const $ = cheerio.load(html);
        const transcript = $('#mw-content-text ul').text();
        const quotes = transcript.split('\n').filter(line => {
            return line.startsWith('SpongeBob:') || line.startsWith('SpongeBob SquarePants:');
        }).map(quote => {
            const q = quote.replace('SpongeBob: ', '').replace('SpongeBob SquarePants: ', '');
            return removeBrackets(q).trim().split(/(\.|\?|\!)/g).join('\n');
        });
        return quotes;
    });
}

function getHtml(link) {
    return new Promise(function(resolve, reject) {
        http.get(link, (response) => {
            let data;
            response.on('data', (d) => data += d);
            response.on('close', () => resolve(data));
        });
    });
}
function removeBrackets(s) {
    return s.indexOf('[') != -1
        ? removeBrackets(s.slice(0, s.indexOf('[')) + s.slice(s.indexOf(']') + 1))
        : s;
}
function getTranscriptLinks() {
    return getHtml('http://spongebob.wikia.com/wiki/List_of_transcripts')
        .then(html => {
            const $ = cheerio.load(html);
            let anchorTags = []
            for (let i = 0; i < $('.tabbertab .wikitable').length; i++) {
                for (let j = 1; j < $(`.wikitable:nth-child(${i}) tr`).length; j++) {
                    anchorTags.push($(`.wikitable:nth-child(${i}) tr:nth-child(${j}) td:nth-child(3) a`).attr('href'));
                }
            }
            return anchorTags
                .filter(route => route != null)
                .map(route => { return 'http://spongebob.wikia.com' + route });
        });
}
function storeQuotesFromLink(link, episodeName) {
    return new Promise(async (resolve, reject) => {
        const folder = path.join(__dirname, 'Transcripts');
        const quotes = await getSpongeobQuotes(link);
        const text = quotes.join('\n');
        fs.writeFile(path.join(folder, episodeName + '.txt'), text, resolve);
    });
}
const nameFromLink = (link) => {
    let route = link.slice(link.indexOf('/wiki/') + 6);
    return route.slice(0, route.indexOf('/'));
}
async function main() {
    const transcriptLinks = await getTranscriptLinks();
    console.log(nameFromLink(transcriptLinks[0]));
    storeQuotesFromLink(transcriptLinks[0], nameFromLink(transcriptLinks[0]));
}

main();