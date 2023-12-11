def getNumBiggerThan(empties, coord): # x = 0, y = 1
    galaxiesLessThan = [value for value in empties if value < coord]
    return len(galaxiesLessThan)

with open("Advent-of-Code-2023/solutions/files/day11input.txt", "r") as file:
    fileLines = file.readlines()

expansionFactor = 999999

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
    # print(i + 1)
    for t in range(len(galaxyList)):
        if i != t:
            xco1 = galaxyList[i][1]
            xco1 += getNumBiggerThan(columnsToAdd, xco1) * expansionFactor

            xco2 = galaxyList[t][1]
            xco2 += getNumBiggerThan(columnsToAdd, xco2) * expansionFactor

            yco1 = galaxyList[i][0]
            yco1 += getNumBiggerThan(rowsToAdd, yco1) * expansionFactor

            yco2 = galaxyList[t][0]
            yco2 += getNumBiggerThan(rowsToAdd, yco2) * expansionFactor

            xdif = abs(xco1 - xco2)
            ydif = abs(yco1 - yco2)
            
            total += xdif + ydif

print(total / 2)