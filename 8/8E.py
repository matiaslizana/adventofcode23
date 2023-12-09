if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    networkMap = {}
    steps = list(Lines[0].replace('\n',''))
    currentSteps = []
    for line in Lines[2:]:
        instruction = line.split(" = ")
        movements = instruction[1].replace('(', '').replace(')', '').replace('\n', '').split(", ")
        if instruction[0].endswith("A"):
            currentSteps.append(instruction[0])
        networkMap[instruction[0]] = {"L": movements[0], "R": movements[1]}

    mapStep = 0
    while not all(step.endswith('Z') for step in currentSteps):
        for c in range(len(currentSteps)):
            currentSteps[c] = networkMap[currentSteps[c]][steps[mapStep % len(steps)]]
            print(currentSteps[c], end=' ')
        mapStep += 1
        print()
    print(mapStep)
