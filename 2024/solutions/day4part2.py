with open("2024/files/day4input.txt") as file:
    fileLines = file.readlines()

grid = []
for line in fileLines:
    grid.append(list(line.strip("\n")))

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "A":
            if (i - 1 > -1 and i + 1 < len(grid) and
                j - 1 > -1 and j + 1 < len(grid[i])):

                subcount = 0

                if grid[i - 1][j - 1] == "M": 
                    if grid[i + 1][j + 1] == "S": subcount += 1

                elif grid[i - 1][j - 1] == "S": 
                    if grid[i + 1][j + 1] == "M": subcount += 1
                
                if grid[i + 1][j - 1] == "M": 
                    if grid[i - 1][j + 1] == "S": subcount += 1

                elif grid[i + 1][j - 1] == "S": 
                    if grid[i - 1][j + 1] == "M": subcount += 1

                if subcount == 2: count += 1

print(count)