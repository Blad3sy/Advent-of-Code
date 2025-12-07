import functools

with open("2025/files/day7input.txt") as file:
    fileLines = file.readlines()

grid = [[char for char in line.strip()] for line in fileLines]
for i in range(len(grid[0])):
    if grid[0][i] == "S":
        startPos = (0, i)
        break

for i in range(len(grid)):
    grid[i] = tuple(grid[i])
grid = tuple(grid)

@functools.cache
def moveLaser(pos, grid):
    if pos[0] == len(grid) - 1: return 1
    elif grid[pos[0] + 1][pos[1]] in [".", "|"]: return moveLaser((pos[0] + 1, pos[1]), grid)
    elif grid[pos[0] + 1][pos[1]] == "^": return moveLaser((pos[0] + 1, pos[1] - 1), grid) + moveLaser((pos[0] + 1, pos[1] + 1), grid)

print(moveLaser(startPos, grid))