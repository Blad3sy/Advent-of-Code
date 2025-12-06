with open("2025/files/day6input.txt") as file:
    fileLines = [line.strip("\n") for line in file.readlines()]

lengths = [0 for num in fileLines[0].split()]
modes = fileLines[-1].split()

for k in range(len(fileLines) - 1):
    line = fileLines[k]
    startIndex = 0
    count = 0

    for i in range(len(line)):
        if i == len(line) - 1 or (line[i] == " " and line[i+1].isdigit()):
            if i == len(line) - 1: length = len(str(int(line[startIndex:])))
            else: length = len(str(int(line[startIndex:i])))
            startIndex = i + 1

            if length > lengths[count]: lengths[count] = length
            count += 1

total = 0
curIndex = 0

for i in range(len(lengths)):
    mode = modes[i]
    numbers = []
    
    for j in range(len(fileLines) - 1):
        numbers.append(fileLines[j][curIndex:curIndex + lengths[i]])
    curIndex += lengths[i] + 1
    
    longestNumLength = lengths[i]
    
    currentVal = 0
    for j in range(longestNumLength - 1, -1, -1):
        currentNum = ""
        for number in numbers:
            if number[j] != " ": currentNum += number[j]
        
        if currentVal == 0: currentVal = int(currentNum)
        else:
            if mode == "*": currentVal *= int(currentNum)
            else: currentVal += int(currentNum)
    
    total += currentVal

print(total)