with open("Advent-of-Code-2023/solutions/files/day3input.txt", "r") as file:
    fullList = file.readlines()
    total = 0

    for i in range(0, 138):
        prevLine = fullList[i]
        currentLine = fullList[i+1]
        nextLine = fullList[i+2]

        asterlist = []

        # Get index of asterisks

        for i in range(len(currentLine)):
            if currentLine[i] == "*":
                asterlist.append(i)

        for asterisk in asterlist:
            connectcounter = 2

            validPrevList = []
            validCurrentList = []
            validNextList = []

            # Check same line

            if currentLine[asterisk - 1].isdigit():
                validCurrentList.append(asterisk - 1)

            if currentLine[asterisk + 1].isdigit():
                validCurrentList.append(asterisk + 1)

            # Check above line

            if prevLine[asterisk - 1].isdigit():
                validPrevList.append(asterisk - 1)

            if prevLine[asterisk + 1].isdigit():
                validPrevList.append(asterisk + 1)
            
            if prevLine[asterisk].isdigit():
                validPrevList.append(asterisk)
        
            # Check below line

            if nextLine[asterisk - 1].isdigit():
                validNextList.append(asterisk - 1)

            if nextLine[asterisk + 1].isdigit():
                validNextList.append(asterisk + 1)
            
            if nextLine[asterisk].isdigit():
                validNextList.append(asterisk)

            if connectcounter == 2:
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

                for item in validPrevList:
                    bufferNum = ""
                    for i in range(item, len(prevLine)):
                        if prevLine[i].isdigit():
                            bufferNum += prevLine[i]
                        else:
                            break
                    if bufferNum != "": numList.append(int(bufferNum))
        
                for item in validCurrentList:
                    bufferNum = ""
                    for i in range(item, len(currentLine)):
                        if currentLine[i].isdigit():
                            bufferNum += currentLine[i]
                        else:
                            break
                    if bufferNum != "": numList.append(int(bufferNum))

                for item in validNextList:
                    bufferNum = ""
                    for i in range(item, len(nextLine)):
                        if nextLine[i].isdigit():
                            bufferNum += nextLine[i]
                        else:
                            break
                    if bufferNum != "": numList.append(int(bufferNum))

                print(numList)
                numList = list(set(numList))
                print(numList)
                if len(numList) == 2:
                    gearRatio = numList[0] * numList[1]
                    total += gearRatio

print(total)