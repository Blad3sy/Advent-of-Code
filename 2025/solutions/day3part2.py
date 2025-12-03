with open("2025/files/day3input.txt") as file:
    fileLines = file.readlines()

banks = [line.strip("\n") for line in fileLines]
total = 0

def getNextHighest(string, minLength):
    largestIndex = 0
    index = 0
    
    while len(string[index:]) > minLength:
        if int(string[index]) > int(string[largestIndex]): largestIndex = index
        index += 1
    return largestIndex

for bank in banks:
    thisBank = bank
    stringbuild = ""

    for i in range(12):
        nextIndex = getNextHighest(thisBank, (11 - i))
        stringbuild += thisBank[nextIndex]
        thisBank = thisBank[nextIndex + 1:]

    total += int(stringbuild)

print(total)