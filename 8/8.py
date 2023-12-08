if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    networkMap = {}
    steps = list(Lines[0].replace('\n',''))
    for line in Lines[2:]:
        instruction = line.split(" = ")
        movements = instruction[1].replace('(', '').replace(')', '').replace('\n', '').split(", ")
        networkMap[instruction[0]] = {"L": movements[0], "R": movements[1]}

    currentStep = "AAA"
    mapStep = 0

    while currentStep != "ZZZ":
        currentStep = networkMap[currentStep][steps[mapStep % len(steps)]]
        mapStep += 1
    print(mapStep)
