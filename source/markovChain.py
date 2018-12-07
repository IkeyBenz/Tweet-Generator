from dictogram import Dictogram
from random import randint
# [one, fish, ....]


class MarkovChain(dict):
    def __init__(self, wordsLst):
        super(MarkovChain, self).__init__()
        self.wordFrequencies = Dictogram(wordsLst)
        self.compile(wordsLst)

    # First Order
    def compile(self, words):
        for i in range(len(words)-1):
            if words[i] not in self:
                self[words[i]] = Dictogram()
            self[words[i]].add_count(words[i+1])

    # Second Order
    def compile2(self, words):
        for i in range(len(words)-2):
            newKey = (words[i], words[i+1])
            if newKey not in self:
                self[newKey] = Dictogram()
            self[newKey].add_count(words[i+2])

    # Nth Order
    def compileN(self, words, n):
        for i in range(len(words)-n):
            newKey = tuple(w for w in words[i:i+n])
            if newKey not in self:
                self[newKey] = Dictogram()
            self[newKey].add_count(words[i+n])

    def getNextWord(self, dictogram):
        words, frequencies = zip(*dictogram.items())
        accumulator, separators = 0, []
        for frequency in frequencies:
            accumulator += frequency
            separators.append(accumulator)
        rand = randint(0, accumulator)
        for index, separator in enumerate(separators):
            if rand <= separator:
                return words[index]

    def makeSentence(self, length=8):
        words = [self.getNextWord(self.wordFrequencies)]
        for _ in range(length-1):
            words.append(self.getNextWord(self[words[-1]]))
        return ' '.join(words)


# spongebob could use the food anyways you my pet snail say that.
