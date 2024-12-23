with open("2024/files/day23input.txt") as file:
    fileLines = file.readlines()

pairs = [line.strip("\n").split("-") for line in fileLines]
connections = {}
for pair in pairs:
    if pair[0] not in connections.keys(): connections[pair[0]] = []
    if pair[1] not in connections.keys(): connections[pair[1]] = []

    connections[pair[0]].append(pair[1])
    connections[pair[1]].append(pair[0])

maxlen = 0
party = []
count = 1
for key in connections.keys():
    print(count, "/", len(connections.keys()))
    for i in range(2 ** len(connections[key])):
        permutation = '{0:013b}'.format(i)
        candidates = [key]

        for j in range(len(connections[key])):
            if permutation[j] == "1": candidates.append(connections[key][j])
        
        isParty = True
        for computer in candidates:
            realCandidates = candidates.copy()
            realCandidates.remove(computer)

            if not realCandidates: continue
            if not set(realCandidates).issubset(connections[computer]):
                isParty = False
                break
        
        if isParty and len(candidates) > maxlen:
            maxlen = len(candidates)
            party = sorted(candidates)
    count += 1

partyStr = ""
for comp in party: partyStr += f"{comp},"
print(partyStr[:-1])