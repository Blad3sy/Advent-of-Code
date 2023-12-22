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

parts = {} # X M A S
counter = 0
for line in partsArray:
    line = line[1:-1]
    line = line.split(",")
    for i in range(len(line)):
        line[i] = int(line[i][2:])
    parts[counter] = line
    counter += 1

total = 0
counter = 1
for part in parts:
    print(f"{counter} / {len(parts)}")
    counter += 1

    x = parts[part][0]
    m = parts[part][1]
    a = parts[part][2]
    s = parts[part][3]

    id = "in"

    while id != "A" and id != "R":
        workflowkeys = list(workflows[id].keys())

        for key in workflowkeys:
            if key == "DEFAULT":
                id = workflows[id][key]
            else:
                if eval(key):
                    id = workflows[id][key]
                    break

    if id == "A":
        total += x + m + a + s

print(total)


'''a = 2000
print(eval(workflows["px"][0][:6]))'''