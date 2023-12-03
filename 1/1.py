file = open('input.txt', 'r')
Lines = file.readlines()
total = 0
for line in Lines:
    first = 0
    last = 0
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