import matplotlib.path
import matplotlib.pyplot as plt

def GetPossibleDirections(pipe):
    match pipe:
        case "|": return ["N", "S"]
        case "-": return ["E", "W"]
        case "L": return ["N", "E"]
        case "J": return ["N", "W"]
        case "7": return ["S", "W"]
        case "F": return ["S", "E"] 
        case _: return None
    
def GetOpposite(direction):
    match direction:
        case "N": return "S"
        case "E": return "W"
        case "S": return "N"
        case "W": return "E"

with open("Advent-of-Code-2023/solutions/files/day10input.txt", "r") as file:
    fileLines = file.readlines()

startingIndex = ()

for i in range(len(fileLines)):
    if "S" in fileLines[i]:
        for t in range(len(fileLines[i])):
            if fileLines[i][t] == "S":
                startingIndex = (i, t)
                break
        break

currentIndex = list(startingIndex)
currentDirection = "E"
indexArray = []
vertexArray = []

while True:
    if fileLines[currentIndex[0]][currentIndex[1]] in ["S", "L", "J", "7", "F"]:
        vertexArray.append([currentIndex[0], currentIndex[1]])
    
    indexArray.append([currentIndex[0], currentIndex[1]])
    
    match currentDirection[0]:
        case "N": currentIndex[0] -= 1
        case "E": currentIndex[1] += 1
        case "S": currentIndex[0] += 1
        case "W": currentIndex[1] -= 1
    
    if tuple(currentIndex) == startingIndex:
        break

    possibleDirections = GetPossibleDirections(fileLines[currentIndex[0]][currentIndex[1]])
    possibleDirections = [value for value in possibleDirections if value != GetOpposite(currentDirection)]
    currentDirection = possibleDirections[0]

total = 0
polygon = matplotlib.path.Path(vertexArray)

for i in range(len(fileLines)):
    for t in range(len(fileLines[i])):
        if polygon.contains_point([i, t]) and not [i, t] in indexArray:
            total += 1

print(total)


xs, ys = zip(*vertexArray) #create lists of x and y values

plt.figure()
plt.plot(xs,ys) 
plt.show()