with open("2024/files/day23input.txt") as file:
    fileLines = file.readlines()

pairs = [line.strip("\n").split("-") for line in fileLines]
connections = {}
for pair in pairs:
    if pair[0] not in connections.keys(): connections[pair[0]] = []
    if pair[1] not in connections.keys(): connections[pair[1]] = []

    connections[pair[0]].append(pair[1])
    connections[pair[1]].append(pair[0])

trios = set()
for key in connections.keys():
    connectors = connections[key]
    for i in range(len(connectors)):
        for j in range(len(connectors)):
            if i == j: continue
            tr1 = key
            tr2 = connectors[i]
            tr3 = connectors[j]

            if (tr1 in connections[tr2] and
                tr1 in connections[tr3] and
                tr2 in connections[tr3] and
                tr3 in connections[tr2]):
            
                trio = tuple(sorted((tr1, tr2, tr3)))
                trios.add(trio)

total = 0
for trio in trios:
    triostr = "".join(trio)
    triostr = triostr[0] + triostr[2] + triostr[4]
    if "t" in triostr: total += 1
print(total)