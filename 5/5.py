def checkRange(seed):
    location = 0
    return location


def readRange(lineId, rangeMap, mapIndex):
    rangeMap[mapIndex] = []
    line = Lines[lineId].strip()
    while line != "":
        if line == "":
            return
        rangeElement = line.split(" ")
        rangeMap[mapIndex].append({"source": rangeElement[1], "target": rangeElement[0], "range": rangeElement[2]})
        lineId += 1
        line = Lines[lineId].strip()
    return lineId


if __name__ == '__main__':
    file = open('example.txt', 'r')
    Lines = file.readlines()
    seeds = Lines[0].split(": ")[1].split(" ")
    lineId = 3
    map = []

    lineId = readRange(lineId, map, 0) + 2
    lineId = readRange(lineId, map, 1) + 2
    lineId = readRange(lineId, map, 2) + 2
    lineId = readRange(lineId, map, 3) + 2
    lineId = readRange(lineId, map, 4) + 2
    lineId = readRange(lineId, map, 5) + 2
    lineId = readRange(lineId, map, 6) + 2

    minLocation = int('inf')
    for s in seeds:
        minLocation = min(minLocation, checkRange(s))

    print(minLocation)