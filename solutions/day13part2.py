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

def getOpposite(para):
    if para == ".": return "#"
    else: return "."

def convert(s): 
    new = "" 

    for x in s: 
        new += x 
 
    return new 

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
print(len(allPatterns))
input()
for i in range(len(allPatterns)):
    print(f"pattern {i + 1}")
    horiSym = None
    vertiSym = None
    end = False

    for t in range(len(allPatterns[i])):
        if checkHorizontalSym(allPatterns[i], t):
            horiSym = t
    
    for t in range(len(allPatterns[i][0])):
        if checkVerticalSym(allPatterns[i], t):
            vertiSym = t

    for q in range(len(allPatterns[i])):
        for w in range(len(allPatterns[i][q])):
            unsmudged = allPatterns[i]
            unsmudged[q] = [value for value in unsmudged[q]]
            unsmudged[q][w] = getOpposite(unsmudged[q][w])
            unsmudged[q] = convert(unsmudged[q])

            for t in range(len(unsmudged)):
                if checkHorizontalSym(unsmudged, t) and t != horiSym:
                    total += checkHorizontalSym(unsmudged, t) * 100
                    end = True

            for t in range(len(unsmudged[0])):
                if checkVerticalSym(unsmudged, t) and t != vertiSym:
                    total += checkVerticalSym(unsmudged, t)
                    end = True

            unsmudged[q] = [value for value in unsmudged[q]]
            unsmudged[q][w] = getOpposite(unsmudged[q][w])
            unsmudged[q] = convert(unsmudged[q])

            if end: break
        if end: break

print(total)