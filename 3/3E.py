def findSymbolPosition(m, r, c):
    if 0 <= r < len(m) and 0 <= c < len(m[0]):
        return m[r][c] != '.' and m[r][c] == '*'
    return False


def findSymbolAllDirections(m, r, c):
    if findSymbolPosition(m, r - 1, c - 1):
        return True, r - 1, c - 1
    if findSymbolPosition(m, r - 1, c):
        return True, r - 1, c
    if findSymbolPosition(m, r - 1, c + 1):
        return True, r - 1, c + 1
    if findSymbolPosition(m, r, c + 1):
        return True, r, c + 1
    if findSymbolPosition(m, r, c - 1):
        return True, r, c - 1
    if findSymbolPosition(m, r + 1, c - 1):
        return True, r + 1, c - 1
    if findSymbolPosition(m, r + 1, c):
        return True, r + 1, c
    if findSymbolPosition(m, r + 1, c + 1):
        return True, r + 1, c + 1
    return False, -1, -1


def setCoordinates(x, y, number):
    if number != "":
        if (x, y) not in coordinates:
            coordinates[(x, y)] = []
        coordinates[(x, y)].append(int(number))
    return


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    columns = len(Lines[0]) - 1
    rows = len(Lines)
    m = [[0 for x in range(rows)] for y in range(columns)]
    coordinates = {(0, 0): []}

    for i, line in enumerate(Lines):
        line = line.strip()
        for j, c in enumerate(line):
            m[i][j] = c

    r = 0
    c = 0
    while r < rows:
        while c < columns:
            s = m[r][c]
            if s.isnumeric():
                number = ""
                found = False
                index = 0
                sx = 0
                sy = 0
                while c + index < columns and m[r][c + index].isnumeric():
                    sf, nsx, nsy = findSymbolAllDirections(m, r, c + index)
                    if sf:
                        sx = nsx
                        sy = nsy
                    found |= sf
                    number += m[r][c + index]
                    index += 1
                if found:
                    setCoordinates(sx, sy, number)
                c += index
            c += 1
        c = 0
        r += 1

    total = 0
    for key, value in coordinates.items():
        gear = 0
        if len(value) == 2:
            gear = value[0] * value[1]
        total += gear
    print(total)