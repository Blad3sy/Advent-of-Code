import functools

with open("2024/files/day21input.txt") as file:
    fileLines = file.readlines()

codes = [line.strip("\n") for line in fileLines]

gap = "."
numpad = (
    "789",
    "456",
    "123",
    ".0A"
)

dirpad = (
    ".^A",
    "<v>"
)

def getPos(value, pad):
    for i in range(len(pad)):
        for j in range(len(pad[i])):
            if pad[i][j] == value: return i, j

def getMoves(start, end, pad):
    sy, sx = getPos(start, pad)
    ey, ex = getPos(end, pad)
    gapy, gapx = getPos(".", pad)

    dy, dx = ey - sy, ex - sx

    if dy >= 0: yMoves = "v" * abs(dy)
    else: yMoves = "^" * abs(dy)

    if dx >= 0: xMoves = ">" * abs(dx)
    else: xMoves = "<" * abs(dx)

    if dy == dx == 0: return [""]
    elif dy == 0: return [xMoves]
    elif dx == 0: return [yMoves]
    # If corner is that of the gap, only one path will be valid
    elif (sy, ex) == (gapy, gapx): return [yMoves + xMoves]
    elif (ey, sx) == (gapy, gapx): return [xMoves + yMoves]
    else: return [xMoves + yMoves, yMoves + xMoves]

def getPaths(code, pad):
    code = "A" + code
    results = []

    # Get possible paths
    for i in range(len(code) - 1):
        results += [[move + "A" for move in getMoves(code[i], code[i+1], pad)]]
    
    return results

@functools.cache
def recurse(code, depth):
    if depth == 1: return len(code)
    
    pad = None
    for char in "0123456789": 
        if char in code: 
            pad = numpad
            break
    if not pad: pad = dirpad

    total = 0
    for paths in getPaths(code, pad):
        total += min(recurse(path, depth - 1) for path in paths)
    return total  
  
sum = 0
for code in codes:
    sum += recurse(code, 27) * int(code[:3])
print(sum)