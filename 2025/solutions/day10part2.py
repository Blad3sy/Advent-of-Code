import z3

with open("2025/files/day10input.txt") as file:
    fileLines = file.readlines()

data = [line.strip().split() for line in fileLines]
joltages = [[int(char) for char in line[-1].strip("{").strip("}").split(",")] for line in data]
buttons = [line[1:-1] for line in data]

total = 0
for i in range(len(joltages)):
    joltage = joltages[i]
    buttonSet = [set([int(num) for num in button.strip("(").strip(")").split(",")]) for button in buttons[i]]

    buttonPresses = [z3.Int(f"press{i}") for i in range(len(buttonSet))]
    solver = z3.Optimize()
    solver.add(z3.And([buttonPress >= 0 for buttonPress in buttonPresses]))
    solver.add(z3.And([sum(buttonPresses[j] for j, button in enumerate(buttonSet) if i in button) == jolt for i, jolt in enumerate(joltage)]))
    solver.minimize(sum(buttonPresses))

    assert solver.check() == z3.sat

    model = solver.model()
    totalPresses = 0
    for press in buttonPresses:
        totalPresses += model[press].as_long()
    
    total += totalPresses
print(total)