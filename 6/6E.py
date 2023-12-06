import re

if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    time = int(''.join(re.findall(r'\d+', Lines[0].split(":")[1])))
    distance = int(''.join(re.findall(r'\d+', Lines[1].split(":")[1])))

    errorMargin = 1
    holdTime = 1
    waysToWin = 0
    while holdTime < time - 1:
        print("Time: " + str(holdTime) + " (" + str(round(holdTime / time, 2)) + ")")
        raceTime = time - holdTime
        raceDistance = holdTime * raceTime
        if raceDistance > distance:
            waysToWin += 1
        holdTime += 1
    errorMargin *= waysToWin

    print(errorMargin)
