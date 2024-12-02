with open("2024/files/day2input.txt") as file:
    fileLines = file.readlines()

unsafe = 0
for line in fileLines:
    linelist = [int(value) for value in line.strip("\n").split(" ")]
    
    dif = 0
    if linelist[1] - linelist[0] >= 0: decreasing = False
    else: decreasing = True

    for i in range(1, len(linelist)):
        dif = linelist[i] - linelist[i-1]

        if abs(dif) != 1 and abs(dif) != 2 and abs(dif) != 3:
            unsafe += 1 
            break

        if (dif < 0) and (not decreasing):
            unsafe += 1 
            break
        
        if (dif > 0) and (decreasing):
            unsafe += 1
            break

safe = len(fileLines) - unsafe
print(safe)