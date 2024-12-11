import functools

@functools.cache
def transformStone(stone: int) -> tuple:
    if stone == 0: return (1, None)
    elif len(str(stone)) % 2 == 0:
        strStone = str(stone)
        mid = len(strStone) // 2
        return (int(strStone[:mid]), int(strStone[mid:]))
    else: return (stone * 2024, None)

@functools.cache
def countStoneBlinks(stone, depth):
    leftStone, rightStone = transformStone(stone)

    if depth == 1:
        if rightStone == None: return 1
        return 2

    output = countStoneBlinks(leftStone, depth - 1)
    if rightStone != None: output += countStoneBlinks(rightStone, depth - 1)
    
    return output

with open("2024/files/day11input.txt") as file:
    fileLine = file.readline()
stones = [int(value) for value in fileLine.strip("\n").split(" ")]

sum = 0
for stone in stones: sum += countStoneBlinks(stone, 75)
print(sum)

# Completed with help of this tutorial
# https://www.reddit.com/r/adventofcode/comments/1hbnyx1/2024_day_11python_mega_tutorial/
# Happy to have made it this far with no help!! 

# I will say that I came up with the idea of memoization myself however I did not think
# of implementing this so abstractly - I was stuck using a list, or keeping track of 
# numbers of stones, trying to save memory, that I didn't think of this really elegant
# way of never even dealing with the actual stone numbers, just recursively counting 
# the NUMBER of stones. Becuase of this I'm claiming everything but lines 13-23 as my 
# original idea (basically part 1 -_-), so i don't think I did too badly!

# TLDR: I need to think more abstractly, and remember recursion as a useful tool.