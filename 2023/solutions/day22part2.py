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
    
    print(totalFalls, " / ", len(fileLines))

bricksSupporting = {}
bricksSupportedBy = {}
for i in range(len(brickArray)):
    bricksSupporting[i] = []
    bricksSupportedBy[i] = []


for i in range(len(brickArray)):
    brick = brickArray[i]
    bricksBelow = [value for value in brickArray if value[1][2] == brick[0][2] - 1]
    bricksBelow = [brickArray.index(value) for value in bricksBelow
                    if set(range(value[0][0], value[1][0] + 1)).intersection(set(range(brick[0][0], brick[1][0] + 1))) and
                    set(range(value[0][1], value[1][1] + 1)).intersection(set(range(brick[0][1], brick[1][1] + 1))) ]

    for brick2 in bricksBelow:
        bricksSupporting[brick2].append(i)
    
    for brick2 in bricksBelow:
        bricksSupportedBy[i].append(brick2)

'''for brick in bricksSupporting:
    print(brick, "->", bricksSupporting[brick])'''

# Part 2 Stuff starts here
    
ids = []
disintegrated = []

def getChainReaction(id):
    global ids
    global disintegrated

    disintegrated.append(id)

    for brick in bricksSupporting[id]:
        if all(brick2 in disintegrated for brick2 in bricksSupportedBy[brick]):
            ids.append(brick)
            getChainReaction(brick)

cannotBeDis = []
for brick in bricksSupportedBy:
    if len(bricksSupportedBy[brick]) == 1:
        cannotBeDis.append(bricksSupportedBy[brick][0])
cannotBeDis = sorted(list(set(cannotBeDis)))

total = 0
counter = 1
print()
for brick in cannotBeDis:
    print(counter, " / ", len(cannotBeDis))
    counter += 1
    ids = []
    disintegrated = []
    getChainReaction(brick)
    total += len(set(ids))

print(total)