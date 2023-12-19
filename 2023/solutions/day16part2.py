def dirConvert(dir, char):
    CONVERTER = {
        "/" : {
            "N" : "E",
            "S" : "W",
            "E" : "N",
            "W" : "S"
        },

        "\\" : {
            "N" : "W",
            "S" : "E",
            "E" : "S",
            "W" : "N"
        },

        "." : {
            "N" : "N",
            "S" : "S",
            "E" : "E",
            "W" : "W"
        },

        "#" : {
            "N" : "N",
            "S" : "S",
            "E" : "E",
            "W" : "W"
        },

        "-" : {
            "E" : "E",
            "W" : "W"
        },

        "|" : {
            "N" : "N",
            "S" : "S"
        }
    }

    return CONVERTER[char][dir]

def move(currentPos, currentDir):
    global fileLines
    global splittersUsed

    mainMap = fileLines

    while True:
        if currentPos[0] < 0: return True
        if currentPos[0] >= len(fileLines): return True
        if currentPos[1] < 0: return True
        if currentPos[1] >= len(fileLines[0]): return True

        emptymap[currentPos[0]][currentPos[1]] = "#"
        currentChar = mainMap[currentPos[0]][currentPos[1]]

        if currentChar == "|" and currentDir in "EW":
            break
        if currentChar == "-" and currentDir in "NS":
            break

        currentDir = dirConvert(currentDir, currentChar)
        if currentPos == startPos: currentDir = startDir

        if currentDir == "N":
            currentPos[0] -= 1
        elif currentDir == "S":
            currentPos[0] += 1
        elif currentDir == "E":
            currentPos[1] += 1
        elif currentDir == "W":
            currentPos[1] -= 1
    
    if currentPos not in splittersUsed:
        splittersUsed.append(currentPos.copy())
        currentChar = mainMap[currentPos[0]][currentPos[1]]

        if currentChar == "-":
            move([currentPos[0], currentPos[1] - 1], "W")
            move([currentPos[0], currentPos[1] + 1], "E")

        elif currentChar == "|":
            move([currentPos[0] - 1, currentPos[1]], "N")
            move([currentPos[0] + 1, currentPos[1]], "S")

def reset(startPosition, startDirection):
    global splittersUsed
    global startPos
    global startDir
    global emptymap
    global fileLines

    with open("Advent-of-Code/2023/solutions/files/day16input.txt", "r") as file:
        fileLines = file.readlines()
        emptymap = []

    for i in range(len(fileLines)):
        fileLines[i] = [value for value in fileLines[i] if value != "\n"] 
        emptymap.append(["." for value in fileLines[i] if value != "\n"])
    
    addBuffer()

    splittersUsed = []
    startPos = startPosition
    startChar = fileLines[startPos[0]][startPos[1]]
    startDir = dirConvert(startDirection, startChar)

def getTotal():
    global emptymap

    total = 0
    for line in emptymap:
        for letter in line:
            if letter == "#":
                total += 1

    return total

def addBuffer():
    global fileLines
    global emptymap

    fileLines.insert(0, ["." for value in fileLines[2] if value != "\n"])
    fileLines.append(["." for value in fileLines[2] if value != "\n"])

    emptymap.insert(0, ["." for value in fileLines[2] if value != "\n"])
    emptymap.append(["." for value in fileLines[2] if value != "\n"])

    for i in range(len(fileLines)):
        fileLines[i].insert(0, ".")
        fileLines[i].append(".")

        emptymap[i].insert(0, ".")
        emptymap[i].append(".")

def removeBuffer():
    global fileLines
    global emptymap

    fileLines.pop(0)
    fileLines.pop()

    emptymap.pop(0)
    emptymap.pop()

    for i in range(len(fileLines)):
        fileLines[i].pop(0)
        fileLines[i].pop()

    for i in range(len(emptymap)):
        emptymap[i].pop(0)
        emptymap[i].pop()

with open("Advent-of-Code/2023/solutions/files/day16input.txt", "r") as file:
    fileLines = file.readlines()
    emptymap = []

    for i in range(len(fileLines)):
        fileLines[i] = [value for value in fileLines[i] if value != "\n"] 
        emptymap.append(["." for value in fileLines[i] if value != "\n"])
    
    columnLength = len(fileLines) + 2
    rowLength = len(fileLines[0]) + 2

splittersUsed = []
startPos = [0, 0]
startDir = dirConvert("E", fileLines[startPos[0]][startPos[1]])

max = 0
for i in range(columnLength):
    print(i)
    reset([i, 0], "E")
    move(startPos, startDir)
    removeBuffer()
    if getTotal() > max: max = getTotal()

print("E DONE")

for i in range(columnLength):
    print(i)
    reset([i, -1], "W")
    move(startPos, startDir)
    removeBuffer()
    if getTotal() > max: max = getTotal()

print("W DONE")

for i in range(rowLength):
    print(i)
    if i != 93: reset([0, i], "S")
    move(startPos, startDir)
    removeBuffer()
    if getTotal() > max: max = getTotal()

print("S DONE")

for i in range(rowLength):
    print(i)
    reset([-1, i], "N")
    move(startPos, startDir)
    removeBuffer()
    if getTotal() > max: max = getTotal()

print("N DONE")

print(max)