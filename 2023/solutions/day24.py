def calculateGradient(x1, x2, y1, y2):
    return  (y2 - y1) / (x2 - x1)

def calculateYIntercept(x, y, m):
    return y - (m * x)

def calculateX(c1, c2, m1, m2):
    try: x = (c2 - c1) / (m1 - m2)
    except ZeroDivisionError: return None

    return x

def calculateY(m, x, c):
    if x == None:
        return None
    return (m * x) + c

def calculateXY(eq1, eq2):
    x = calculateX(eq1[1], eq2[1], eq1[0], eq2[0])
    y = calculateY(eq1[0], x, eq1[1])

    return x, y

with open("Advent-of-Code-2023/2023/files\day24input.txt", "r") as file:
    fileLines = file.readlines()

posray = []
velray = []

for line in fileLines:
    line = line.strip().split("@")
    line[0] = line[0].strip().split(",")
    line[1] = line[1].strip().split(",")

    line[0] = [int(value) for value in line[0]]
    line[1] = [int(value) for value in line[1]]

    posray.append(line[0])
    velray.append(line[1])

# m, c
eqArray = []
for i in range(len(posray)):
    # print(posray[i], "->", velray[i])
    gradient = calculateGradient(posray[i][0], posray[i][0] + velray[i][0], posray[i][1], posray[i][1] + velray[i][1])
    yIntercept = calculateYIntercept(posray[i][0], posray[i][1], gradient)
    # print(f"y = {gradient}x + {yIntercept}")
    eqArray.append([gradient, yIntercept])

total = 0
for i in range(len(eqArray)):
    # print(i + 1, " / ", len(fileLines))
    for j in range(len(eqArray)):
        if i != j:
            x, y = calculateXY(eqArray[i], eqArray[j])
            if x == None or y == None:
                continue
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                iX = posray[i][0]
                iV = velray[i][0]

                jX = posray[j][0]
                jV = velray[j][0]

                if iV > 0:
                    if iX > x:
                        continue
                else:
                    if iX < x:
                        continue

                if jV > 0:
                    if jX > x:
                        continue
                else:
                    if jX < x:
                        continue
                
                total += 1

# Account for duplicates - both (X, Y) and (Y, X) will be valid here
print(total / 2)