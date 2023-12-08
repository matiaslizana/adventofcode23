import sys


def checkRange(seed, rangeMap):
    currentMapping = seed
    for m in rangeMap:
        for r in rangeMap[m]:
            if r["source"] < currentMapping < r["source"] + r["range"]:
                currentMapping = r["target"] + currentMapping - r["source"]
                break
    return currentMapping


def readRange(lineId, rangeMap, mapIndex):
    rangeMap[mapIndex] = []
    line = Lines[lineId].strip()
    while line != "" and lineId < len(Lines):
        line = Lines[lineId].strip()
        if line == "":
            return lineId
        rangeElement = line.split(" ")
        rangeMap[mapIndex].append({"source": int(rangeElement[1]), "target": int(rangeElement[0]), "range": int(rangeElement[2])})
        lineId += 1
    return lineId


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    seedsRanges = Lines[0].split(": ")[1].split(" ")

    lineId = 3
    rangeMap = {}

    print("Read Ranges")
    lineId = readRange(lineId, rangeMap, 0) + 2
    lineId = readRange(lineId, rangeMap, 1) + 2
    lineId = readRange(lineId, rangeMap, 2) + 2
    lineId = readRange(lineId, rangeMap, 3) + 2
    lineId = readRange(lineId, rangeMap, 4) + 2
    lineId = readRange(lineId, rangeMap, 5) + 2
    lineId = readRange(lineId, rangeMap, 6) + 2

    seeds = []
    seedIndex = 0
    minLocation = sys.maxsize

    while seedIndex < len(seedsRanges):
        initial = int(seedsRanges[seedIndex])
        length = int(seedsRanges[seedIndex + 1])
        s = initial
        while s < initial + length:
            print(str(seedIndex/2+1) + "/" + str(len(seedsRanges)/2) + " - (" + str(round((s - initial) / length * 100,2)) + "%) Mapping seed " + str(s))
            minLocation = min(minLocation, checkRange(int(s), rangeMap))
            s += 1
        seedIndex += 2

    print(minLocation)