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

        if mainMap[currentPos[0]][currentPos[1]] == ".":
            mainMap[currentPos[0]][currentPos[1]] = "#"

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

with open("Advent-of-Code/2023/solutions/files/day16input.txt", "r") as file:
    fileLines = file.readlines()
    emptymap = []

    for i in range(len(fileLines)):
        fileLines[i] = [value for value in fileLines[i] if value != "\n"] 
        emptymap.append(["." for value in fileLines[i] if value != "\n"])

splittersUsed = []

startPos = [0, 0]
startDir = dirConvert("E", fileLines[startPos[0]][startPos[1]])

move(startPos, startDir)

total = 0
for line in emptymap:
    for letter in line:
        if letter == "#":
            total += 1
print(total)