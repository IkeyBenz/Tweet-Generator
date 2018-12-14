import random

def getWordsFrom(filePath="/usr/share/dict/words"):
    ''' Takes a file with words separated by \n and returns them in a list '''
    return open(filePath, 'r').read().split('\n')

def pickRandomWords(amount, words):
    ''' Returns a list of (amount) randomly chosen words from the words list '''
    return [random.choice(words) for _ in range(amount)]

def makeSentenceWith(words):
    ''' Joins the words list by spaces and returns it '''
    return ' '.join(words) + '.'
    
def main():
    words = getWordsFrom()
    selectedWords = pickRandomWords(8, words)
    return makeSentenceWith(selectedWords)

if __name__ == '__main__':
    print(main())
