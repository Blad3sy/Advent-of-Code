with open("Advent-of-Code-2023/solutions/files/day15input.txt", "r") as file:
    file = file.readline()

file = file.split(",")
file = [value.strip() for value in file]

boxes = {}
for i in range(256):
    boxes[i] = {}

for step in file:
    HASHValue = 0
    for i in range(len(step)):
        if step[i] == "=":
            stepToAdd = step.replace("=", " ").split()
            stepLabel = str(stepToAdd[0])
            stepFocalLength = int(stepToAdd[1])

            boxes[HASHValue][stepLabel] = stepFocalLength
            break

        elif step[i] == "-":
            stepToAdd = step.replace("-", " ").split()
            stepLabel = str(stepToAdd[0])

            if stepLabel in boxes[HASHValue].keys():
                boxes[HASHValue].pop(stepLabel)
            break

        else:
            HASHValue += ord(step[i])
            HASHValue *= 17
            HASHValue %= 256 

total = 0
for i in range(len(boxes.keys())):
    boxID = i + 1
    boxKeys = list(boxes[i].keys())

    for t in range(len(boxKeys)):
        secondBoxID = t + 1
        currentFocalLength = boxes[i][boxKeys[t]]

        total += boxID * secondBoxID * currentFocalLength

print(total)