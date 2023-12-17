def checkHorizontalSym(thisPattern, lineIndex):
    # Line after the index
    if len(thisPattern[lineIndex + 1:]) > len(thisPattern[:lineIndex + 1]):
        numberOfLines = len(thisPattern[:lineIndex + 1])
    else:
        numberOfLines = len(thisPattern[lineIndex + 1:])
    
    beforeLine = []
    afterLine = []

    for i in range(lineIndex, lineIndex - numberOfLines, -1):
        beforeLine.append(thisPattern[i])
    
    for i in range(lineIndex + 1, lineIndex + 1 + numberOfLines):
        afterLine.append(thisPattern[i])
    
    if beforeLine == afterLine and numberOfLines > 0:
        return len(thisPattern[:lineIndex + 1])
    else: 
        return 0

def checkVerticalSym(thisPattern, rowIndex):
    if len(thisPattern[0][rowIndex + 1:]) > len(thisPattern[0][:rowIndex + 1]):
        numberOfLines = len(thisPattern[0][:rowIndex + 1])
    else:
        numberOfLines = len(thisPattern[0][rowIndex + 1:])
    
    beforeLine = ""
    afterLine = ""

    if numberOfLines == 0: return 0

    for i in range(len(thisPattern)):
        beforeLine = thisPattern[i][rowIndex + 1 - numberOfLines : rowIndex + 1]
        beforeLine = beforeLine[::-1]
        afterLine = thisPattern[i][rowIndex + 1 : rowIndex + 1 + numberOfLines]

        if beforeLine != afterLine:
            return 0
    
    return len(thisPattern[0][:rowIndex + 1])

with open("Advent-of-Code-2023/solutions/files/day13input.txt", "r") as file:
    fileLines = file.readlines()
    fileLines.append("")

allPatterns = []
currentPattern = []

for line in fileLines:
    if line.strip() == "":
        if currentPattern:
            allPatterns.append(currentPattern)
            currentPattern = []
    else:
        currentPattern.append(line.strip())

total = 0
for pattern in allPatterns:
    for i in range(len(pattern)):
        total += 100 * checkHorizontalSym(pattern, i)

for pattern in allPatterns:
    for i in range(len(pattern[0])):
        total += checkVerticalSym(pattern, i)

print(total)