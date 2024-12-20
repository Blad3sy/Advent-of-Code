from sys import setrecursionlimit
setrecursionlimit(10000)

from copy import deepcopy

with open("2024/files/day20input.txt") as file:
    fileLines = file.readlines()

grid = [list(line.strip("\n")) for line in fileLines]

nodes = []
walls = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#": walls.append((i, j))
        else: nodes.append((i, j))

        if grid[i][j] == "S": start = (i, j)
        elif grid[i][j] == "E": end = (i, j)

def djikstras(node):
    print(len(unvisited))
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for dir in dirs:
        newNode = (node[0] + dir[0], node[1] + dir[1])
        if newNode in unvisited: 
            newDistance = distances[node] + 1

            newPath = deepcopy(paths[node])
            newPath.append(newNode)

            if newDistance < distances[newNode]: 
                distances[newNode] = newDistance              
                paths[newNode] = newPath

    unvisited.remove(node)

    min = None
    for nextNode in unvisited:
        if not min: min = nextNode
        elif distances[nextNode] < distances[min]:
            min = nextNode
    if min: djikstras(min)

distances = {}
paths = {}
inf = 1000000000000000000
for node in nodes: 
    distances[node] = inf
    paths[node] = []
distances[start] = 0
paths[start] = [start]
unvisited = nodes.copy()

djikstras(start)

shortestPath = paths[end]
baseline = len(shortestPath)
timeSaves = []

count = 1
for node in shortestPath:
    print(count, "/", baseline)
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for dir in dirs:
        midNode = (node[0] + dir[0], node[1] + dir[1])
        newNode = (node[0] +  2 * dir[0], node[1] + 2 * dir[1])
        if newNode in shortestPath and midNode in walls:
            newPath = []
            skipStartIndex = shortestPath.index(node) + 1
            skipEndIndex = shortestPath.index(newNode)

            length = baseline - (skipEndIndex - skipStartIndex)
            if length < baseline:
                timeSaves.append(baseline - length - 1)
    
    count += 1

count = 0
for timeSave in timeSaves:
    if timeSave >= 100: count += 1
print(count)