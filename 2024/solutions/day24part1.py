with open("2024/files/day24input.txt") as file:
    fileLines = file.readlines()

wires = {}
instructions = []
baseValuesMode = True
for line in fileLines:
    line = line.strip("\n")
    if line == "": 
        baseValuesMode = False
        continue

    if baseValuesMode:
        line = line.split(":")
        wires[line[0]] = int(line[1])

    else:
        instruction = []
        substr = ""
        for char in line:
            if char == " ": 
                if substr == "AND" or substr == "OR" or substr == "XOR": instruction.append(substr)
                elif substr != "":
                    if substr not in wires.keys(): wires[substr] = None
                    instruction.append(substr)
                substr = ""

            elif char in "->": substr = ""
            else: substr += char
        instruction.append(substr)
        instructions.append(instruction)

def instructionExecute(A, B, gate):
    if gate == "AND": return A & B
    elif gate == "OR": return A | B
    elif gate == "XOR": return A ^ B

while instructions != []:
    currentInstruction = instructions.pop(0)
    para1 = currentInstruction[0]
    gate = currentInstruction[1]
    para2 = currentInstruction[2]
    register = currentInstruction[3]

    if wires[para1] != None and wires[para2] != None: wires[register] = instructionExecute(wires[para1], wires[para2], gate)
    else: instructions.append(currentInstruction)

zregisters = {}
for key in wires.keys():
    if "z" in key:
        keyID = int("".join([char for char in list(key) if char.isnumeric()]))
        zregisters[keyID] = wires[key]

binstring = ""
for i in range(len(zregisters)):
    binstring = str(zregisters[i]) + binstring

print(int(binstring, 2))