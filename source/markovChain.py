from dictogram import Dictogram
from random import randint

class MarkovChain(dict):
    def __init__(self, wordsLst):
        super(MarkovChain, self).__init__()
        self.wordFrequencies = Dictogram(wordsLst)
        self._comile(wordsLst)

    def _comile(self, words):
        for i in range(len(words)-1):
            if words[i] not in self:
                self[words[i]] = Dictogram()
            self[words[i]].add_count(words[i+1])

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


