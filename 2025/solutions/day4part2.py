with open("2025/files/day4input.txt") as file:
    fileLines = file.readlines()

grid = [[char for char in line.strip("\n")] for line in fileLines]
dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
total = 0

def nextRemoval():
    global grid
    removed = 0

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == ".": continue
            adjacent = 0

            for dir in dirs:
                if ((i + dir[0]) in range(len(grid)) and
                (j + dir[1]) in range(len(grid)) and
                grid[(i + dir[0])][(j + dir[1])] in ["@", "x"]):
                    adjacent += 1
        
            if adjacent < 4:
                grid[i][j] = "x"
                removed += 1
    
    return removed

while True:
    thisRemoved = nextRemoval()
    if thisRemoved == 0: break
    
    total += thisRemoved
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "x": grid[i][j] = "."

print(total)