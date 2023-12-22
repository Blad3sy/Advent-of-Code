import numpy as np
import os

# https://en.wikipedia.org/wiki/Shoelace_formula
# https://www.101computing.net/the-shoelace-algorithm/
# Had to switch implementation as numpy handles 32+bit integers badly, apparently.

def shoelace(vertices):
    numberOfVertices = len(vertices)
    sum1 = 0
    sum2 = 0
  
    for i in range(0,numberOfVertices-1):
        sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
        sum2 = sum2 + vertices[i][1] *  vertices[i+1][0]
  
    sum1 = sum1 + vertices[numberOfVertices-1][0]*vertices[0][1]   
    sum2 = sum2 + vertices[0][0]*vertices[numberOfVertices-1][1]   
  
    area = abs(sum1 - sum2) / 2
    return area

# https://en.wikipedia.org/wiki/Pick%27s_theorem
def pick(area, perimeter):
    interiors = area
    interiors -= perimeter / 2
    interiors += 1
    return interiors

def convertHex(hexnum):
    directionNum = hexnum[-1]
    lengthNum = hexnum[:5]
    returnArray = []

    if directionNum == "0": returnArray.append("R")
    if directionNum == "1": returnArray.append("D")
    if directionNum == "2": returnArray.append("L")
    if directionNum == "3": returnArray.append("U")

    returnArray.append(int(lengthNum, 16))

    return returnArray

with open("Advent-of-Code-2023/2023/files/day18input.txt", "r") as file:
    fileLines = file.readlines()

    for i in range(len(fileLines)):
        fileLines[i] = fileLines[i].strip().split()
        fileLines[i] = fileLines[i][-1]
        fileLines[i] = fileLines[i].replace("(", "")
        fileLines[i] = fileLines[i].replace(")", "")
        fileLines[i] = fileLines[i].replace("#", "")
        fileLines[i] = convertHex(fileLines[i])

vertexArray = [[0, 0]]
coordArray = []
currentVertex = [0, 0]
perimeter = 0

counter = 1
for line in fileLines:
    os.system('cls||clear')
    print(f"{counter} / {len(fileLines)}")
    counter += 1

    if line[0] == "U":
        cVcopy = currentVertex.copy()
        currentVertex[0] -= int(line[1])
        perimeter += abs(currentVertex[0] - cVcopy[0])

    elif line[0] == "R":
        cVcopy = currentVertex.copy()
        currentVertex[1] += int(line[1])
        perimeter += abs(currentVertex[1] - cVcopy[1])

    elif line[0] == "D":
        cVcopy = currentVertex.copy()
        currentVertex[0] += int(line[1])
        perimeter += abs(currentVertex[0] - cVcopy[0])

    else:
        cVcopy = currentVertex.copy()
        currentVertex[1] -= int(line[1])
        perimeter += abs(currentVertex[1] - cVcopy[1])
    
    vertexArray.append(currentVertex.copy())

area = shoelace(vertexArray)
interiorPoints = pick(area, perimeter)

print(area)
print(perimeter)
print(interiorPoints)

print(perimeter + interiorPoints)