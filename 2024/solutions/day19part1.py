with open("2024/files/day19input.txt") as file:
    fileLines = file.readlines()

towels = [value.strip() for value in fileLines[0].split(",")]
towels.sort(key = len, reverse = True)

patterns = []
for i in range(2, len(fileLines)): patterns.append(fileLines[i].strip("\n"))

todo = []
for i in range(len(patterns)): todo.append((patterns[i], i))

possibles = set()
while len(todo) > 0:
    print(len(todo), len(possibles))
    cur = todo.pop(0)
    for towel in towels:
        lentowel = len(towel)
        if cur[0] == towel:
            possibles.add(cur[1])
            todo = [value for value in todo if value[1] != cur[1]]
        elif cur[0][:lentowel] == towel:
            new = (cur[0][lentowel:], cur[1])
            if new not in todo: todo.append(new)

print(len(possibles))

# Idea shamelessly stolen from 
# https://www.reddit.com/r/adventofcode/comments/1hhqwa9/2024_day_19_memoization_sure_but_what_am_i/