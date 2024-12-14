with open("2024/files/day14input.txt") as file:
    fileLines = file.readlines()

HEIGHT = 103
WIDTH = 101
XCENTRAL = int((WIDTH - 1) / 2)
YCENTRAL = int((HEIGHT - 1) / 2)

time = 0

robots = []
for line in fileLines:
    line = line.strip("\n")
    equalsIndices = []
    for i in range(len(line)): 
        if line[i] == "=": equalsIndices.append(i)
    
    pos = line[equalsIndices[0] + 1:line.index(" ")].split(",")
    vel = line[equalsIndices[1] + 1:].split(",")

    robots.append([pos, vel])

while True:
    time += 1
    print(time)
    positions = []
    for i in range(len(robots)):
        posx, posy = int(robots[i][0][0]), int(robots[i][0][1])
        velx, vely = int(robots[i][1][0]), int(robots[i][1][1])

        posx += velx * time
        posx %= WIDTH

        posy += vely * time
        posy %= HEIGHT

        positions.append((posx, posy))

    quadrants = [0, 0, 0, 0]

    for position in positions:
        if position[0] < XCENTRAL and position[1] < YCENTRAL: quadrants[0] += 1
        elif position[0] > XCENTRAL and position[1] < YCENTRAL: quadrants[1] += 1
        elif position[0] < XCENTRAL and position[1] > YCENTRAL: quadrants[2] += 1
        elif position[0] > XCENTRAL and position[1] > YCENTRAL: quadrants[3] += 1

    for i in range(len(quadrants)):
        printTrue = True
        for j in range(len(quadrants)):
            if i != j:
                if quadrants[i] < quadrants[j] * 2: printTrue = False # Hueristic as below

        if printTrue:
            for a in range(HEIGHT):
                for b in range(WIDTH):
                    if (b, a) in positions: print("#", end = "")
                    else: print(".", end = "")
                print()
            
            input()
    

    # Completed with use of this
    # https://www.reddit.com/r/adventofcode/comments/1he0g67/2024_day_14_part_2_the_clue_was_in_part_1/
    # and manually checking with the above print function.

    # This part 2 was stupid. I will not defend it.