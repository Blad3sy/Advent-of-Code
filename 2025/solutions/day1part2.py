with open("2025/files/day1input.txt") as file:
    fileLines = file.readlines()

turns = [line.strip("\n") for line in fileLines]
val = 50
totalZeroes = 0

for turn in turns:
    if turn[0] == "R": modifier = 1
    elif turn[0] == "L": modifier = -1

    change = int(turn[1:])
    
    for i in range(change):
        val += modifier
        if val < 0: val += 100
        elif val >= 100: val -= 100

        if val == 0: 
            totalZeroes += 1

print(totalZeroes)