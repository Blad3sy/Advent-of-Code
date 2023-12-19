import functools

@functools.cache
def calc(record, groups):
    if not groups:
        if "#" not in record:
            return 1
        else:
            return 0

    if not record:
        return 0

    next_character = record[0]
    next_group = groups[0]

    def hash():
        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")

        if this_group != next_group * "#":
            return 0

        if len(record) == next_group:
            if len(groups) == 1:
                return 1
            else:
                return 0

        if record[next_group] in "?.":
            return calc(record[next_group+1:], groups[1:])
        
        return 0

    def dot():
        return calc(record[1:], groups)

    if next_character == '#':
        out = hash()

    elif next_character == '.':
        out = dot()

    elif next_character == '?':
        out = dot() + hash()

    else:
        raise RuntimeError
    
    return out

with open("Advent-of-Code-2023/solutions/files/day12input.txt", "r") as file:
    fileLines = file.readlines()

springStrings = []
numLists = []

for i in range(len(fileLines)):
    spaceIndex = fileLines[i].index(" ")

    nums = (fileLines[i][spaceIndex:].strip() + ",") * 5
    nums = nums[:-1].split(",")
    nums = [int(value) for value in nums]

    springs = (fileLines[i][:spaceIndex] + "?") * 5
    springs = springs[:-1]

    numLists.append(tuple(nums))
    springStrings.append(springs)

total = 0
for i in range(len(springStrings)):
    total += calc(springStrings[i], numLists[i])

print(total)

# Solution inspired by (and partially copied from)
# https://www.reddit.com/r/adventofcode/comments/18hbbxe/2023_day_12python_stepbystep_tutorial_with_bonus/ 