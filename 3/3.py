def findSymbolPosition(m, r, c):
    if 0 <= r < len(m) and 0 <= c < len(m[0]):
        return m[r][c] != '.' and not m[r][c].isnumeric()
    return False


def findSymbolAllDirections(m, r, c):
    return findSymbolPosition(m, r - 1, c - 1) or findSymbolPosition(m, r - 1, c) or findSymbolPosition(m, r - 1, c + 1) or findSymbolPosition(m, r, c + 1) or findSymbolPosition(m, r, c - 1) or findSymbolPosition(m, r + 1, c - 1) or findSymbolPosition(m, r + 1, c) or findSymbolPosition(m, r + 1, c + 1)


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    columns = len(Lines[0]) - 1
    rows = len(Lines)
    m = [[0 for x in range(rows)] for y in range(columns)]

    for i, line in enumerate(Lines):
        line = line.strip()
        for j, c in enumerate(line):
            m[i][j] = c

    total = 0
    r = 0
    c = 0
    while r < rows:
        while c < columns:
            s = m[r][c]
            if s.isnumeric():
                number = ""
                found = False
                index = 0
                while c + index < columns and m[r][c + index].isnumeric():
                    found |= findSymbolAllDirections(m, r, c + index)
                    number += m[r][c + index]
                    index += 1
                if found:
                    total += int(number)
                c += index
            c += 1
        c = 0
        r += 1
    print(total)


