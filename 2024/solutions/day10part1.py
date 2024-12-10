def getConnections(gridmap, searchval, coords) -> set:
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    validDirs = set()

    for dir in dirs:
        newCoords = (coords[0] + dir[0], coords[1] + dir[1])
        if newCoords[0] >= 0 and newCoords[0] < len(gridmap) and newCoords[1] >= 0 and newCoords[1] < len(gridmap[0]):
            if gridmap[newCoords[0]][newCoords[1]] == searchval:
                if searchval == 9: validDirs.add(newCoords)
                else:
                    for value in getConnections(gridmap, searchval + 1, newCoords):
                        validDirs.add(value)
    
    return validDirs

with open("2024/files/day10input.txt") as file:
    fileLines = file.readlines()

gridmap = [[int(value) for value in list(line.strip("\n"))] for line in fileLines]

trailheads = {}
for i in range(len(gridmap)):
    for j in range(len(gridmap[i])):
        if gridmap[i][j] == 0:
            trailheads[(i, j)] = getConnections(gridmap, 1, (i, j))

sum = 0
for key in trailheads: sum += len(trailheads[key])
print(sum)