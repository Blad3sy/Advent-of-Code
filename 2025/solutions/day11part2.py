import functools

with open("2025/files/day11input.txt") as file:
    fileLines = file.readlines()

data = [line.replace(":", "").strip().split() for line in fileLines]
connections = {}

for line in data:
    connections[line[0]] = line[1:]

@functools.cache
def followPath(device, dacVisited, fftVisited):
    if device == "out":
        if dacVisited and fftVisited: return 1
        else: return 0
    
    if device == "dac": dacVisited = True
    if device == "fft": fftVisited = True

    total = 0
    for connected in connections[device]:
        total += followPath(connected, dacVisited, fftVisited)
    
    return total

print(followPath("svr", False, False))