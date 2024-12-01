with open("2024/files/day1input.txt") as file:
    fileLines = file.readlines()

list1 = []
list2 = []

for line in fileLines:
    lineComps =  [int(value) for value in line.strip("\n").split(" ") if value != '']
    list1.append(lineComps[0])
    list2.append(lineComps[1])

list1.sort()
list2.sort()

sum = 0
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum)