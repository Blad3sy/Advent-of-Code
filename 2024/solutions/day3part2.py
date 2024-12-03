with open("2024/files/day3input.txt") as file:
    fileLines = file.readlines()

instruction = "".join(fileLines)
subinstruction = ""
realinstructions = []
bracketopen = False

doInstruction = True

for letter in instruction:
    if letter == "m" or letter == "d": 
        subinstruction = ""
        bracketopen = False

    subinstruction += letter

    if (not letter.isnumeric()) and (not letter in "mul,()don't"):
        subinstruction = ""
        bracketopen = False

    if letter == "(":
        if bracketopen:
            subinstruction = ""
            bracketopen = False
        else:
            bracketopen = True

    if letter == ")":
        bracketopen = False
        if subinstruction[0:4] == "mul(" and subinstruction[-1] == ")" and doInstruction:
            realinstructions.append(subinstruction)
            subinstruction = ""
        
        if subinstruction == "do()": 
            doInstruction = True
            subinstruction = ""

        if subinstruction == "don't()": 
            doInstruction = False
            subinstruction = ""

sum = 0
for mult in realinstructions:
    cleaner = mult
    cleaner = [int(value) for value in cleaner[4:-1].split(",")]
    sum += cleaner[0] * cleaner[1]
print(sum)