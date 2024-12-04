with open("2024/files/day4input.txt") as file:
    fileLines = file.readlines()

grid = []
for line in fileLines:
    grid.append(list(line.strip("\n")))

directions = []
for k in range(-1, 2):
    for m in range(-1, 2):
        directions.append([k, m])
directions.remove([0, 0])

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "X":
            for dir in directions:
                if (i + dir[0] > -1 and i + dir[0] < len(grid) and
                j + dir[1] > -1 and j + dir[1] < len(grid[i]) and
                grid[i + dir[0]][j + dir[1]] == "M"):
                    if (i + dir[0] * 2 > -1 and i + dir[0] * 2 < len(grid) and
                    j + dir[1] * 2 > -1 and j + dir[1] * 2 < len(grid[i]) and
                    grid[i + dir[0] * 2][j + dir[1] * 2] == "A"):
                        if (i + dir[0] * 3 > -1 and i + dir[0] * 3 < len(grid) and
                        j + dir[1] * 3 > -1 and j + dir[1] * 3 < len(grid[i]) and
                        grid[i + dir[0] * 3][j + dir[1] * 3] == "S"): count += 1

print(count)