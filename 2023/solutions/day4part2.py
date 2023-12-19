with open("Advent-of-Code-2023/solutions/files/day4input.txt", "r") as file:
    fileLines = file.readlines()
    total = len(fileLines)
    copyList = []
    for i in range(0, total):
        copyList.append(1)
    counter = 1

    while counter < total + 1:
        currentLine = fileLines[counter - 1]

        id = 0
        bufferNum = ""
        for i in range(len(currentLine)):
            if currentLine[i] == ":":
                currentLine = currentLine[i + 1:]
                id = int(bufferNum)
                break
            elif currentLine[i].isdigit():
                bufferNum += currentLine[i]
        
        currentLine = currentLine.strip()

        winningNumbers = []
        bufferNum = ""

        for i in range(len(currentLine)):
            if currentLine[i] == "|":
                currentLine = currentLine[i + 1:]
                break
            elif currentLine[i] == " ":
                if bufferNum != "": winningNumbers.append(int(bufferNum))
                bufferNum = ""
            else:
                bufferNum += currentLine[i]

        yourNumbers = []
        bufferNum = ""

        currentLine = currentLine.strip()

        for i in range(len(currentLine)):
            if currentLine[i] == " ":
                if bufferNum != "": yourNumbers.append(int(bufferNum))
                bufferNum = ""
            else:
                bufferNum += currentLine[i]
            
            if i == len(currentLine) - 1:
                if bufferNum != "": yourNumbers.append(int(bufferNum))
                bufferNum = ""

        winCount = 0

        for number in yourNumbers:
            if number in winningNumbers: winCount += 1
        
        idsToAdd = []
        print(id)

        for t in range(copyList[id - 1]):
            for i in range(1, winCount + 1):
                idsToAdd.append(id + i)

        for id2 in idsToAdd:
            copyList[id2 - 1] += 1
        
        counter += 1
        
totalNum = 0
for i in range(len(copyList)):
    totalNum += copyList[i]
print(totalNum)