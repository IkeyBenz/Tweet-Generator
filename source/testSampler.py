import sampleBasedOnFrequency as wordFrequency

# Tests whether the trueData is close to the data recieved from my
# chooseWordFromHistogram function
def test():
    words = []
    for _ in range(10000):
        words.append(wordFrequency.test())
    trueData = wordFrequency.histogram(open('oneFish.txt', 'r').read())
    data = normalize(wordFrequency.histogram(words), trueData, 10000)
    print('DATA:\n', data)
    print('TRUE:\n', trueData)

# Does some math to mofity the data to make it comparable to trueData
def normalize(data, trueData, total):
    trueCount = sum([trueData[i] for i in trueData.keys()])
    newData = {}
    for key, value in data.items():
        newData[key] = value * trueCount / total
    return newData


if __name__ == '__main__':
    print('Running Test...')
    test()