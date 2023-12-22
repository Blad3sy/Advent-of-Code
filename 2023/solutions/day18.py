import numpy as np

# https://en.wikipedia.org/wiki/Shoelace_formula
# https://stackoverflow.com/questions/41077185/fastest-way-to-shoelace-formula
def shoelace(x_y):
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    y = x_y[:,1]

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)

    return area

# https://en.wikipedia.org/wiki/Pick%27s_theorem
def pick(area, perimeter):
    interiors = area
    interiors -= perimeter / 2
    interiors += 1
    return interiors

with open("Advent-of-Code-2023/2023/files/day18input.txt", "r") as file:
    fileLines = file.readlines()

    for i in range(len(fileLines)):
        fileLines[i] = fileLines[i].strip().split()
        fileLines[i] = fileLines[i][:2]

vertexArray = [[0, 0]]
coordArray = []
currentVertex = [0, 0]
maxx = 0
maxy = 0

for line in fileLines:
    if line[0] == "U":
        cVcopy = currentVertex.copy()
        for i in range(int(line[1])):
            cVcopy[0] -= 1
            coordArray.append(cVcopy.copy())

        currentVertex[0] -= int(line[1])

    elif line[0] == "R":
        cVcopy = currentVertex.copy()
        for i in range(int(line[1])):
            cVcopy[1] += 1
            coordArray.append(cVcopy.copy())

        currentVertex[1] += int(line[1])
        if currentVertex[1] > maxy:
            maxy = currentVertex[1]

    elif line[0] == "D":
        cVcopy = currentVertex.copy()
        for i in range(int(line[1])):
            cVcopy[0] += 1
            coordArray.append(cVcopy.copy())

        currentVertex[0] += int(line[1])
        if currentVertex[0] > maxx:
            maxx = currentVertex[0]

    else:
        cVcopy = currentVertex.copy()
        for i in range(int(line[1])):
            cVcopy[1] -= 1
            coordArray.append(cVcopy.copy())

        currentVertex[1] -= int(line[1])
    
    vertexArray.append(currentVertex.copy())

area = shoelace(vertexArray)
perimeter = len(coordArray)
interiorPoints = pick(area, perimeter)

print(perimeter + interiorPoints)