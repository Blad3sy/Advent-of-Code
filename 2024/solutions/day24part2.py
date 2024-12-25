from copy import deepcopy

with open("2024/files/day24input.txt") as file:
    fileLines = file.readlines()

wires = {}
instructions = []
baseValuesMode = True
xbin = ""
ybin = ""
for line in fileLines:
    line = line.strip("\n")
    if line == "": 
        baseValuesMode = False
        continue

    if baseValuesMode:
        line = line.split(":")
        if line[0][0] == "x": xbin = line[1].strip() + xbin
        if line[0][0] == "y": ybin = line[1].strip() + ybin
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
        wires[substr] = None
        instructions.append(instruction)

def findFullAdderRoots(zbit, gates):
    for gate in gates:
        if gate[3] == zbit and gate[1] == "XOR":
            zbit1 = gate[0]
            zbit2 = gate[2]
            break
    
    for gate in gates:
        if gate[3] == zbit1 and gate[1] == "XOR":
            xbit = gate[0]
            return xbit
        
        if gate[3] == zbit2 and gate[1] == "XOR":
            xbit = gate[0]
            return xbit   

wrongXORS = []
wrongANDORS = []
for instruction in instructions:
    if instruction[3][0] == "z":
        if instruction[1] != "XOR" and instruction[3][1:] != "45": wrongANDORS.append(instruction[3])
    else:
        if instruction[0][0] not in "xy" and instruction[2][0] not in "xy" and instruction[1] == "XOR": wrongXORS.append(instruction[3])

for wire in wrongXORS:
    id =  f"z{findFullAdderRoots(wire, instructions)[1:]}"
    
    for i in range(len(instructions)):
        if instructions[i][3] == id and instructions[i][1] != "XOR":
            instructions[i][3] = wire
            break
    
    for i in range(len(instructions)):
        if instructions[i][3] == wire and instructions[i][1] == "XOR":
            instructions[i][3] = id
            break

swaps = []
swaps += wrongXORS
swaps += wrongANDORS

def instructionExecute(A, B, gate):
    if gate == "AND": return A & B
    elif gate == "OR": return A | B
    elif gate == "XOR": return A ^ B

def getAnswer(instructions):
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

    return int(binstring, 2)

correct = int(xbin, 2) + int(ybin, 2)
result = getAnswer(deepcopy(instructions))

differenceString = '{0:045b}'.format(correct ^ result)
for i in range(0, len(differenceString) + 1):
    if differenceString[-i] == "1": 
        carryStringIncorrect = i - 1
        break

incorrectZBIT = f"z{carryStringIncorrect}"

def findflawedRootOutput(zbit, gates):
    presumedxRoot, presumedyRoot = f"x{zbit[1:]}", f"y{zbit[1:]}"
    for gate in gates:
        if gate[3] == zbit and gate[1] == "XOR":
            zbit1 = gate[0]
            zbit2 = gate[2]
            break
    
    for gate in gates:
        if (gate[0] == presumedxRoot and gate[2] == presumedyRoot) or (gate[2] == presumedxRoot and gate[0] == presumedyRoot):
            if gate[3] == zbit1 and gate[1] != "XOR":
                return gate
        
            if gate[3] == zbit2 and gate[1] != "XOR":
                return gate

wrongGate = findflawedRootOutput(incorrectZBIT, instructions)
swap1 = wrongGate[3]

for i in range(len(instructions)):
    if ((instructions[i][0] == wrongGate[0] and instructions[i][1] == "XOR" and instructions[i][2] == wrongGate[2]) or 
        (instructions[i][0] == wrongGate[2] and instructions[i][1] == "XOR" and instructions[i][2] == wrongGate[0])):

        swap2 = instructions[i][3]
        swaps += [swap1, swap2]
        break

swaps.sort()
outputstr = ""
for swap in swaps: outputstr += f"{swap},"
print(outputstr[:-1])

# Used this tutorial
# https://www.reddit.com/r/adventofcode/comments/1hlhhjv/2024_day_24_part_2_python_need_help_getting_the/
# And SOME of my own ideas and code