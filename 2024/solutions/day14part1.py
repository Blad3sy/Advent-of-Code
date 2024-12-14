with open("2024/files/day14input.txt") as file:
    fileLines = file.readlines()

HEIGHT = 103
WIDTH = 101
TIME = 100

robots = []
for line in fileLines:
    line = line.strip("\n")
    equalsIndices = []
    for i in range(len(line)): 
        if line[i] == "=": equalsIndices.append(i)
    
    pos = line[equalsIndices[0] + 1:line.index(" ")].split(",")
    vel = line[equalsIndices[1] + 1:].split(",")

    robots.append([pos, vel])

positions = []
for i in range(len(robots)):
    posx, posy = int(robots[i][0][0]), int(robots[i][0][1])
    velx, vely = int(robots[i][1][0]), int(robots[i][1][1])

    posx += velx * TIME
    posx %= WIDTH

    posy += vely * TIME
    posy %= HEIGHT

    positions.append((posx, posy))

quadrants = [0, 0, 0, 0]
XCENTRAL = int((WIDTH - 1) / 2)
YCENTRAL = int((HEIGHT - 1) / 2)

for position in positions:
    if position[0] < XCENTRAL and position[1] < YCENTRAL: quadrants[0] += 1
    elif position[0] > XCENTRAL and position[1] < YCENTRAL: quadrants[1] += 1
    elif position[0] < XCENTRAL and position[1] > YCENTRAL: quadrants[2] += 1
    elif position[0] > XCENTRAL and position[1] > YCENTRAL: quadrants[3] += 1

print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])