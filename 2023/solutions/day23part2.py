import sys
sys.setrecursionlimit(10000)

class Tree():
    def __init__(self):
        # node : neighbours
        self.nodes = {}
        self.nodeCount = 0

        self.stack = []
        self.visited = {}
    
    def addNode(self, node, neighbours):
        self.nodes[node] = neighbours
        self.nodeCount += 1
    
    def getAllNodes(self):
        return list(self.nodes.keys())

    def getNeighbours(self, node):
        return self.nodes[node]

    def displayNodes(self):
        for node in self.nodes:
            print(node, "->", self.nodes[node])
    
    def pruneNeighbours(self):
        twoNeighborNodes = [node for node in self.nodes if len(self.nodes[node]) == 2]
        
        for twoNode in twoNeighborNodes:
            # print(len(self.nodes))
            neighbourNodes = self.nodes[twoNode]
            beforeNode = neighbourNodes[0]
            afterNode = neighbourNodes[1]

            self.nodes[beforeNode][self.nodes[beforeNode].index(twoNode)] = afterNode
            self.nodes[afterNode][self.nodes[afterNode].index(twoNode)] = beforeNode
            self.nodes.pop(twoNode)
            self.nodeCount -= 1

            twoNeighborNodes = [node for node in self.nodes if len(self.nodes[node]) == 2]

with open("Advent-of-Code/2023/files/day23input.txt", "r") as file:
    fileLines = file.readlines()
    grid = []

    for line in fileLines:
        line = line.replace(">", ".").replace("<", ".").replace("^", ".").replace("v", ".")
        grid.append([char for char in line.strip()])

maintree = Tree()

gridHeightRange = range(len(grid))
gridWidthRange = range(len(grid[0]))

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            continue

        elif grid[i][j] == ".":
            neighbours = []

            if i-1 in gridHeightRange and grid[i - 1][j] not in "#": neighbours.append((i-1, j))
            if j+1 in gridWidthRange and grid[i][j + 1] not in "#": neighbours.append((i, j+1))
            if i+1 in gridHeightRange and grid[i + 1][j] not in "#": neighbours.append((i+1, j))
            if j-1 in gridWidthRange and grid[i][j - 1] not in "#": neighbours.append((i, j-1))

            maintree.addNode((i, j), neighbours)

print("target :", len([node for node in maintree.nodes if len(maintree.nodes[node]) != 2]))
print("current :", len(maintree.nodes))
maintree.pruneNeighbours()
print("current :", len(maintree.nodes))

startNode = (0, 1)
outputs = set()
startUnvisited = maintree.getAllNodes()

def calculatePaths(tree, unvisited, currentNode, pathLength):
    global outputs
    #print(currentNode)

    thisUnvisited = unvisited.copy()
    thisUnvisited.remove(currentNode)

    currentNodeNeighbours = tree.getNeighbours(currentNode)
    currentNodeNeighbours = [node for node in currentNodeNeighbours if node in thisUnvisited]

    # print(len(thisUnvisited), len(currentNodeNeighbours))
    if currentNode == (140, 139):
        # print(pathLength)
        outputs.add(pathLength)
        print(len(outputs))
        return
    
    # print(currentNode, "->", currentNodeNeighbours)
    for node in currentNodeNeighbours:
        calculatePaths(tree, thisUnvisited, node, pathLength + 1)

calculatePaths(maintree, startUnvisited, startNode, 0)

outputs = sorted(outputs)
print(outputs[-1])