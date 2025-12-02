with open("2025/files/day2input.txt") as file:
    fileLines = file.readlines()
total = 0

def checkPattern(patternCheck, string):
    if string == patternCheck: return True
    if len(patternCheck) > len(string): return False

    patternLength = len(patternCheck)
    if string[0:patternLength] == patternCheck: return checkPattern(patternCheck, string[patternLength:])
    else: return False

ids = fileLines[0].split(",")
for id in ids:
    idrange = id.split("-")
    for i in range(int(idrange[0]), int(idrange[1]) + 1):
        realID = str(i)
        length = len(realID)

        for j in range(1, length):
            if checkPattern(realID[0:j], realID): 
                total += int(realID)
                break

print(total)