with open("2024/files/day9input.txt") as file:
    diskmap = file.readline()

diskmap = [int(char) for char in diskmap]
fileID = 0
expandedDiskMap = []
for i in range(len(diskmap)):
    if (i + 1) % 2 == 1:
        for j in range(diskmap[i]):
            expandedDiskMap.append(fileID)
        fileID += 1

    if (i + 1) % 2 == 0:
        for j in range(diskmap[i]):
            expandedDiskMap.append(".")

endpos = -1
for i in range(len(expandedDiskMap)):
    if expandedDiskMap[i] == ".":
        expandedDiskMap[i] = expandedDiskMap[endpos]
        expandedDiskMap[endpos] = "."

        while True:
            endpos -= 1
            if expandedDiskMap[endpos] != ".": break
            if len(expandedDiskMap) + endpos - 1 <= i: break
        
        if len(expandedDiskMap) + endpos - 1 <= i: break
    
checksum = 0
for i in range(len(expandedDiskMap)):
    if expandedDiskMap[i] != ".":
        checksum += i * expandedDiskMap[i]
print(checksum)