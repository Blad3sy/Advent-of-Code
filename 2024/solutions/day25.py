with open("2024/files/day25input.txt") as file:
    fileLines = file.readlines()
    fileLines.append("")

locks = []
keys = []
cur = []

for line in fileLines:
    line = line.strip("\n")

    if line == "":
        if cur == []: pass
        elif cur[0][0] == "#": locks.append(cur)
        elif cur[0][0] == ".": keys.append(cur)

        cur = []
    else:
        cur.append(line)

lockmaps = []
for lock in locks:
    lockmap = [-1 for i in range(len(lock[0]))]
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            if lock[i][j] == "#": lockmap[j] += 1
    
    lockmaps.append(lockmap)

keymaps = []
for key in keys:
    keymap = [-1 for i in range(len(key[0]))]
    for i in range(len(key)):
        for j in range(len(key[i])):
            if key[i][j] == "#": keymap[j] += 1
    
    keymaps.append(keymap)

def lockKeyMatch(lockmap, keymap):
    for i in range(len(lockmap)):
        if lockmap[i] + keymap[i] >= 6: return False
        #if lockmap[i] + keymap[i] <= 6: return False
    return True

total = 0
for i in range(len(lockmaps)):
    for j in range(len(keymaps)):
        if lockKeyMatch(lockmaps[i], keymaps[j]): total += 1
print(total)