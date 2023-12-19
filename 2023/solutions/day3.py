with open("Advent-of-Code-2023/solutions/files/day3input.txt", "r") as file:
    total = 0
    fileList = file.readlines()
    symbolList = []
    for item in fileList:
        for letter in item:
            if not letter.isdigit() and not letter.isalpha() and letter != "." and letter != "\n" and letter not in symbolList:
                symbolList.append(letter)

    for i in range(0, 138): # Number of lines - 2 (138)
        prevLine = fileList[i]
        prevSymbols = []
        prevNums = []

        currentLine = fileList[i+1]
        currentSymbols = []
        currentNums = []

        nextLine = fileList[i+2]
        nextSymbols = []
        nextNums = []

        for i in range(len(prevLine)):
            if prevLine[i].isdigit():
                prevNums.append(i)
            elif prevLine[i] in symbolList:
                prevSymbols.append(i)
        
        for i in range(len(currentLine)):
            if currentLine[i].isdigit():
                currentNums.append(i)
            elif currentLine[i] in symbolList:
                currentSymbols.append(i)

        for i in range(len(nextLine)):  
            if nextLine[i].isdigit():
                nextNums.append(i)
            elif nextLine[i] in symbolList:
                nextSymbols.append(i)

        validPrevList = []
        validCurrentList = []
        validNextList = []

        # Nums and Symbols on the same line

        for i in range(len(prevNums)):
            if prevNums[i] - 1 in prevSymbols or prevNums[i] + 1 in prevSymbols:
                validPrevList.append(prevNums[i])

        for i in range(len(currentNums)):
            if currentNums[i] - 1 in currentSymbols or currentNums[i] + 1 in currentSymbols:
                validCurrentList.append(currentNums[i])

        for i in range(len(nextNums)):
            if nextNums[i] - 1 in nextSymbols or nextNums[i] + 1 in nextSymbols:
                validNextList.append(nextNums[i])

        # Nums and symbols on different lines

        for i in range(len(prevNums)):
            if prevNums[i] in currentSymbols or prevNums[i] - 1 in currentSymbols or prevNums[i] + 1 in currentSymbols:
                validPrevList.append(prevNums[i])
        
        for i in range(len(currentNums)):
            if currentNums[i] in prevSymbols or currentNums[i] - 1 in prevSymbols or currentNums[i] + 1 in prevSymbols:
                validCurrentList.append(currentNums[i])
            if currentNums[i] in nextSymbols or currentNums[i] - 1 in nextSymbols or currentNums[i] + 1 in nextSymbols:
                validCurrentList.append(currentNums[i])
        
        for i in range(len(nextNums)):
            if nextNums[i] in currentSymbols or nextNums[i] - 1 in currentSymbols or nextNums[i] + 1 in currentSymbols:
                validNextList.append(nextNums[i])

        validPrevList = list(set(validPrevList))
        validCurrentList = list(set(validCurrentList))
        validNextList = list(set(validNextList))

        validPrevList.sort()
        validCurrentList.sort()
        validNextList.sort()

        # Remove indices that occur sequentially

        deathList = []

        for i in range(len(validPrevList) - 1):
            if validPrevList[i] + 1 == validPrevList[i + 1]:
                deathList.append(i+1)

        validPrevList = [i for i in validPrevList if validPrevList.index(i) not in deathList]
        deathList = []

        for i in range(len(validCurrentList) - 1):
            if validCurrentList[i] + 1 == validCurrentList[i + 1]:
                deathList.append(i+1)

        validCurrentList = [i for i in validCurrentList if validCurrentList.index(i) not in deathList]
        deathList = []

        for i in range(len(validNextList) - 1):
            if validNextList[i] + 1 == validNextList[i + 1]:
                deathList.append(i+1)

        validNextList = [i for i in validNextList if validNextList.index(i) not in deathList]
        deathList = []

        # Change each number to start index of its number

        for i in range(len(validPrevList)):
            while True:
                if prevLine[validPrevList[i] - 1].isdigit():
                    validPrevList[i] -= 1
                else:
                    break
        
        for i in range(len(validCurrentList)):
            while True:
                if currentLine[validCurrentList[i] - 1].isdigit():
                    validCurrentList[i] -= 1
                else:
                    break

        for i in range(len(validNextList)):
            while True:
                if nextLine[validNextList[i] - 1].isdigit():
                    validNextList[i] -= 1
                else:
                    break

        # Turn indices back into numbers

        numList = []
        
        for item in validCurrentList:
            bufferNum = ""
            for i in range(item, len(currentLine)):
                if currentLine[i].isdigit():
                    bufferNum += currentLine[i]
                else:
                    break
            if bufferNum != "": numList.append(int(bufferNum))
        
        print(numList)
        # Add to total

        for item in numList:
            total += item
    
    print(total)

    # i hate this but I had to manually add on the bottom and top line numbers as they aren't included.... I could've done it but it would've been just an annoying amount of extra work