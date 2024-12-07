def convertToTernary(num):
    ternaryString = "0000000000000000"

    if num == 0: return ternaryString  
    bits = []
    while num:
        num, result = divmod(num, 3)
        bits.append(str(result))

    for i in range(len(bits)):
        ternaryString = list(ternaryString)
        ternaryString[-1 - i] = bits[i]
        ternaryString = "".join(ternaryString)
    
    return ternaryString



with open("2024/files/day7input.txt") as file:
    fileLines = file.readlines()

total = 0
counter = 1

for line in fileLines:
    print(counter, "/", len(fileLines))
    expectedValue = int(line.split(":")[0])
    operands =  [int(value) for value in line.split(":")[1].strip().split(" ")]

    numberOfOperators = len(operands) - 1
    for i in range(3 ** numberOfOperators): 
        formatMask = convertToTernary(i)

        sum = operands[0]
        for j in range(1, len(operands)):
            if formatMask[0 - j] == "0": sum += operands[j]
            elif formatMask[0 - j] == "1": sum *= operands[j]
            else: sum = int(str(sum) + str(operands[j]))
        
        if sum == expectedValue: 
            total += sum
            break
    
    counter += 1

print()
print(total)