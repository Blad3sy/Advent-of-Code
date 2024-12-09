with open("2024/files/day9input.txt") as file:
    diskmap = file.readline()

diskmap = [int(char) for char in diskmap]
fileID = 0
expandedDiskMap = []
fileLog = {}

for i in range(len(diskmap)):
    if (i + 1) % 2 == 1:
        fileLog[fileID] = [diskmap[i], len(expandedDiskMap)]
        for j in range(diskmap[i]):
            expandedDiskMap.append(fileID)
        fileID += 1

    if (i + 1) % 2 == 0:
        for j in range(diskmap[i]):
            expandedDiskMap.append(".")

fileLogKeys = list(fileLog.keys())
for j in range(-1, -1 - len(fileLogKeys), -1):
    print(j * -1, "/", len(fileLogKeys))
    fileID = fileLogKeys[j]

    for i in range(len(expandedDiskMap)):
        if i >= fileLog[fileID][1]: break     
        if expandedDiskMap[i] == ".":
            for b in range(i, len(expandedDiskMap)):
                if expandedDiskMap[b] != ".":
                    emptyLength = b - i
                    break

            if fileLog[fileID][0] <= emptyLength:
                for k in range(fileLog[fileID][0]):
                    expandedDiskMap[i + k] = fileID
                    expandedDiskMap[fileLog[fileID][1] + k] = "." 
                break          

checksum = 0
for i in range(len(expandedDiskMap)):
    if expandedDiskMap[i] != ".":
        checksum += i * expandedDiskMap[i]
print(checksum)