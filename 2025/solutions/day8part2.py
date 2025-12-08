with open("2025/files/day8input.txt") as file:
    fileLines = file.readlines()

coords = [tuple([int(coord) for coord in line.strip().split(",")]) for line in fileLines]
distances = {}

for i in range(len(coords)):
    for j in range(len(coords)):
        if i == j or (i, j) in distances.keys() or (j, i) in distances.keys(): continue
        xdist = (coords[i][0] - coords[j][0]) ** 2
        ydist = (coords[i][1] - coords[j][1]) ** 2
        zdist = (coords[i][2] - coords[j][2]) ** 2

        truedistsq = xdist + ydist + zdist
        distances[(i, j)] = truedistsq

distances = sorted(distances.items(), key=lambda item: item[1])
groups = [[i] for i in range(len(coords))]

index = 0
while len(groups) > 1:
    firstBox = distances[index][0][0]
    secondBox = distances[index][0][1]

    index += 1

    for j in range(len(groups)):
        if firstBox in groups[j]: firstBoxGroup = groups[j]
        if secondBox in groups[j]: secondBoxGroup = groups[j]
    
    if firstBoxGroup == secondBoxGroup: continue

    newGroup = [*firstBoxGroup, *secondBoxGroup]
    groups.remove(firstBoxGroup)
    groups.remove(secondBoxGroup)

    groups.append(newGroup)

print(coords[distances[index - 1][0][0]][0] * coords[distances[index - 1][0][1]][0])