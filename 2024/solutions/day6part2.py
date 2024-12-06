from copy import deepcopy

def getTravel(dir):
    match dir:
        case "^": return [-1, 0]
        case ">": return [0, 1]
        case "v": return [1, 0]
        case "<": return [0, -1]
    
def rotate(dir):
    match dir:
        case "^": return ">"
        case ">": return "v"
        case "v": return "<"
        case "<": return "^"

with open("2024/files/day6input.txt") as file:
    fileLines = file.readlines()

grid = []
for line in fileLines:
    grid.append(list(line.strip("\n")))

originalGrid = deepcopy(grid)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "^":
            oxPos = j
            oyPos = i

loopCount = 0

for i in range(len(grid)):
    print(f"{i + 1} / {len(grid)}")
    for j in range(len(grid[i])):
        grid = deepcopy(originalGrid)
        grid[i][j] = "#"
        xPos = oxPos
        yPos = oyPos

        dir = "^"
        collisionRecord = []
        while xPos >= 0 and xPos < len(grid[0]) and yPos >= 0 and yPos < len(grid):
            coordinateOffset = getTravel(dir)

            try:
                if grid[yPos + coordinateOffset[0]][xPos + coordinateOffset[1]] == "#":
                    record = [[yPos + coordinateOffset[0], xPos + coordinateOffset[1]], dir]
                    if record in collisionRecord:
                        loopCount += 1
                        break
                    else: collisionRecord.append(record)

                    dir = rotate(dir)
                    continue
            except IndexError: pass

            yPos += coordinateOffset[0]
            xPos += coordinateOffset[1]

print(loopCount)