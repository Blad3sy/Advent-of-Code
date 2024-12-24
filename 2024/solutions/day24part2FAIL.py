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

def findFullAdder(zbit, gates):
    for gate in gates:
        if gate[3] == zbit and gate[1] == "XOR":
            zbit1 = gate[0]
            zbit2 = gate[2]
            break
    
    for gate in gates:
        if gate[3] == zbit1 and gate[1] == "XOR":
            xbit = gate[0]
            ybit = gate[2]
            return zbit
        
        if gate[3] == zbit2 and gate[1] == "XOR":
            xbit = gate[0]
            ybit = gate[2]
            return zbit
    
    print(xbit, ybit)

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

def instructionExecute(A, B, gate):
    if gate == "AND": return A & B
    elif gate == "OR": return A | B
    elif gate == "XOR": return A ^ B

def getBinstring(instructions, wires):
    history = []
    while instructions != []:        
        curLength = len(instructions)
        history.append(curLength)

        if len(history) > 10000:
            if history[-10000] == curLength: return None

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

    try: return int(binstring, 2)
    except ValueError: pass

exists = []
for wire in wires.keys():
    try: exists.append(findFullAdder(wire, instructions))
    except: pass

allWires = []
missing = []
#z00 and z45 aren't part of full adders as z00 receives no carry and z45 outputs no carry
for i in range(1, 45):
    if i < 10: check = f"z0{i}"
    else: check = f"z{i}"

    if check not in exists: missing.append(check)
allWires += missing

outofPlace = []
for exist in exists:
    if exist[0] != "z": outofPlace.append(exist)
allWires += outofPlace

for wire in outofPlace:
    id =  f"z{findFullAdderRoots(wire, instructions)[1:]}"
    
    for i in range(len(instructions)):
        if instructions[i][3] == id and instructions[i][1] != "XOR":
            instructions[i][3] = wire
            break
    
    for i in range(len(instructions)):
        if instructions[i][3] == wire and instructions[i][1] == "XOR":
            instructions[i][3] = id
            break   

    missing.remove(id)

final = missing[0]
correct = int(xbin, 2) + int(ybin, 2)
incorrect = getBinstring(deepcopy(instructions), deepcopy(wires))

for i in range(len(instructions)):
    if instructions[i][3] == final: finalIndex = i

for i in range(len(instructions)):
    testInt = deepcopy(instructions)
    
    testInt[finalIndex][3] = testInt[i][3]
    testInt[i][3] = final

    result = getBinstring(deepcopy(testInt), deepcopy(wires))
    
    if result == correct:
        allWires.append(testInt[finalIndex][3])
        break

allWires.sort()
outputStr = ""
for wire in allWires: outputStr += f"{wire},"
outputStr = outputStr[:-1]
print(outputStr)

# Leaving this in as it gets the correct value for the input but not ALL cases, and I came up with this one myself before following a tutorial