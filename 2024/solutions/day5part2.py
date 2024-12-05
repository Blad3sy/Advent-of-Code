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

correctedIndices = []
while True:
    incorrectUpdates = []
    for update in updates:
        for pageNum in pageOrders.keys():
            if pageNum in update:
                firstOccurence = update.index(pageNum)
                for i in range(firstOccurence):
                    if update[i] in pageOrders[pageNum]: 
                        incorrectUpdates.append(update)
                        val = update[i]
                        update[firstOccurence] = val
                        update[i] = pageNum

                        if updates.index(update) not in correctedIndices: correctedIndices.append(updates.index(update))
                        break

    if incorrectUpdates == []: break

sum = 0
for i in range(len(updates)):
    if i in correctedIndices:
        middle = int(len(updates[i]) / 2)
        sum += int(updates[i][middle])
print(sum)