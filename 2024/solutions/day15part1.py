def pushBox(grid, instruction, position):
    tempgrid = grid.copy()
    movementObject = tempgrid[position[0]][position[1]]
    change = False

    if instruction == ">":
        if tempgrid[position[0]][position[1] + 1] == ".":
            tempgrid[position[0]][position[1] + 1] = movementObject
            tempgrid[position[0]][position[1]] = "."
            change = True
        
        elif tempgrid[position[0]][position[1] + 1] == "O":
            tempgrid, changeHappen = pushBox(tempgrid, instruction, [position[0], position[1] + 1])
            if changeHappen:
                tempgrid[position[0]][position[1] + 1] = movementObject
                tempgrid[position[0]][position[1]] = "."
                change = True             

    elif instruction == "^":
        if tempgrid[position[0] - 1][position[1]] == ".":
            tempgrid[position[0] - 1][position[1]] = movementObject
            tempgrid[position[0]][position[1]] = "."
            change = True
        
        elif tempgrid[position[0] - 1][position[1]] == "O":
            tempgrid, changeHappen = pushBox(tempgrid, instruction, [position[0] - 1, position[1]])
            if changeHappen:
                tempgrid[position[0] - 1][position[1]] = movementObject
                tempgrid[position[0]][position[1]] = "."
                change = True 

    elif instruction == "<":
        if tempgrid[position[0]][position[1] - 1] == ".":
            tempgrid[position[0]][position[1] - 1] = movementObject
            tempgrid[position[0]][position[1]] = "."
            change = True
        
        elif tempgrid[position[0]][position[1] - 1] == "O":
            tempgrid, changeHappen = pushBox(tempgrid, instruction, [position[0], position[1] - 1])
            if changeHappen:
                tempgrid[position[0]][position[1] - 1] = movementObject
                tempgrid[position[0]][position[1]] = "."
                change = True 

    elif instruction == "v":
        if tempgrid[position[0] + 1][position[1]] == ".":
            tempgrid[position[0] + 1][position[1]] = movementObject
            tempgrid[position[0]][position[1]] = "."
            change = True
        
        elif tempgrid[position[0] + 1][position[1]] == "O":
            tempgrid, changeHappen = pushBox(tempgrid, instruction, [position[0] + 1, position[1]])
            if changeHappen:
                tempgrid[position[0] + 1][position[1]] = movementObject
                tempgrid[position[0]][position[1]] = "."
                change = True 

    return tempgrid, change

with open("2024/files/day15input.txt") as file:
    fileLines = file.readlines()

grid = []
instructionMode = False
instructions = ""
for line in fileLines:
    if line == "\n": 
        instructionMode = True
        continue

    if instructionMode: instructions += line.strip("\n")
    else: grid.append(list(line.strip("\n")))

robotPos = []

for instruction in instructions:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@": robotPos = [i, j]

    grid, changes = pushBox(grid, instruction, robotPos)

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "O":
            total += i * 100
            total += j
print(total)