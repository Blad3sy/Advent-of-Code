with open("2025/files/day6input.txt") as file:
    fileLines = file.readlines()

problems = [line.strip("\n").split() for line in fileLines]
total = 0

currentVal = 0
for i in range(len(problems[0])):
    mode = problems[len(problems) - 1][i]
    currentVal = int(problems[0][i])

    for j in range(1, len(problems) - 1):
        if mode == "*": currentVal *= int(problems[j][i])
        else: currentVal += int(problems[j][i])
    
    total += currentVal

print(total)