from dictogram import Dictogram
import random
# [one, fish, ....]


class MarkovChain(dict):
    def __init__(self, sentences, order=1):
        super(MarkovChain, self).__init__()
        self.sentenceStarters = Dictogram()
        for s in sentences:
            self.compile2(s)

    # First Order
    def compile(self, sentence):
        words = sentence.split(' ')
        for i in range(len(words)-1):
            if words[i] not in self:
                self[words[i]] = Dictogram()
            self[words[i]].add_count(words[i+1])

    # Second Order
    def compile2(self, sentence):
        # Split sentence by spaces, remove empty strings, add '###' to the end of wordsLst
        words = list(filter(lambda w: w != '', sentence.split(' '))) + ['###']

        # Ensures this sentence can be evaluated in second order
        if len(words) > 2:
            # Add tuple of first two words to our sentence starters dictogram
            self.sentenceStarters.add_count((words[0], words[1]))

            # Loop through indices of wordsLst and create 2nd order markov chain
            for i in range(len(words)-2):
                newKey = (words[i], words[i+1])
                if newKey not in self:
                    self[newKey] = Dictogram()
                self[newKey].add_count(words[i+2])

    # Nth Order
    def compileN(self, sentence, n):
        words = list(filter(lambda w: w != '', sentence.split(' ')))
        if len(words) > n:
            for i in range(len(words)-n):
                newKey = tuple(w for w in words[i:i+n])
                if len([i for i in newKey if i[-1] not in '!?.']) == n:
                    if newKey not in self:
                        self[newKey] = Dictogram()
                    self[newKey].add_count(words[i+n])

    def probableWordFrom(self, dictogram):
        '''Picks a random word from histogram containing words and weights'''
        words, weights = zip(*dictogram.items())

        # Creates a list of integers, which act as separators between weights
        accumulator, separators = 0, []
        for weight in weights:
            accumulator += weight
            separators.append(accumulator)

        # The indices of the words lst and seperators lst are concurrent
        # Here we return the word at index of whichever weight in the separators lst
        # is greater than this random number
        rand = random.randint(0, accumulator)
        for index, separator in enumerate(separators):
            if rand <= separator:
                return words[index]

    def makeSentence(self):
        words = list(self.probableWordFrom(self.sentenceStarters))
        newWord = self.probableWordFrom(self[(words[-2], words[-1])])
        while newWord != '###':
            words.append(newWord)
            newWord = self.probableWordFrom(self[(words[-2], words[-1])])
        return ' '.join(words)


# spongebob could use the food anyways you my pet snail say that.
