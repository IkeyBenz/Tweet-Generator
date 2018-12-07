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
    charactersToRemove = ['\n', ',', ':']
    for c in charactersToRemove:
        text = ' '.join(text.split(c))
    withoutSpaces = list(filter(lambda w: w != '', text.split(' ')))
    lowerCase = list(map(lambda w: w.lower(), withoutSpaces))
    return lowerCase


generator = MarkovChain(getAllWords())
for _ in range(10):
    print(generator.makeSentence(12) + '.')


'''
RegEx:
it's all about patterns
regular expressions work with strings
strings are just sequences of characters (bytes)

You can ask
1) if the pattern is there
2) how mant times
3) where does the pattern start
4) where does it occur
5) what is before it and what is after it


'''
