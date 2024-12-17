from math import floor

with open("2024/files/day17input.txt") as file:
    fileLines = file.readlines()

regA = 0
regB = 0
regC = 0
program = []
instructionPointer = 0
jump = False

for line in fileLines:
    if "A" in line: 
        regA = int("".join([char for char in line if char.isnumeric()]))
    elif "B" in line:
        regB = int("".join([char for char in line if char.isnumeric()]))
    elif "C" in line:
        regC = int("".join([char for char in line if char.isnumeric()]))
    elif "P" in line:
        program = [int(char) for char in line if char.isnumeric()]

def combo(operand):
    global regA
    global regB
    global regC

    match operand:
        case 0: return 0
        case 1: return 1
        case 2: return 2
        case 3: return 3
        case 4: return regA
        case 5: return regB
        case 6: return regC

def adv(operand): 
    global regA
    regA = int(floor(regA / (2**combo(operand))))

def bxl(operand): 
    global regB
    regB = regB ^ operand

def bst(operand): 
    global regB
    regB = combo(operand) % 8

def jnz(operand):
    global regA
    global instructionPointer
    global jump
    if regA == 0: return
    instructionPointer = operand
    jump = True

def bxc(operand):
    global regB
    global regC

    regB = regB ^ regC

def out(operand): print(f"{combo(operand) % 8},", end = "")
def bdv(operand):
    global regA
    global regB
    regB = int(floor(regA / (2**combo(operand))))

def cdv(operand):
    global regA
    global regC
    regC = int(floor(regA / (2**combo(operand))))

while instructionPointer < len(program):
    match program[instructionPointer]:
        case 0: adv(program[instructionPointer + 1])
        case 1: bxl(program[instructionPointer + 1])
        case 2: bst(program[instructionPointer + 1])
        case 3: jnz(program[instructionPointer + 1])
        case 4: bxc(program[instructionPointer + 1])
        case 5: out(program[instructionPointer + 1])
        case 6: bdv(program[instructionPointer + 1])
        case 7: cdv(program[instructionPointer + 1])
    if not jump: instructionPointer += 2
    jump = False