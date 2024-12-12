def findConnections(grid, region, coords, visited):
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    area = set()
    area.add(coords)

    perim = set()
    
    if coords in visited: return perim, area
    visited.add(coords)

    for dir in dirs:
        newCoords = (coords[0] + dir[0], coords[1] + dir[1])
        
        if newCoords[0] in range(len(grid)) and newCoords[1] in range(len(grid[coords[0]])):
            if grid[newCoords[0]][newCoords[1]] != region:
                perim.add((coords, dirConvert(dir)))
            else:
                if newCoords not in visited:
                    p1, a1 = findConnections(grid, region, newCoords, visited)
                    perim = perim.union(p1)
                    area = area.union(a1)
        else:
            perim.add((coords, dirConvert(dir)))
    
    return perim, area

def dirConvert(dir):
    match dir:
        case [1, 0]: return "D"
        case [-1, 0]: return "U"
        case [0, 1]: return "R"
        case [0, -1]: return "L"

with open("2024/files/day12input.txt") as file:
    fileLines = file.readlines()

grid = [list(line.strip("\n")) for line in fileLines]
regionList = []

for i in range(len(grid)):
    print(i+1, "/", len(grid))
    for j in range(len(grid[i])):
       region = grid[i][j]

       regionPerim, regionArea = findConnections(grid, region, (i, j), set())

       if (region, regionPerim, regionArea) not in regionList:
           regionList.append((region, regionPerim, regionArea))

sum = 0
for val in regionList:
    sum += len(val[1]) * len(val[2])
print(sum)