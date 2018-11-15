from markovChain import MarkovChain
from os import listdir, path

def getAllWords():
    transcriptsDir = '/Users/IkeyBenz/Code/MakeSchool/CS-1.2/ClassTweetGenerator/WebScrapper/Transcripts'
    words = []
    for transcript in listdir(transcriptsDir):
        words.extend(getWordsFrom(path.join(transcriptsDir, transcript)))
    return words
        
def getWordsFrom(filePath):
    text = open(filePath, 'r').read()
    charactersToRemove = ['\n', '.', ',', '!', '?', ':']
    for c in charactersToRemove:
        text = ' '.join(text.split(c))
    withoutSpaces = list(filter(lambda w: w != '', text.split(' ')))
    lowerCase = list(map(lambda w: w.lower(), withoutSpaces))
    return lowerCase

generator = MarkovChain(getAllWords())
for _ in range(10):
    print(generator.makeSentence(12) + '.')