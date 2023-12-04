file = open('input.txt', 'r')
Lines = file.readlines()
total = 0

for line in Lines:
    numbers = line.split(": ")
    numbersSplit = numbers[1].split("| ")
    winners = numbersSplit[0].replace("  ", " ").strip().split(" ")
    have = numbersSplit[1].replace("  ", " ").strip().split(" ")
    matches = 0
    price = 0
    for w in winners:
        for h in have:
            if w == h:
                matches += 1
    if matches > 0:
        matches -= 1
        price = pow(2, matches)
    total += price
print(total)