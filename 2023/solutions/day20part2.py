from math import lcm

totalHigh = 0
totalLow = 0

class Module():
    def __init__(self, name, typ):
        self.name = name
        self.type = typ

        self.inputs = []

        self.out = None

        self.targets = []
        self.recipients = []

        self.isOn = False

    def addTarget(self, target):
        self.targets.append(target)
    
    def addRecipient(self, recipient):
        self.recipients.append(recipient)

    def recieveInput(self, input, recipient):
        if input != None:
            if self.type == "&":
                offset = 0
                for i in range(len(self.inputs)):
                    if self.inputs[i - offset][1] == recipient:
                        self.inputs.pop(i)
                        offset += 1

            self.inputs.append([input, recipient])
    
    def calcOutput(self):
        if not self.inputs:
            return

        if self.type == "broadcaster":
            self.out = "L"

        elif self.type == "%":
            if self.inputs[0][0] == "H":
                self.out = None
            elif self.inputs[0][0] == "L":
                if self.isOn:
                    self.isOn = False
                    self.out = "L"
                else:
                    self.isOn = True    
                    self.out = "H"

            self.inputs.pop(0)

        elif self.type == "&":
            if all(value[0] == "H" for value in self.inputs) and len(self.inputs) == len(self.recipients):
                self.out = "L"
            else:
                self.out = "H"

        else:
            self.out = None    
    
    def output(self):
        global totalHigh
        global totalLow
        global moduleQueue
        global foundNums
        global counter

        self.calcOutput()

        if self.name == "xc" and self.out == "H" and foundNums[0] == False:
            foundNums[0] = counter
            print("xc", counter)
        if self.name == "ks" and self.out == "H" and foundNums[1] == False:
            foundNums[1] = counter
            print("ks", counter)
        if self.name == "ct" and self.out == "H" and foundNums[2] == False:
            foundNums[2] = counter
            print("ct", counter)
        if self.name == "kp" and self.out == "H" and foundNums[3] == False:
            foundNums[3] = counter
            print("kp", counter)


        for target in self.targets:
            if target == "rx": outputname = "rx"
            else: outputname = target.name
            # if self.out != None: print(module.name, f" -{self.out}-> ", outputname)

            if target != "rx": 
                target.recieveInput(self.out, self)
                if self.out != None: moduleQueue.append(target)

            if self.out == "H": totalHigh += 1
            elif self.out == "L": totalLow += 1

with open("Advent-of-Code-2023/2023/files/day20input.txt", "r") as file:
    fileLines = file.readlines()

moduleDict = {}
for i in range(len(fileLines)):
    fileLines[i] = fileLines[i] .split()
    
    moduleName = fileLines[i][0].replace("%", "").replace("&", "")

    if moduleName == "broadcaster":
        moduleType = "broadcaster"
    else:
        moduleType = fileLines[i][0][0]
    
    moduleDict[moduleName] = (Module(moduleName, moduleType))

    fileLines[i] = fileLines[i][2:]

moduleKeys = list(moduleDict.keys())

for i in range(len(fileLines)):
    for target in fileLines[i]:
        target = target.replace(",", "")
        if target != "rx": 
            moduleDict[moduleKeys[i]].addTarget(moduleDict[target])
            moduleDict[target].addRecipient(moduleDict[moduleKeys[i]])
        else: moduleDict[moduleKeys[i]].addTarget("rx")

foundNums = [False, False, False, False]
counter = 1
while True:
    totalLow += 1

    moduleDict["broadcaster"].recieveInput("L", None)
    moduleQueue = [moduleDict["broadcaster"]]

    for module in moduleQueue:
        module.output()
    
    if all(value != False for value in foundNums):
        break

    moduleQueue.clear()
    counter += 1

print(lcm(*foundNums))