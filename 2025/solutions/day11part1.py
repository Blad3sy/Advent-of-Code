with open("2025/files/day11input.txt") as file:
    fileLines = file.readlines()

data = [line.replace(":", "").strip().split() for line in fileLines]
connections = {}

for line in data:
    connections[line[0]] = line[1:]

def followPath(device, connections):
    if device == "out": return 1

    total = 0
    for connected in connections[device]:
        total += followPath(connected, connections)
    
    return total

print(followPath("you", connections))