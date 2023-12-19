def mapConvert(destNums, sourceNums, counts, seeds):
    finalSeeds = []
    for seed in seeds:
        finalSeeds.append(seed)

    for i in range(len(counts)):
        for t in range(len(seeds)):
            if seeds[t] >= sourceNums[i] and seeds[t] < sourceNums[i] + counts[i]:
                difference = destNums[i] - sourceNums[i]
                finalSeeds[t] = seeds[t] + difference
            
    for i in range(len(finalSeeds)):
        if finalSeeds[i] == None:
            finalSeeds[i] = seeds[i]
        
    return finalSeeds  

with open("Advent-of-Code-2023/solutions/files/day5input.txt", "r") as file:
    fileLines = file.readlines()
    fullPathMap = []

    seeds = []
    subSeeds = []
    numConstructor = ""
    for i in range(len(fileLines[0])):
        if fileLines[0][i].isdigit():
            numConstructor += fileLines[0][i]
        elif fileLines[0][i] == " " or i == len(fileLines[0]) - 1:
            if numConstructor != "":
                subSeeds.append(int(numConstructor))
            numConstructor = ""
            if len(subSeeds) == 2:
                seeds.append(subSeeds)
                subSeeds = []
    
    print(seeds)

    onNumLine = False
    numConstructor = ""
    lineNums = []

    for i in range(1, len(fileLines)):
        currentLine = fileLines[i]

        if currentLine == "\n":
            if lineNums:
                destNums = []
                sourceNums = []
                counts = []

                for i in range(len(lineNums)):
                    if i % 3 == 0:
                        destNums.append(lineNums[i])
                    elif i % 3 == 1:
                        sourceNums.append(lineNums[i])
                    else:
                        counts.append(lineNums[i])
                
                fullPathMap.append([destNums, sourceNums, counts])

            onNumLine = False
            lineNums = []
        
        if onNumLine:
            for i in range(len(currentLine)):
                if currentLine[i].isdigit():
                    numConstructor += currentLine[i]
                elif currentLine[i] == " " or i == len(currentLine) - 1:
                    if numConstructor != "":
                        lineNums.append(int(numConstructor))
                        numConstructor = ""
        
        if currentLine[0].isalpha():
            onNumLine = True
    
    lowest = 2000000000
    
    for seed in seeds:
        actualSeeds = []
        for i in range(seed[0], seed[0] + seed[1]):
            actualSeeds.append(i)

        print(f"{seed} DONE")
        counter = 0
        for path in fullPathMap:
            actualSeeds = mapConvert(path[0], path[1], path[2], actualSeeds)
            print(f"CONVERSION {counter} DONE")
            counter += 1
            
        print(f"{seed} DONE 2")
        actualSeeds.sort()
        if actualSeeds[0] < lowest:
            lowest = actualSeeds[0]
    
    print(lowest)