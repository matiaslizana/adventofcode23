def calculateHistory(history):
    historyNext = []
    for h in range(len(history) - 1):
        historyNext.append(history[h + 1] - history[h])
    if all(h == 0 for h in historyNext):
        historyNext.append(0)
    else:
        nextValue = historyNext[-1] + calculateHistory(historyNext)
        historyNext.append(nextValue)
    return historyNext[-1]


if __name__ == '__main__':
    file = open('example.txt', 'r')
    Lines = file.readlines()
    total = 0
    for line in Lines:
        history = line.replace('\n','').split(" ")
        history = [int(h) for h in history]
        predicted = history[-1] + calculateHistory(history)
        total = total + predicted
    print(total)