with open("Advent-of-Code-2023/2023/files/day19input.txt", "r") as file:
    fileLines = file.readlines()

addToParts = False
workflowArray = []
partsArray = []

for line in fileLines:
    if line.strip() == "":
        addToParts = True
    else:
        if addToParts: partsArray.append(line.strip())
        else: workflowArray.append(line.strip())

workflows = {}

for line in workflowArray:
    line = line.strip().split("{")
    line[1] = line[1][:-1]
    id = line[0]

    workflow = line[1]
    workflow = workflow.split(",")
    actualworkflow = {}

    for i in range(len(workflow)):
        splitter = workflow[i].split(":")
        
        if len(splitter) > 1:
            condition = splitter[0]
            newid = splitter[1]
            actualworkflow[condition] = newid
        else:
            actualworkflow["DEFAULT"] = splitter[0]
    
    workflows[id] = actualworkflow

xmas = {
    "x" : [1, 4000],
    "m" : [1, 4000],
    "a" : [1, 4000],
    "s" : [1, 4000]
}

def getSplitInterval(thisxmas, condition):

    char = condition[0]
    operator = condition[1]
    num = int(condition[2:])

    xmasBefore, xmasAfter = thisxmas.copy(), thisxmas.copy()

    newItemBefore = [thisxmas[char][0], num-1] if operator == '<' else [thisxmas[char][0], num]
    xmasBefore[char] = newItemBefore

    newItemAfter = [num, thisxmas[char][1]] if operator == '<' else [num+1, thisxmas[char][1]]
    xmasAfter[char] = newItemAfter

    return xmasBefore, xmasAfter


def calculateInterval(xmas, workflows, id):

    if id == "A":
        return (xmas['x'][1]-xmas['x'][0]+1)*(xmas['m'][1]-xmas['m'][0]+1)*(xmas['a'][1]-xmas['a'][0]+1)*(xmas['s'][1]-xmas['s'][0]+1)
    elif id == "R":
        return 0

    copyxmas = xmas.copy()
    total = 0
    for condition in workflows[id]:

        if condition == "DEFAULT":
            total += calculateInterval(copyxmas, workflows, workflows[id][condition])
            break

        operator = condition[1]
        xmasBefore, xmasAfter = getSplitInterval(copyxmas, condition)

        if operator == '<':
            inXmas = xmasBefore
            outXmas = xmasAfter
        elif operator == '>':
            inXmas = xmasAfter
            outXmas = xmasBefore
        
        copyxmas = outXmas
        total += calculateInterval(inXmas, workflows, workflows[id][condition])
    
    return total

total = 0
total = calculateInterval(xmas, workflows, "in")
print(total)