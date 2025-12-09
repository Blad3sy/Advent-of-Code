with open("2025/files/day9input.txt") as file:
    fileLines = file.readlines()

coords = [tuple([int(num) for num in line.strip().split(",")]) for line in fileLines]
areas = {}

for i in range(len(coords)):
    for j in range(len(coords)):
        if i == j or (i, j) in areas.keys() or (j, i) in areas.keys(): continue
        area = (abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1)
        areas[(i, j)] = area

areas = sorted(areas.items(), key=lambda item: item[1], reverse = True)
print(areas[0][1])