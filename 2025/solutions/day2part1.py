with open("2025/files/day2input.txt") as file:
    fileLines = file.readlines()
total = 0

ids = fileLines[0].split(",")
for id in ids:
    idrange = id.split("-")
    for i in range(int(idrange[0]), int(idrange[1]) + 1):
        realID = str(i)
        if len(realID) % 2 != 0: continue

        length = len(realID)
        start = realID[0:int(length / 2)]
        end = realID[int(length / 2):]

        if start == end: total += int(realID)

print(total)