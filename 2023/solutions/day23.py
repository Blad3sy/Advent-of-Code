import sys
sys.setrecursionlimit(5000)

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
 
# https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
    def topologicalSortUtil(self, v):
        self.visited[v] = True

        for i in self.nodes[v]:
            if self.visited[i] == False:
                self.topologicalSortUtil(i)
 
        self.stack.insert(0,v)
 
    def topologicalSort(self):
        self.visited = {}
        for node in self.getAllNodes():
            self.visited[node] = False
        self.stack = []
 
        for i in self.getAllNodes():
            if self.visited[i] == False:
                self.topologicalSortUtil(i)
 
        #print(self.stack)
    
    def longestPath(self, startNode):
        dist = {}
        for node in self.getAllNodes():
            dist[node] = -10**9
 
        self.topologicalSort()
        dist[startNode] = 0

        while (len(self.stack) > 0):

            u = self.stack[0]
            del self.stack[0]

            if (dist[u] != 10**9):
                for i in self.getNeighbours(u):
                    if (dist[i] < dist[u] + 1):
                        dist[i] = dist[u] + 1
 
        print(dist[(140, 139)])

with open("Advent-of-Code-2023/2023/files/day23input.txt", "r") as file:
    fileLines = file.readlines()
    grid = []

    for line in fileLines:
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

            if i-1 in gridHeightRange and grid[i - 1][j] not in "#v": neighbours.append((i-1, j))
            if j+1 in gridWidthRange and grid[i][j + 1] not in "#<": neighbours.append((i, j+1))
            if i+1 in gridHeightRange and grid[i + 1][j] not in "#^": neighbours.append((i+1, j))
            if j-1 in gridWidthRange and grid[i][j - 1] not in "#>": neighbours.append((i, j-1))

            maintree.addNode((i, j), neighbours)

        else:
            if grid[i][j] == ">":
                maintree.addNode((i, j), [(i, j + 1)])
            elif grid[i][j] == "<":
                maintree.addNode((i, j), [(i, j - 1)])
            elif grid[i][j] == "^":
                maintree.addNode((i, j), [(i - 1, j)])
            elif grid[i][j] == "v":
                maintree.addNode((i, j), [(i + 1, j)])

# maintree.displayNodes()

startNode = (0, 1)

# track already visited nodes to make sure backtracking is impossible
# doing this allows the graph to be classified as a Directed Acylic Graph

maintree.longestPath(startNode)