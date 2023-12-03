file = open('input.txt', 'r')
Lines = file.readlines()

total = 0
for line in Lines:
    line = line.strip()
    red = 0
    green = 0
    blue = 0
    gameLine = line.split(": ")
    gameId = int(gameLine[0].split(" ")[1])
    turns = gameLine[1].split("; ")
    for t in turns:
        cubes = t.split(", ")
        for c in cubes:
            cube = c.split(" ")
            num = int(cube[0])
            color = cube[1]
            if color == "red":
                red = max(red, num)
            if color == "green":
                green = max(green, num)
            if color == "blue":
                blue = max(blue, num)
    power = red * green * blue
    total += power

print(total)

