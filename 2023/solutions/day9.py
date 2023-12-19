with open("Advent-of-Code-2023/solutions/files/day9input.txt", "r") as file:
    fileLines = file.readlines()

total = 0

for line in fileLines:
    sequenceArray = []

    currentLineArray = line.split()
    currentLineArray = [int(value) for value in currentLineArray]

    sequenceArray.append(currentLineArray)

    allZeroes = False
    while not allZeroes:
        numArray = sequenceArray[0]
        intermediateArray = []

        for i in range(len(numArray) - 1):
            dif = numArray[i+1] - numArray[i]
            intermediateArray.append(dif)
        
        sequenceArray.insert(0, intermediateArray)
        
        arrayCheck = [value for value in intermediateArray if value != 0]
        if len(arrayCheck) == 0:
            allZeroes = True

    for i in range(len(sequenceArray) - 1):
        sequenceArray[i+1].append(sequenceArray[i+1][-1] + sequenceArray[i][-1])
    
    total += sequenceArray[-1][-1]

print(total)