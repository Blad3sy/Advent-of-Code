with open("2024/files/day2input.txt") as file:
    fileLines = file.readlines()

safelist = {}
for i in range(len(fileLines)):
    safelist[i] = False

for count in range(len(fileLines)):
    line = fileLines[count]
    linelist = [int(value) for value in line.strip("\n").split(" ")]
    
    for i in range(len(linelist)):
        dampenedReport = []
        for j in range(len(linelist)):
            if j != i: dampenedReport.append(linelist[j])

        safe = True
        dif = 0
        if dampenedReport[1] - dampenedReport[0] >= 0: decreasing = False
        else: decreasing = True

        for k in range(1, len(dampenedReport)):
            dif = dampenedReport[k] - dampenedReport[k-1]

            if abs(dif) != 1 and abs(dif) != 2 and abs(dif) != 3:
                safe = False
                break

            elif (dif < 0) and (not decreasing):
                safe = False
                break
        
            elif (dif > 0) and (decreasing):
                safe = False
                break
        
        if safe == True:  safelist[count] = True

safe = 0
for key in safelist.keys():
    if safelist[key]: safe += 1

print(safe)