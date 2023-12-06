import re

if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    time = re.findall(r'\d+', Lines[0].split(":")[1])
    time = [int(t) for t in time]
    distance = re.findall(r'\d+', Lines[1].split(":")[1])
    distance = [int(d) for d in distance]

    errorMargin = 1
    for race in range(len(time)):
        holdTime = 1
        waysToWin = 0
        while holdTime < time[race] - 1:
            raceTime = time[race] - holdTime
            raceDistance = holdTime * raceTime
            if raceDistance > distance[race]:
                waysToWin += 1
            holdTime += 1
        errorMargin *= waysToWin

    print(errorMargin)