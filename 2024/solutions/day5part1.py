with open("2024/files/day5input.txt") as file:
    fileLines = file.readlines()

instructions = []
updates = []

for line in fileLines:
    line = line.strip("\n")
    if "|" in line: instructions.append(line.split("|"))
    elif line == "": pass
    else: updates.append(line.split(","))

pageOrders = {}
for instruction in instructions:
    if instruction[0] not in pageOrders.keys(): pageOrders[instruction[0]] = []    
    pageOrders[instruction[0]].append(instruction[1])

sum = 0
for update in updates:
    correctOrder = True

    for pageNum in pageOrders.keys():
        if pageNum in update:
            firstOccurence = update.index(pageNum)
            for i in range(firstOccurence):
                if update[i] in pageOrders[pageNum]: correctOrder = False
    
    if correctOrder:
        middle = int(len(update) / 2)
        sum += int(update[middle])

print(sum)