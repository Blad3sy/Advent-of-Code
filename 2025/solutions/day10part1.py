import itertools

with open("2025/files/day10input.txt") as file:
    fileLines = file.readlines()

data = [line.strip().split() for line in fileLines]
lights = [line[0].strip("[").strip("]") for line in data]
buttons = [line[1:-1] for line in data]

def flip(char):
    if char == ".": return "#"
    elif char == "#": return "."

def buttonPress(light, button):
    lightList = [char for char in light]
    buttonNums = [int(num) for num in button.strip("(").strip(")").split(",")]
    for num in buttonNums:
        lightList[num] = flip(lightList[num])
    light = str(lightList).replace("[", "").replace("]", "").replace("'", "").replace(",", " ").replace(" ", "")

    return light

def getShortest(buttonSet):
    baseState = ""
    for j in range(len(light)): baseState += "."

    for j in range(1, len(buttonSet)):
        permutations = list(itertools.permutations(buttonSet, j))

        for permutation in permutations:
            currentState = baseState
            for button in permutation:
                currentState = buttonPress(currentState, button)
                if currentState == light: return j

total = 0

for i in range(len(lights)):
    light = lights[i]
    button = buttons[i]

    print(i+1, "/", 170, f"({len(button)})")
    total += getShortest(button)

print(total)