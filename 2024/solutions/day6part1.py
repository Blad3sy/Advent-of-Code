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

recordingGrid = deepcopy(grid)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "^":
            xPos = j
            yPos = i

dir = "^"
while xPos >= 0 and xPos < len(grid[0]) and yPos >= 0 and yPos < len(grid):
    recordingGrid[yPos][xPos] = "X"
    coordinateOffset = getTravel(dir)

    try:
        if grid[yPos + coordinateOffset[0]][xPos + coordinateOffset[1]] == "#":
            dir = rotate(dir)
            continue
    except IndexError: pass

    yPos += coordinateOffset[0]
    xPos += coordinateOffset[1]

count = 0
for line in recordingGrid:
    for char in line:
        if char == "X": count += 1

print(count)