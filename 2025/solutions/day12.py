with open("2025/files/day12input.txt") as file:
    fileLines = file.readlines()

areas = [line.strip() for line in fileLines if "x" in line]
immediateValids = []
immediateInvalids = []

for area in areas:
    splits = area.split()
    lengthWidth = splits[0].strip(":").split("x")
    totalArea = int(lengthWidth[0]) * int(lengthWidth[1])

    totalHueristicPresentArea = 0
    for i in range(1, len(splits)):
        totalHueristicPresentArea += (int(splits[i]) * 9)

    if totalArea >= totalHueristicPresentArea: immediateValids.append(area)
    else: immediateInvalids.append(area)

# THIS WAS SUPPOSED TO BE A PRELIMINARY CHECK TO SCREEN OUT TRIVAL CASES WHAT IS THIS WHY DOES IT WORK
print(len(immediateValids))