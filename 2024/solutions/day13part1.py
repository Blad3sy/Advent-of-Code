with open("2024/files/day13input.txt") as file:
    fileLines = file.readlines()

aPresses = []
bPresses = []
targets = []

for line in fileLines:
    if "A" in line:
        plusIndices = []
        for i in range(len(line)):
            if line[i] == "+": plusIndices.append(i)

        Ax = int(line[plusIndices[0] + 1:line.index(",")])
        Ay = int(line[plusIndices[1] + 1:].strip("\n"))

        aPresses.append((Ax, Ay))


    elif "B" in line:
        plusIndices = []
        for i in range(len(line)):
            if line[i] == "+": plusIndices.append(i)

        Bx = int(line[plusIndices[0] + 1:line.index(",")])
        By = int(line[plusIndices[1] + 1:].strip("\n"))

        bPresses.append((Bx, By))
    
    elif "z" in line:
        equalsIndices = []
        for i in range(len(line)):
            if line[i] == "=": equalsIndices.append(i)

        x = int(line[equalsIndices[0] + 1:line.index(",")])
        y = int(line[equalsIndices[1] + 1:].strip("\n"))

        targets.append((x, y))

total = 0
for i in range(len(aPresses)):
    eq1 = (aPresses[i][0], bPresses[i][0])
    eq2 = (aPresses[i][1], bPresses[i][1])
    results = targets[i]

    # Solving simultaneous equations via matrix multiplication
    determinant = eq1[0]*eq2[1] - eq1[1]*eq2[0]

    a = (eq2[1]*results[0] - eq1[1]*results[1]) / determinant
    b = (eq1[0]*results[1] - eq2[0]*results[0]) / determinant

    if a.is_integer() and b.is_integer():
        total += int(a) * 3
        total += int(b)

print(total)