def gridExpand():
    print("expanded")
    global grid

    global gridHeight
    global gridWidth

    for i in range(len(grid)):
        grid[i] = convert(grid[i]) + grid[i] + convert(grid[i])
    
    gridWidth = len(grid[0])

    for i in range(len(grid)):
        grid.append(convert(grid[i]))
    
    for i in range(1, int(len(grid) / 2) + 1):
        grid.insert(0, convert(grid[-i]))
    
    gridHeight = len(grid)

def convert(list):
    list = "".join(list)
    list = [char for char in list.strip().replace("O", ".")]
    return list

def getO(maingrid):
    print("GETO START")
    total = 0
    for list in maingrid:
        list = "".join(list)
        list = [char for char in list.strip() if char == "O"]
        total += len(list)
    print(total)
    return total

def getOIndices():
    global grid

    Oindices = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                Oindices.append([i, j])

    return Oindices

with open("Advent-of-Code-2023/2023/files/day21input.txt", "r") as file:
    fileLines = file.readlines()
    grid = []
    
    for line in fileLines:
        line = [char for char in line.strip().replace("S", "O")]
        grid.append(line)

origGridHeight = len(grid)
origGridWidth = len(grid[0])

gridHeight = len(grid)
gridWidth = len(grid[0])

maxSteps = 330
criticalValues = []

for z in range(1, maxSteps + 1):
    print(z)

    '''for row in grid:
        for char in row:
            print(char, end = "")
        print("\n", end = "")
    print()'''

    Oindices = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                Oindices.append([i, j])
        
    for Oindex in Oindices:
        if Oindex[0] == 0 or Oindex[0] == gridHeight - 1 or Oindex[1] == 0 or Oindex[0] == gridWidth - 1:
            gridExpand()
            Oindices = getOIndices()
            break
    
    for Oindex in Oindices:
        north = [Oindex[0] - 1, Oindex[1]]
        east = [Oindex[0], Oindex[1] + 1]
        south = [Oindex[0] + 1, Oindex[1]]
        west = [Oindex[0], Oindex[1] - 1]

        if grid[north[0]][north[1]] != "#":
            grid[north[0]][north[1]] = "O"
        
        if grid[east[0]][east[1]] != "#":
            grid[east[0]][east[1]] = "O"

        if grid[south[0]][south[1]] != "#":
            grid[south[0]][south[1]] = "O"

        if grid[west[0]][west[1]] != "#":
            grid[west[0]][west[1]] = "O"
        
        grid[Oindex[0]][Oindex[1]] = "."
    
    if z == 65 or z == 196 or z == 327:
        criticalValues.append(getO(grid))
    
    '''for row in grid:
        for char in row:
            print(char, end = "")
        print("\n", end = "")
    print()'''

print(criticalValues)
# criticalValues = [3734, 33285, 92268]

n = 131
goal = 26501365
def f(n):
    print(n)
    a0 = 3734
    a1 = 33285
    a2 = 92268

    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)

print(f(goal//n))

# 602259568764234
# Thanks to https://www.reddit.com/r/adventofcode/comments/18nevo3/2023_day_21_solutions/keat9hm/?context=3 for this function that saves me the effort of wolfram-alpha'ing every time I fuck up