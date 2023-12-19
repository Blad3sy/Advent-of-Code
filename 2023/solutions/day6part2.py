with open("Advent-of-Code-2023/solutions/files/day6input.txt", "r") as file:
    fileLines = file.readlines()

    time = ""
    for letter in fileLines[0] + " ":
        if letter.isdigit():
            time += letter
    
    distance = ""
    for letter in fileLines[1] + " ":
        if letter.isdigit():
            distance += letter

    time = int(time)
    distance = int(distance)

    print(time)
    print(distance)

    totalExponents = 0

    timesThatWin = 0
    for t in range(1, time):
        speed = t
        distanceTravelled = speed * (time - t)

        if distanceTravelled > distance:
            timesThatWin += 1
        
    print(timesThatWin)