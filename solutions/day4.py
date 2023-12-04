with open("Advent-of-Code-2023/solutions/files/day4input.txt", "r") as file:
    fileLines = file.readlines()
    total = 0

    for i in range(len(fileLines)):
        currentLine = fileLines[i]

        for i in range(len(currentLine)):
            if currentLine[i] == ":":
                currentLine = currentLine[i + 1:]
                break
        
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

        points = 0
        for number in yourNumbers:
            if number in winningNumbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        
        total += points

print(total)

# FIRST TRY PART 1 WOOOOOOO