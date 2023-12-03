if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    total = 0
    numbers = [
               "zero",
               "one",
               "two",
               "three",
               "four",
               "five",
               "six",
               "seven",
               "eight",
               "nine"
              ]
    for line in Lines:
        first = 0
        last = 0

        index = 0
        foundIndex = len(line)
        foundNum = 0
        for n in numbers:
            newIndex = line.find(n)
            if foundIndex > newIndex > -1:
                foundIndex = newIndex
                foundNum = index
            index+= 1
        line = line.replace(numbers[foundNum], str(foundNum), 1)

        index = 0
        foundIndex = 0
        foundNum = 0
        for n in numbers:
            newIndex = line.rfind(n)
            if newIndex > foundIndex and newIndex != -1:
                foundIndex = newIndex
                foundNum = index
            index+= 1
        line = line.replace(numbers[foundNum], str(foundNum), 1)

        for c in line:
            if c.isnumeric():
                first = c
                break
        for c in reversed(line):
            if c.isnumeric():
                last = c
                break
        number = int(first) * 10 + int(last)
        total += int(number)
    print(total)