def calculateHistory(history):
    historyNext = [history[h + 1] - history[h] for h in range(len(history) - 1)]
    historyNext.insert(0, 0 if all(h == 0 for h in historyNext) else historyNext[0] - calculateHistory(historyNext))
    return historyNext[0]


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    total = 0
    for line in Lines:
        history = [int(h) for h in line.replace('\n', '').split(" ")]
        total += history[0] - calculateHistory(history)
    print(total)
