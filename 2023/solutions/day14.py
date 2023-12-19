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

total = 0
for i in range(len(fileLines)):
    for letter in fileLines[i]:
        if letter == "O":
            total += (len(fileLines) - i)

print(total)