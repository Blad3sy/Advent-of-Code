from copy import deepcopy
import os

def moveRobot(grid, instruction, position):
    tempgrid = deepcopy(grid)
    movementObject = tempgrid[position[0]][position[1]]

    if instruction == ">":
        if tempgrid[position[0]][position[1] + 1] == ".":
            tempgrid[position[0]][position[1] + 1] = movementObject
            tempgrid[position[0]][position[1]] = "."
        
        elif tempgrid[position[0]][position[1] + 1] == "[":
            tempgrid, changeHappen = pushBox(tempgrid, instruction, [position[0], position[1] + 1], [position[0], position[1] + 2])
            if changeHappen:
                tempgrid[position[0]][position[1] + 1] = movementObject
                tempgrid[position[0]][position[1]] = "."           

    elif instruction == "^":
        if tempgrid[position[0] - 1][position[1]] == ".":
            tempgrid[position[0] - 1][position[1]] = movementObject
            tempgrid[position[0]][position[1]] = "."
        
        elif tempgrid[position[0] - 1][position[1]] == "[":
            tempgrid, changeHappen = pushBox(tempgrid, instruction, [position[0] - 1, position[1]], [position[0] - 1, position[1] + 1])
            if changeHappen:
                tempgrid[position[0] - 1][position[1]] = movementObject
                tempgrid[position[0]][position[1]] = "."

        elif tempgrid[position[0] - 1][position[1]] == "]":
            tempgrid, changeHappen = pushBox(tempgrid, instruction, [position[0] - 1, position[1] - 1], [position[0] - 1, position[1]])
            if changeHappen:
                tempgrid[position[0] - 1][position[1]] = movementObject
                tempgrid[position[0]][position[1]] = "."

    elif instruction == "<":
        if tempgrid[position[0]][position[1] - 1] == ".":
            tempgrid[position[0]][position[1] - 1] = movementObject
            tempgrid[position[0]][position[1]] = "."
        
        elif tempgrid[position[0]][position[1] - 1] == "]":
            tempgrid, changeHappen = pushBox(tempgrid, instruction, [position[0], position[1] - 2], [position[0], position[1] - 1])
            if changeHappen:
                tempgrid[position[0]][position[1] - 1] = movementObject
                tempgrid[position[0]][position[1]] = "."

    elif instruction == "v":
        if tempgrid[position[0] + 1][position[1]] == ".":
            tempgrid[position[0] + 1][position[1]] = movementObject
            tempgrid[position[0]][position[1]] = "."
        
        elif tempgrid[position[0] + 1][position[1]] == "[":
            tempgrid, changeHappen = pushBox(tempgrid, instruction, [position[0] + 1, position[1]], [position[0] + 1, position[1] + 1])
            if changeHappen:
                tempgrid[position[0] + 1][position[1]] = movementObject
                tempgrid[position[0]][position[1]] = "."

        elif tempgrid[position[0] + 1][position[1]] == "]":
            tempgrid, changeHappen = pushBox(tempgrid, instruction, [position[0] + 1, position[1] - 1], [position[0] + 1, position[1]])
            if changeHappen:
                tempgrid[position[0] + 1][position[1]] = movementObject
                tempgrid[position[0]][position[1]] = "."

    return tempgrid

def pushBox(grid, instruction, pos1, pos2):
    tempgrid = deepcopy(grid)
    change = False

    if instruction == ">":
        if tempgrid[pos2[0]][pos2[1] + 1] == ".":
            tempgrid[pos1[0]][pos1[1] + 1] = "["
            tempgrid[pos2[0]][pos2[1] + 1] = "]"

            tempgrid[pos1[0]][pos1[1]] = "."

            change = True
        
        elif tempgrid[pos2[0]][pos2[1] + 1] == "[":
            tempgrid, changeHappen = pushBox(tempgrid, instruction, [pos2[0], pos2[1] + 1], [pos2[0], pos2[1] + 2])
            if changeHappen:
                tempgrid[pos1[0]][pos1[1] + 1] = "["
                tempgrid[pos2[0]][pos2[1] + 1] = "]"

                tempgrid[pos1[0]][pos1[1]] = "."

                change = True                

    elif instruction == "^":
        if tempgrid[pos1[0] - 1][pos1[1]] == "." and tempgrid[pos2[0] - 1][pos2[1]] == ".":
            tempgrid[pos1[0] - 1][pos1[1]] = "["
            tempgrid[pos2[0] - 1][pos2[1]] = "]"

            tempgrid[pos1[0]][pos1[1]] = "."
            tempgrid[pos2[0]][pos2[1]] = "."

            change = True
        
        else:
            changeHappen = False
            check1 = False
            check2 = False
            changeHappen1 = False
            changeHappen2 = False

            if tempgrid[pos1[0] - 1][pos1[1]] == "[":
                tempgrid, changeHappen = pushBox(tempgrid, instruction, [pos1[0] - 1, pos1[1]], [pos2[0] - 1, pos2[1]])
        
            if tempgrid[pos1[0] - 1][pos1[1]] == "]":
                check1 = True
                tempgrid, changeHappen1 = pushBox(tempgrid, instruction, [pos1[0] - 1, pos1[1] - 1], [pos1[0] - 1, pos1[1]])

            if tempgrid[pos2[0] - 1][pos2[1]] == "[":
                check2 = True
                tempgrid, changeHappen2 = pushBox(tempgrid, instruction, [pos2[0] - 1, pos2[1]], [pos2[0] - 1, pos2[1] + 1])
            
            if (check1 and check2) and (changeHappen1 != changeHappen2): return grid, False
        
            if changeHappen or changeHappen1 or changeHappen2:
                if tempgrid[pos1[0] - 1][pos1[1]] == "#" or tempgrid[pos2[0] - 1][pos2[1]] == "#": return grid, False          
                tempgrid[pos1[0] - 1][pos1[1]] = "["
                tempgrid[pos2[0] - 1][pos2[1]] = "]"

                tempgrid[pos1[0]][pos1[1]] = "."
                tempgrid[pos2[0]][pos2[1]] = "."

                change = True


    elif instruction == "<":
        if tempgrid[pos1[0]][pos1[1] - 1] == ".":
            tempgrid[pos1[0]][pos1[1] - 1] = "["
            tempgrid[pos2[0]][pos2[1] - 1] = "]"

            tempgrid[pos2[0]][pos2[1]] = "."

            change = True

        elif tempgrid[pos1[0]][pos1[1] - 1] == "]":
            tempgrid, changeHappen = pushBox(tempgrid, instruction, [pos1[0], pos1[1] - 2], [pos1[0], pos1[1] - 1])
            if changeHappen:
                tempgrid[pos1[0]][pos1[1] - 1] = "["
                tempgrid[pos2[0]][pos2[1] - 1] = "]"

                tempgrid[pos2[0]][pos2[1]] = "."

                change = True   

    elif instruction == "v":
        changeHappen = False
        if tempgrid[pos1[0] + 1][pos1[1]] == "." and tempgrid[pos2[0] + 1][pos2[1]] == ".":
            tempgrid[pos1[0] + 1][pos1[1]] = "["
            tempgrid[pos2[0] + 1][pos2[1]] = "]"

            tempgrid[pos1[0]][pos1[1]] = "."
            tempgrid[pos2[0]][pos2[1]] = "."

            change = True
        
        else:
            changeHappen = False
            check1 = False
            check2 = False
            changeHappen1 = False
            changeHappen2 = False

            if tempgrid[pos1[0] + 1][pos1[1]] == "[":
                tempgrid, changeHappen = pushBox(tempgrid, instruction, [pos1[0] + 1, pos1[1]], [pos2[0] + 1, pos2[1]])
        
            if tempgrid[pos1[0] + 1][pos1[1]] == "]":
                check1 = True
                tempgrid, changeHappen1 = pushBox(tempgrid, instruction, [pos1[0] + 1, pos1[1] - 1], [pos1[0] + 1, pos1[1]])

            if tempgrid[pos2[0] + 1][pos2[1]] == "[":
                check2 = True
                tempgrid, changeHappen2 = pushBox(tempgrid, instruction, [pos2[0] + 1, pos2[1]], [pos2[0] + 1, pos2[1] + 1])

            if (check1 and check2) and (changeHappen1 != changeHappen2): return grid, False

            if changeHappen or changeHappen1 or changeHappen2:
                if tempgrid[pos1[0] + 1][pos1[1]] == "#" or tempgrid[pos2[0] + 1][pos2[1]] == "#": return grid, False        
                tempgrid[pos1[0] + 1][pos1[1]] = "["
                tempgrid[pos2[0] + 1][pos2[1]] = "]"

                tempgrid[pos1[0]][pos1[1]] = "."
                tempgrid[pos2[0]][pos2[1]] = "."

                change = True
    
    return tempgrid, change

with open("2024/files/day15input.txt") as file:
    fileLines = file.readlines()

for i in range(len(fileLines)):
    if fileLines[i] == "\n": break
    newline = ""
    for char in fileLines[i]:
        if char == "#": newline += "##"
        elif char == "O": newline += "[]"
        elif char == ".": newline += ".."
        elif char == "@": newline += "@."
    
    fileLines[i] = newline

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
count = 1
for instruction in instructions:
    print("Move:", instruction, count, "/", len(instructions))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@": robotPos = [i, j]

    grid = moveRobot(grid, instruction, robotPos)
    count += 1

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "[":
            total += i * 100
            total += j
print(total)