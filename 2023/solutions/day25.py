import networkx as nx

'''class Graph():
    def __init__(self):
        self.nodes = {}
    
    def addNode(self, node):
        self.nodes[node] = []
    
    def addConnection(self, node1, node2):
        self.nodes[node1].append(node2)
        self.nodes[node2].append(node1)
    
    def getAllNodes(self):
        return list(self.nodes.keys()) 
    
    def getNodeConnections(self, node):
        return self.nodes[node]

    def displayNodes(self):
        for node in self.nodes:
            print(node, "->", self.nodes[node])'''
    
with open("Advent-of-Code/2023/files/day25input.txt", "r") as file:
    fileLines = file.readlines()

maingraph = nx.Graph()

for line in fileLines:
    thisID = line.strip().split(":")[0]
    connections = line.strip().split(":")[1].strip().split()

    for connection in connections:
        maingraph.add_edge(thisID, connection, capacity = 100)

outputs = nx.minimum_cut(maingraph, "hgg", "jlx")
print(len(outputs[1][0]) * len(outputs[1][1]))

# its a little cheaty, I don't care! I had to figure out how to use this library and it was not easy.
# I read many articles.

# If it was a normal day I probably would've written my own 
# max-flow min-cut algorithm but because it's christmas day 
# and i'm busy seeing family, I'm satisfied with this slightly
# cheaty solution. Who knows, maybe I'll write that algorithm in
# the next few days!! Again, this AOC was wonderful and fun!!