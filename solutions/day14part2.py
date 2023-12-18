def north():
    global fileLines
    global rockIndices

    moved = True

    while moved:
        moved = False

        for r in range(len(rockIndices)):
            if rockIndices[r][0] - 1 >= 0:
                if fileLines[rockIndices[r][0] - 1][rockIndices[r][1]] == ".":
                    rockIndices[r][0] -= 1
                    fileLines[rockIndices[r][0]][rockIndices[r][1]] = "O"
                    fileLines[rockIndices[r][0] + 1][rockIndices[r][1]] = "."
                    moved = True

def south():
    global fileLines
    global rockIndices

    moved = True

    while moved:
        moved = False

        for r in range(len(rockIndices)):
            if rockIndices[r][0] + 1 < len(fileLines):
                if fileLines[rockIndices[r][0] + 1][rockIndices[r][1]] == ".":
                    rockIndices[r][0] += 1
                    fileLines[rockIndices[r][0]][rockIndices[r][1]] = "O"
                    fileLines[rockIndices[r][0] - 1][rockIndices[r][1]] = "."
                    moved = True

def east():
    global fileLines
    global rockIndices

    moved = True

    while moved:
        moved = False

        for r in range(len(rockIndices)):
            if rockIndices[r][1] + 1 < len(fileLines[0]):
                if fileLines[rockIndices[r][0]][rockIndices[r][1] + 1] == ".":
                    rockIndices[r][1] += 1
                    fileLines[rockIndices[r][0]][rockIndices[r][1]] = "O"
                    fileLines[rockIndices[r][0]][rockIndices[r][1] - 1] = "."
                    moved = True

def west():
    global fileLines
    global rockIndices

    moved = True

    while moved:
        moved = False

        for r in range(len(rockIndices)):
            if rockIndices[r][1] - 1 >= 0:
                if fileLines[rockIndices[r][0]][rockIndices[r][1] - 1] == ".":
                    rockIndices[r][1] -= 1
                    fileLines[rockIndices[r][0]][rockIndices[r][1]] = "O"
                    fileLines[rockIndices[r][0]][rockIndices[r][1] + 1] = "."
                    moved = True

def cycle():
    north()
    west()
    south()
    east()

with open("Advent-of-Code-2023/solutions/files/day14input.txt", "r") as file:
    fileLines = file.readlines()

    for i in range(len(fileLines)):
        intermediate = fileLines[i].strip()
        fileLines[i] = [value for value in intermediate]

rockIndices = []
for i in range(len(fileLines)):
    for t in range(len(fileLines[i])):
        if fileLines[i][t] == "O":
            rockIndices.append([i, t])

prevPositions = []
cycleNum = 1000000000
loopFound = False
i = 0
while i < cycleNum:
    cycle()

    '''for line in fileLines:
        for letter in line:
            print(letter, end = "")
        print("\n", end = "")
    print()'''

    copyArray = [value.copy() for value in fileLines]

    if not loopFound:
        if copyArray in prevPositions:
            print("LOOP FOUND")
            loopFound = True
            distanceToGoal = cycleNum - i
            loopLen = i - prevPositions.index(copyArray)
            i = cycleNum - distanceToGoal % loopLen
        
        else:
            prevPositions.append(copyArray)
    
    i += 1

total = 0
for i in range(len(fileLines)):
    for letter in fileLines[i]:
        if letter == "O":
            total += (len(fileLines) - i)

print(total)