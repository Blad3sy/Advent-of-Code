with open("Advent-of-Code-2023/2023/files/day22input.txt", "r") as file:
    fileLines = file.readlines()

brickArray = []
for i in range(len(fileLines)):
    line = fileLines[i]
    line = line.strip().split("~")
    line[0] = [int(value) for value in line[0].split(",")]
    line[1] = [int(value) for value in line[1].split(",")]
    brickArray.append(line)

brickArray = sorted(brickArray, key = lambda x: x[0][2])

change = True
while change:
    change = False
    totalFalls = 0

    for i in range(len(brickArray)):
        brick = brickArray[i]
        bricksBelow = [value for value in brickArray if value[1][2] == brick[0][2] - 1]
        bricksBelow = [brickArray.index(value) for value in bricksBelow
                      if set(range(value[0][0], value[1][0] + 1)).intersection(set(range(brick[0][0], brick[1][0] + 1))) and
                      set(range(value[0][1], value[1][1] + 1)).intersection(set(range(brick[0][1], brick[1][1] + 1))) ]

        if not bricksBelow and brick[0][2] != 1:
            brick[0][2] -= 1
            brick[1][2] -= 1
            change = True

            totalFalls += 1
    
    print(totalFalls)

bricksSupportedBy = {}
canBeDis = []
for i in range(len(brickArray)):
    bricksSupportedBy[i] = []
    canBeDis.append(i)

for i in range(len(brickArray)):
    brick = brickArray[i]
    bricksBelow = [value for value in brickArray if value[1][2] == brick[0][2] - 1]
    bricksBelow = [brickArray.index(value) for value in bricksBelow
                    if set(range(value[0][0], value[1][0] + 1)).intersection(set(range(brick[0][0], brick[1][0] + 1))) and
                    set(range(value[0][1], value[1][1] + 1)).intersection(set(range(brick[0][1], brick[1][1] + 1))) ]

    for brick2 in bricksBelow:
        bricksSupportedBy[i].append(brick2)

for brick in bricksSupportedBy:
    if len(bricksSupportedBy[brick]) == 1:
        try: canBeDis.remove(bricksSupportedBy[brick][0])
        except ValueError: pass

print(len(canBeDis))