import sys
sys.setrecursionlimit(10000)

mapsize = 71
bits = 1024

distances = {}
unvisited = []

def findPath(coords):
    global distances
    global unvisited

    print(len(unvisited))
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    unvisited.remove(coords)

    for dir in dirs:
        newCoords = (coords[0] + dir[0], coords[1] + dir[1])
        if newCoords not in unvisited: continue
        if newCoords[0] in range(mapsize) and newCoords[1] in range(mapsize):
            if grid[coords[0]][coords[1]] == ".":
                newDist = distances[coords] + 1
                if newDist < distances[newCoords]: distances[newCoords] = newDist               
                
    min = None
    for coord in unvisited:
        if not min: min = coord
        else:
            if distances[coord] < distances[min]:
                min = coord
    
    if min: findPath(min)

with open("2024/files/day18input.txt") as file:
    fileLines = file.readlines()

grid = [["." for i in range(mapsize)] for i in range(mapsize)]
start = (0, 0)
exit = (mapsize - 1, mapsize - 1)

for i in range(bits):
    line = fileLines[i]
    coords = [int(value) for value in line.strip("\n").split(",")]
    grid[coords[1]][coords[0]] = "#"

for i in range(mapsize):
    for j in range(mapsize):
        if grid[i][j] == ".": 
            unvisited.append((i, j))
            distances[(i, j)] = 10000000000000
distances[start] = 0

findPath(start)
print(distances[exit])