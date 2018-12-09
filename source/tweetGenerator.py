from markovChain import MarkovChain
from os import listdir, path


def getAllSentences():
    transcriptsDir = '/Users/IkeyBenz/Code/MakeSchool/CS-1.2/ClassTweetGenerator/WebScrapper/Transcripts'
    sentences = []
    for transcript in listdir(transcriptsDir):
        sentences.extend(getSentencesFrom(
            path.join(transcriptsDir, transcript)))
    return sentences


def isEndOfSentence(word):
    if word == 'mr.' or word == 'mrs.' or word == '':
        return False
    if word[-1] in '?!.':
        return True
    return False


def getSentencesFrom(filePath):
    lines = [l.lower() for l in open(filePath, 'r').read().split('\n')]
    sentences = []
    currSentence = []
    for line in lines:
        for word in line.split(' '):
            currSentence.append(word)
            if isEndOfSentence(word):
                sentences.append(' '.join(currSentence))
                currSentence = []
    return sentences


generator = MarkovChain(getAllSentences())
for _ in range(10):
    print(generator.makeSentence())


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
