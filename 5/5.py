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
    seeds = Lines[0].split(": ")[1].split(" ")
    lineId = 3
    rangeMap = {}

    lineId = readRange(lineId, rangeMap, 0) + 2
    lineId = readRange(lineId, rangeMap, 1) + 2
    lineId = readRange(lineId, rangeMap, 2) + 2
    lineId = readRange(lineId, rangeMap, 3) + 2
    lineId = readRange(lineId, rangeMap, 4) + 2
    lineId = readRange(lineId, rangeMap, 5) + 2
    lineId = readRange(lineId, rangeMap, 6) + 2

    minLocation = sys.maxsize
    for s in seeds:
        minLocation = min(minLocation, checkRange(int(s), rangeMap))

    print(minLocation)