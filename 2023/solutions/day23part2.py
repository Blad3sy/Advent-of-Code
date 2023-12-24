import sys
sys.setrecursionlimit(3000)

class Tree():
    def __init__(self):
        # node : neighbours
        self.nodes = {}
        self.nodeCount = 0
    
    def addNode(self, node, neighbours):
        self.nodes[node] = neighbours
        self.nodeCount += 1
    
    def getAllNodes(self):
        return list(self.nodes.keys())

    def getNeighbours(self, node):
        return list(self.nodes[node].keys())

    def displayNodes(self):
        for node in self.nodes:
            print(node, "->", self.nodes[node])
    
    def pruneNeighbours(self):
        twoNeighborNodes = [node for node in self.nodes if len(self.nodes[node]) == 2]
        
        for twoNode in twoNeighborNodes:
            # print(len(self.nodes))
            neighbourNodes = self.nodes[twoNode]
            neighbourNodeKeys = self.getNeighbours(twoNode)

            beforeNode = neighbourNodeKeys[0]
            beforeNodeWeight = neighbourNodes[neighbourNodeKeys[0]]

            afterNode = neighbourNodeKeys[1]
            afterNodeWeight = neighbourNodes[neighbourNodeKeys[1]]

            #self.nodes[beforeNode][self.nodes[beforeNode].index(twoNode)] = afterNode
            #self.nodes[afterNode][self.nodes[afterNode].index(twoNode)] = beforeNode

            self.nodes[beforeNode].pop(twoNode)
            self.nodes[beforeNode][afterNode] = beforeNodeWeight + afterNodeWeight

            self.nodes[afterNode].pop(twoNode)
            self.nodes[afterNode][beforeNode] = afterNodeWeight + beforeNodeWeight

            self.nodes.pop(twoNode)
            self.nodeCount -= 1

            twoNeighborNodes = [node for node in self.nodes if len(self.nodes[node]) == 2]

with open("Advent-of-Code-2023/2023/files/day23input.txt", "r") as file:
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
            neighbours = {}

            if i-1 in gridHeightRange and grid[i - 1][j] not in "#": neighbours[(i-1, j)] = 1
            if j+1 in gridWidthRange and grid[i][j + 1] not in "#": neighbours[(i, j+1)] = 1
            if i+1 in gridHeightRange and grid[i + 1][j] not in "#": neighbours[(i+1, j)] = 1
            if j-1 in gridWidthRange and grid[i][j - 1] not in "#": neighbours[(i, j-1)] = 1

            maintree.addNode((i, j), neighbours)

print("target :", len([node for node in maintree.nodes if len(maintree.nodes[node]) != 2]))
print("current :", len(maintree.nodes))
maintree.pruneNeighbours()
print("current :", len(maintree.nodes))

startNode = (0, 1)
outputs = set()
startVisited = set()

def dfs(visited, graph, node, pathLength):
    thisVisited = visited.copy()

    if node not in thisVisited:
        thisVisited.add(node)

        if node == (140, 139):
            if len(outputs) > 0 and pathLength > max(outputs): print(pathLength)
            outputs.add(pathLength)

        for neighbour in graph.getNeighbours(node):
            dfs(thisVisited, graph, neighbour, pathLength + graph.nodes[node][neighbour])

dfs(startVisited, maintree, startNode, 0)
print(">>>>", max(outputs), "<<<<")