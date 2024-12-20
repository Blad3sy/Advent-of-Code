from sys import setrecursionlimit
from datetime import datetime
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
distances[end] = 0
paths[end] = [end]
unvisited = nodes.copy()

djikstras(end)

shortestPath = paths[start]
shortestPath.reverse()
baseline = len(shortestPath) - 1
timeSaves = []

count = 1
for node in shortestPath:
    print(count, "/", baseline)
    now = datetime.now()

    for i in range(-20, 21):
        for j in range(-20, 21):
            newNode = (node[0] + i, node[1] + j)
            skipDistance = abs(i) + abs(j)
            if newNode in nodes and distances[newNode] < distances[node] and skipDistance <= 20:
                skipStartIndex = shortestPath.index(node)

                length = distances[newNode] + skipStartIndex + skipDistance
                timeSave = baseline - length
                if timeSave >= 100:
                    timeSaves.append(timeSave)
    
    count += 1

    skipTime = datetime.now() - now
    print(f"Estimated time remaining: {skipTime * (baseline - count)}")

print(len(timeSaves))