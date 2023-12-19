def checkValid(string, nums):
    string += "."
    currentInstance = ""
    currentNumToCheck = 0

    for letter in string:
        if letter == "#":
            currentInstance += letter
        elif letter == "." and len(currentInstance) > 0:
            if currentNumToCheck >= len(nums):
                return False
            elif len(currentInstance) != int(nums[currentNumToCheck]):
                return False
            
            currentInstance = ""
            currentNumToCheck += 1
    
    if currentNumToCheck != len(nums):
        return False
    
    return True

def convert(s): 
    str1 = "" 
    return(str1.join(s)) 

with open("Advent-of-Code-2023/solutions/files/day12input.txt", "r") as file:
    fileLines = file.readlines()

springStrings = []
numLists = []

for i in range(len(fileLines)):
    spaceIndex = fileLines[i].index(" ")

    nums = fileLines[i][spaceIndex:].strip()
    springs = fileLines[i][:spaceIndex]

    numLists.append(nums.split(","))
    springStrings.append(springs)

print(numLists)
print(springStrings)

total = 0

for i in range(len(springStrings)):
    print(i)
    voidIndices = []
    binNum = ""

    for t in range(len(springStrings[i])):
        if springStrings[i][t] == "?":
            voidIndices.append(t)
            binNum += "0"

    tempstring = list(str(springStrings[i]))

    for z in range(2 ** len(binNum)):
        strBinNum = bin(z)
        strBinNum = strBinNum[2:]

        while len(strBinNum) < len(binNum):
            strBinNum = "0" + strBinNum
        
        for f in range(len(voidIndices)):
            if strBinNum[f] == "0":
                tempstring[voidIndices[f]] = "#"
            else: tempstring[voidIndices[f]] = "."
        
        if checkValid(convert(tempstring), numLists[i]):
            total += 1

print(total)