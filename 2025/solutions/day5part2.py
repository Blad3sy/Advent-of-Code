with open("2025/files/day5input.txt") as file:
    fileLines = file.readlines()

ids = [id.strip("\n").split("-") for id in fileLines]
ranges = []
rangesUsed = {}

for id in ids:
    if id == [""]: break
    ranges.append((int(id[0]), int(id[1])))
    rangesUsed[(int(id[0]), int(id[1]))] = False

def mergeRanges(ranges, rangesUsed):
    newRanges = []
    newRangesUsed = {}
    total = 0

    for range1 in ranges:
        if rangesUsed[range1]: continue

        for range2 in ranges:
            if rangesUsed[range2]: continue
            if range1 == range2: continue

            if range1[0] <= range2[1] and range2[0] <= range1[1]:
                newRange = (min(range1[0], range2[0]), max(range1[1], range2[1]))

                newRanges.append(newRange)
                newRangesUsed[newRange] = False

                rangesUsed[range1] = True
                rangesUsed[range2] = True
                total += 1
                break
    
    for key in rangesUsed.keys():
        if not rangesUsed[key]:
            newRanges.append(key)
            newRangesUsed[key] = False

    return newRanges, newRangesUsed, total

while True:
    ranges, rangesUsed, count = mergeRanges(ranges, rangesUsed)
    if count == 0: break

total = 0
for range in ranges: total += (range[1] - range[0] + 1)

print(total)