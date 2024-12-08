with open("2024/files/day8input.txt") as file:
    fileLines = file.readlines()

antennaMap = [list(line.strip("\n")) for line in fileLines]

antennaLog = {}
for i in range(len(antennaMap)):
    for j in range(len(antennaMap[i])):
        if antennaMap[i][j] != ".":
            if antennaMap[i][j] not in antennaLog.keys():
                antennaLog[antennaMap[i][j]] = []
            antennaLog[antennaMap[i][j]].append([i, j])

antinodes = set()
for key in antennaLog.keys():
    for pos1 in antennaLog[key]:
        for pos2 in antennaLog[key]:
            if pos1 != pos2:
                pos1differenceVector = [2 * (pos2[0] - pos1[0]), 2 * (pos2[1] - pos1[1])]
                pos2differenceVector = [2 * (pos1[0] - pos2[0]), 2 * (pos1[1] - pos2[1])]

                antinodes.add((pos1[0] + pos1differenceVector[0], pos1[1] + pos1differenceVector[1]))
                antinodes.add((pos2[0] + pos2differenceVector[0], pos2[1] + pos2differenceVector[1]))

count = 0
for antinode in antinodes:
    if antinode[0] >= 0 and antinode[0] < len(antennaMap) and antinode[1] >= 0 and antinode[1] < len(antennaMap[0]):
        count += 1

print(count)