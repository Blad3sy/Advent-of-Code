with open("2025/files/day7input.txt") as file:
    fileLines = file.readlines()

grid = [[char for char in line.strip()] for line in fileLines]
for i in range(len(grid[0])):
    if grid[0][i] == "S":
        startPos = (0, i)
        break

def moveLaser(pos, grid, completedPaths):
    if pos in completedPaths: return 0
    completedPaths.append(pos)
    if pos[0] == len(grid) - 1: return 1
    elif grid[pos[0] + 1][pos[1]] in [".", "|"]: 
        grid[pos[0] + 1][pos[1]] = "|"
        return moveLaser((pos[0] + 1, pos[1]), grid, completedPaths)
    elif grid[pos[0] + 1][pos[1]] == "^":
        grid[pos[0] + 1][pos[1] - 1] = "|"
        grid[pos[0] + 1][pos[1] + 1] = "|"
        return moveLaser((pos[0] + 1, pos[1] - 1), grid, completedPaths) + moveLaser((pos[0] + 1, pos[1] + 1), grid, completedPaths)

completedPaths = []
moveLaser(startPos, grid, completedPaths)

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "^" and grid[i-1][j] == "|": total += 1
        
print(total)