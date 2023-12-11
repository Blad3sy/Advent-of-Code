with open("Advent-of-Code-2023/solutions/files/day11input.txt", "r") as file:
    fileLines = file.readlines()

# EXPANDER

rowsToAdd = []
for i in range(len(fileLines)):
    if "#" not in fileLines[i]:
        rowsToAdd.append(i)

columnsToAdd = []
for t in range(len(fileLines[0]) - 1):
    column = ""
    for i in range(len(fileLines)):
        column += fileLines[i][t]
    if "#" not in column:
        columnsToAdd.append(t)

addString = ""
for i in range(len(fileLines[0]) - 1):
    addString += "."

for i in range(len(rowsToAdd)):
    fileLines.insert(rowsToAdd[i] + i, addString)

offset = 0
for i in range(len(columnsToAdd)):
    for t in range(len(fileLines)):
        fileLines[t] = fileLines[t][0:columnsToAdd[i] + offset] + "." + fileLines[t][columnsToAdd[i] + offset:]
    offset += 1

# EXPANDER DONE
print("DONE EXPANDING")
galaxyList = []

for i in range(len(fileLines)):
    for t in range(len(fileLines[i])):
        if fileLines[i][t] == "#":
            galaxyList.append([i, t])

total = 0
doneList = []

for i in range(len(galaxyList)):
    print(i + 1)
    for t in range(len(galaxyList)):

        '''doneCheck = []
        if i > t:
            doneCheck = [i, t]
        else:
            doneCheck = [t, i]'''

        if i != t: # and doneCheck not in doneList:
            xdif = abs(galaxyList[i][0] - galaxyList[t][0])
            ydif = abs(galaxyList[i][1] - galaxyList[t][1])
            
            # doneList.append(doneCheck)

            total += xdif + ydif

print(total / 2)