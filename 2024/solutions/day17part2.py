from math import floor

with open("2024/files/day17input.txt") as file:
    fileLines = file.readlines()

regA = 0
regB = 0
initregB = 0
regC = 0
initregC = 0
program = []
instructionPointer = 0
jump = False
output = []

for line in fileLines:
    if "A" in line: 
        regA = int("".join([char for char in line if char.isnumeric()]))
    elif "B" in line:
        regB = int("".join([char for char in line if char.isnumeric()]))
    elif "C" in line:
        regC = int("".join([char for char in line if char.isnumeric()]))
    elif "P" in line:
        program = [int(char) for char in line if char.isnumeric()]

initregB = regB
intiregC = regC

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

def out(operand): 
    output.append(combo(operand) % 8)

def bdv(operand):
    global regA
    global regB
    regB = int(floor(regA / (2**combo(operand))))

def cdv(operand):
    global regA
    global regC
    regC = int(floor(regA / (2**combo(operand))))

test = 0
numToFind = -2

while True:
    regA = test
    regB = initregB
    regC = initregC
    instructionPointer = 0
    jump = False
    output = []

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

    if output == program: break
    if output[numToFind:] == program[numToFind:]:
        test *= 64
        numToFind -= 2

    test += 1

print(test)

# Completed with help of this reddit comment
# https://tinyurl.com/mkw2y6rs

# I really like the part 1 of this one (probably because it was fairly easy, but fun.)
# I really struggled with part 2, and had to use this hint to get it - even then, I'm not sure I really got it
# and I just played around with some ideas on how it might work until it did. Shame - I had some ideas and was 
# staring at my output and the pattern recognition was real (apparently the strategy I used (iterating
# by increasing powers of 8 when a new number matches, but it doesn't work as the interval between
# number changes for each of the 16 digits is non-constant on miy input) actually works for some inputs!),
# but ultimately I fell to this.