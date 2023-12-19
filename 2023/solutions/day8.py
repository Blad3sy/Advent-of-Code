with open("Advent-of-Code-2023/solutions/files/day8input.txt", "r") as file:
    fileLines = file.readlines()
    mainDict = {}

    rightLeft = fileLines[0]

    for i in range(2, len(fileLines)):
        key = fileLines[i][0:3]
        leftValue = fileLines[i][7:10]
        rightValue = fileLines[i][12:15]

        mainDict[key] = [leftValue, rightValue]

    ZZZreached = False
    counter = 0
    steps = 0

    rightLeftNum = 0
    currentKey = "AAA"

    while not ZZZreached:
        if rightLeft[counter] == "L":
            rightLeftNum = 0
        else:
            rightLeftNum = 1
        
        counter += 1
        if counter == len(rightLeft) - 1: counter = 0

        currentKey = mainDict[currentKey][rightLeftNum]
        steps += 1
        if currentKey == "ZZZ": ZZZreached = True
    
    print(steps)