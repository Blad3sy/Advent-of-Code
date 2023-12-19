with open("Advent-of-Code-2023/solutions/files/day6input.txt", "r") as file:
    fileLines = file.readlines()

    times = []
    distances = []

    numConstructor = ""
    for letter in fileLines[0] + " ":
        if letter.isdigit():
            numConstructor += letter
        elif letter == " ":
            if numConstructor != "":
                times.append(int(numConstructor))
                numConstructor = ""
    
    numConstructor = ""
    for letter in fileLines[1] + " ":
        if letter.isdigit():
            numConstructor += letter
        elif letter == " ":
            if numConstructor != "":
                distances.append(int(numConstructor))
                numConstructor = ""
    
    totalExponents = 0

    for i in range(len(times)):
        timesThatWin = 0
        for t in range(1, times[i]):
            speed = t
            distanceTravelled = speed * (times[i] - t)

            if distanceTravelled > distances[i]:
                timesThatWin += 1
        
        if not totalExponents: totalExponents += timesThatWin
        else: totalExponents *= timesThatWin
    
    print(totalExponents)