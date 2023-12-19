with open("Advent-of-Code-2023/solutions/files/day15input.txt", "r") as file:
    file = file.readline()

file = file.split(",")
file = [value.strip() for value in file]

finalValues = []

for step in file:
    currentValue = 0
    for letter in step:
        currentValue += ord(letter)
        currentValue *= 17
        currentValue %= 256
    finalValues.append(currentValue)

total = 0
for item in finalValues:
    total += item
print(total)