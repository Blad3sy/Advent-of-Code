def normalise(val):
    while True: 
        if 0 <= val and val < 100: return val

        if val < 0: val += 100
        elif val >= 100: val -= 100


with open("2025/files/day1input.txt") as file:
    fileLines = file.readlines()

turns = [line.strip("\n") for line in fileLines]
val = 50
totalZeroes = 0

for turn in turns:
    if turn[0] == "R": val += int(turn[1:])
    elif turn[0] == "L": val -= int(turn[1:])

    val = normalise(val)
    if val == 0: totalZeroes += 1

print(totalZeroes)