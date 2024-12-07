with open("2024/files/day7input.txt") as file:
    fileLines = file.readlines()

total = 0
for line in fileLines:
    expectedValue = int(line.split(":")[0])
    operands =  [int(value) for value in line.split(":")[1].strip().split(" ")]

    numberOfOperators = len(operands) - 1
    for i in range(2 ** numberOfOperators): 
        formatMask = '{0:016b}'.format(i)

        sum = operands[0]
        for j in range(1, len(operands)):
            if formatMask[0 - j] == "0": sum += operands[j]
            else: sum *= operands[j]
        
        if sum == expectedValue: 
            total += sum
            break

print(total)