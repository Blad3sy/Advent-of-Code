with open("2024/files/day11input.txt") as file:
    fileLine = file.readline()

stones = [int(value) for value in fileLine.strip("\n").split(" ")]

for i in range(25):
    newStones = []
    for j in range(len(stones)):
        if stones[j] == 0: newStones.append(1)
        elif len(str(stones[j])) % 2 == 0:
            strStone = str(stones[j])
            mid = len(strStone) // 2
            newStones.append(int(strStone[0:mid]))
            newStones.append(int(strStone[mid:]))
        else: newStones.append(stones[j] * 2024)
    stones = newStones

print(len(stones))