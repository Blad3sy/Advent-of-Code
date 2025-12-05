with open("2025/files/day5input.txt") as file:
    fileLines = file.readlines()

ids = [id.strip("\n").split("-") for id in fileLines]
total = 0

checkMode = False
ranges = []

for id in ids:
    if id == [""]:
        checkMode = True
        continue

    if checkMode:
        intID = int(id[0])
        for currentRange in ranges:
            if intID in currentRange:
                total += 1 
                break
            
    else: ranges.append(range(int(id[0]), int(id[1]) + 1))

print(total)