import functools

with open("2024/files/day19input.txt") as file:
    fileLines = file.readlines()

towels = [value.strip() for value in fileLines[0].split(",")]

patterns = []
for i in range(2, len(fileLines)): patterns.append(fileLines[i].strip("\n"))
maxlen = len(max(patterns, key = len))

methods = {}
for pattern in patterns: methods[pattern] = 0

@functools.cache
def checkPattern(cpattern):
    total = 0
    for towel in towels:
        lentowel = len(towel)
        if cpattern == towel: total += 1
        elif cpattern[:lentowel] == towel:
            total += checkPattern(cpattern[lentowel:])
    return total

total = 0
for pattern in patterns:
    total += checkPattern(pattern)
print(total)