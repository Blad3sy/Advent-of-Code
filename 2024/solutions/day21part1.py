from sys import setrecursionlimit
setrecursionlimit(10000)

with open("2024/files/day21input.txt") as file:
    fileLines = file.readlines()

codes = [line.strip("\n") for line in fileLines]

numNodes = {
    "A": [["0", "<"], ["3", "^"]],
    "0": [["A", ">"], ["2", "^"]],
    "1": [["2", ">"], ["4", "^"]],
    "2": [["0", "v"], ["1", "<"], ["3", ">"], ["5", "^"]],
    "3": [["A", "v"], ["2", "<"], ["6", "^"]],
    "4": [["1", "v"], ["5", ">"], ["7", "^"]],
    "5": [["2", "v"], ["4", "<"], ["6", ">"], ["8", "^"]],
    "6": [["3", "v"], ["5", "<"], ["9", "^"]],
    "7": [["4", "v"], ["8", ">"]],
    "8": [["5", "v"], ["7", "<"], ["9", ">"]],
    "9": [["6", "v"], ["8", "<"]],
}

dirNodes = {
    "A": [["^", "<"], [">", "v"]],
    "^": [["v", "v"], ["A", ">"]],
    ">": [["v", "<"], ["A", "^"]],
    "v": [["<", "<"], ["^", "^"], [">", ">"]],
    "<": [["v", ">"]]
}

distances = {}
paths = {}
inf = 10000000000000000000
unvisited = []

def djikstrasSetup(nodes, start):
    global distances
    global inf
    global unvisited
    global paths

    distances = {}
    paths = {}
    unvisited = list(nodes.keys())
    for node in unvisited: 
        distances[node] = inf
        paths[node] = [[]]
    
    distances[start] = 0

def djikstras(nodes, node):
    for edge in nodes[node]:
        if edge[0] in unvisited:
            newDist = distances[node] + 1

            newPaths = []
            for path in paths[node]:
                newPath = path.copy()
                newPath.append(edge[1])
                newPaths.append(newPath)

            if newDist < distances[edge[0]]:
                distances[edge[0]] = newDist
                paths[edge[0]] = newPaths
            
            elif newDist == distances[edge[0]]:
                for path in newPaths:
                    paths[edge[0]].append(path)
    
    unvisited.remove(node)

    min = None
    for nextNode in unvisited:
        if not min: min = nextNode
        elif distances[nextNode] < distances[min]:
            min = nextNode

    if min: djikstras(nodes, min)

def getPath(start, end, nodes):
    djikstrasSetup(nodes, start)
    djikstras(nodes, start)

    return paths[end]

def getStr(code, nodes):
    codeStrs = []
    for i in range(len(code)):
        letter = code[i]
        if i > 0: prevLetter = code[i - 1]
        else: prevLetter = "A"

        curPaths = getPath(prevLetter, letter, nodes)
        for path in curPaths:
            codeStr = [i, "".join(path) + "A"]
            codeStrs.append(codeStr)

    subs = []
    for i in range(len(code)):
        subs.append([code[1] for code in codeStrs if code[0] == i])

    finals = subs[0]

    next = []
    for i in range(1, len(subs)):
        sub = subs[i]
        for code in sub:
            for final in finals:
                next.append(final + code)
        finals = next.copy()
        next = []

    #finals = [final for final in finals if len(final) == len(min(finals, key = len))]
    return finals

firstOrder = []
for code in codes: firstOrder.append(getStr(code, numNodes))
for i in range(len(codes)): print(codes[i], ":", firstOrder[i])
print()

secondOrder = []
for codes1 in firstOrder:
    temp = []
    for code1 in codes1: temp.append(getStr(code1, dirNodes))
    secondOrder.append(temp)

for i in range(len(secondOrder)):
    secondOrder[i] = [j for sub in secondOrder[i] for j in sub]
    secondOrder[i] = [code for code in secondOrder[i] if len(code) == len(min(secondOrder[i], key = len))]

for i in range(len(codes)): print(codes[i], ":", secondOrder[i])
print()

thirdOrder = []
for codes1 in secondOrder:
    temp = []
    for code1 in codes1: 
        print(codes1.index(code1) + 1, "/", len(codes1), ":", code1)
        temp.append(getStr(code1, dirNodes))
    thirdOrder.append(temp)

total = 0
for i in range(len(thirdOrder)):
    thirdOrder[i] = [j for sub in thirdOrder[i] for j in sub]
    total += int(codes[i][:3]) * len(min(thirdOrder[i], key = len))
print(total)