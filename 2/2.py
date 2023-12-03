file = open('input.txt', 'r')
Lines = file.readlines()

totalIds = 0
for line in Lines:
    line = line.strip()
    red = 12
    green = 13
    blue = 14
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
    if red <= 12 and green <= 13 and blue <= 14:
        totalIds += gameId
print(totalIds)

