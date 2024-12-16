from copy import deepcopy
import sys
import functools
from os import system

sys.setrecursionlimit(100000)

scores = []

def rotationScore(direction1, direction2):
    map = {
        "U":
        {
            "L": 1000, "R":1000, "U":0, "D": 2000
        },
        "D":
        {
            "L": 1000, "R":1000, "U":2000, "D": 0
        },
        "L":
        {
            "L": 0, "R": 2000, "U": 1000, "D": 1000
        },
        "R":
        {
            "L": 2000, "R": 0, "U": 1000, "D": 1000
        }
    }

    return map[direction1][direction2]

nodes = {}
def makeNodes(position, direction):
    nodes[(position, direction)] = {}
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    dirStrs = ["U", "D", "L", "R"]

    if grid[position[0]][position[1]] == "E":
        return

    for i in range(len(dirs)):
        dir = dirs[i]
        dirStr = dirStrs[i]
        newPos = (position[0] + dir[0], position[1] + dir[1])

        if grid[newPos[0]][newPos[1]] != "#":
            nodes[(position, direction)][(newPos, dirStr)] = 1 + rotationScore(direction, dirStr)

with open("2024/files/day16input.txt") as file:
    fileLines = file.readlines()

grid = [list(line.strip("\n")) for line in fileLines]

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
dirStrs = ["U", "D", "L", "R"] 
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != "#":
            for t in range(len(dirs)):
                if i - dirs[t][0] in range(len(grid)) and j - dirs[t][1] in range(len(grid[i])):
                    if grid[i - dirs[t][0]][j - dirs[t][1]] != "#": makeNodes((i, j), dirStrs[t])
        if grid[i][j] == "S":
            startPos = ((i, j), "R")
        if grid[i][j] == "E":
            endPos = (i, j)

makeNodes(startPos[0], startPos[1])

distances = {}
for node in nodes.keys():
    distances[node] = 100000000000
distances[startPos] = 0

unvisited = list(nodes.keys())

def dijkstras(pos):
    global unvisited
    print(len(unvisited))
    for node in nodes[pos]:
        if node in unvisited:
            newDist = distances[pos] + nodes[pos][node]
            if newDist < distances[node]: distances[node] = newDist
    
    unvisited.remove(pos)

    nextPos = None
    for node in unvisited:
        if not nextPos: nextPos = node
        else:
            if distances[node] < distances[nextPos]: nextPos = node
    
    if nextPos: dijkstras(nextPos)

dijkstras(startPos)

finals = []
for dir in dirStrs:
    key = (endPos, dir)
    if key in distances.keys(): finals.append(distances[key])
print(min(finals))