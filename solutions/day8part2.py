from math import lcm

with open("Advent-of-Code-2023/solutions/files/day8input.txt", "r") as file:
    fileLines = file.readlines()
    mainDict = {}
    
    startKeys = []
    endKeys = []

    rightLeft = fileLines[0]

    for i in range(2, len(fileLines)):
        key = fileLines[i][0:3]
        if key[2] == "A": startKeys.append(key)
        if key[2] == "Z": endKeys.append(key)

        leftValue = fileLines[i][7:10]
        rightValue = fileLines[i][12:15]

        mainDict[key] = [leftValue, rightValue]
    
    stepsArray = []

    for i in range(len(startKeys)):
        ZZZreached = False
        counter = 0
        steps = 0

        rightLeftNum = 0
        currentKey = startKeys[i]

        while not ZZZreached:
            if rightLeft[counter] == "L":
                rightLeftNum = 0
            else:
                rightLeftNum = 1
        
            counter += 1
            if counter == len(rightLeft) - 1: counter = 0

            currentKey = mainDict[currentKey][rightLeftNum]
            steps += 1
            if currentKey[2] == "Z": ZZZreached = True
        
        stepsArray.append(steps)
    
    print(stepsArray)
    
    print(lcm(stepsArray[0], stepsArray[1], stepsArray[2], stepsArray[3], stepsArray[4], stepsArray[5]))