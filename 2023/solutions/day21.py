with open("Advent-of-Code-2023/2023/files/day21input.txt", "r") as file:
    fileLines = file.readlines()
    grid = []
    
    for line in fileLines:
        line = [char for char in line.strip().replace("S", "O")]
        grid.append(line)

gridHeight = len(grid)
gridWidth = len(grid[0])

print(gridHeight, gridWidth)

'''for row in grid:
    for step in row:
        print(step, end = "")
    print("\n", end = "")'''

maxSteps = 64

for i in range(maxSteps):

    Oindices = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                Oindices.append([i, j])
    
    for Oindex in Oindices:
        north = [Oindex[0] - 1, Oindex[1]]
        east = [Oindex[0], Oindex[1] + 1]
        south = [Oindex[0] + 1, Oindex[1]]
        west = [Oindex[0], Oindex[1] - 1]

        if north[0] in range(gridHeight) and north[1] in range(gridWidth) and grid[north[0]][north[1]] != "#":
            grid[north[0]][north[1]] = "O"
        
        if east[0] in range(gridHeight) and east[1] in range(gridWidth) and grid[east[0]][east[1]] != "#":
            grid[east[0]][east[1]] = "O"

        if south[0] in range(gridHeight) and south[1] in range(gridWidth) and grid[south[0]][south[1]] != "#":
            grid[south[0]][south[1]] = "O"

        if west[0] in range(gridHeight) and west[1] in range(gridWidth) and grid[west[0]][west[1]] != "#":
            grid[west[0]][west[1]] = "O"
        
        grid[Oindex[0]][Oindex[1]] = "."

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "O":
            total += 1
print(total)