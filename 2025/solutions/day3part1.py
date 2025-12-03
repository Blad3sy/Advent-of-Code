with open("2025/files/day3input.txt") as file:
    fileLines = file.readlines()

banks = [line.strip("\n") for line in fileLines]
total = 0

for bank in banks:
    first = 0
    firstIndex = None

    second = 0
    secondIndex = None

    for i in range(len(bank)):
        if int(bank[i]) > first:
            second = first
            secondIndex = firstIndex

            first = int(bank[i])
            firstIndex = i

        elif int(bank[i]) > second:
            second = int(bank[i])
            secondIndex = i

    third = 0   
    for i in range(firstIndex + 1, len(bank)):
        if int(bank[i]) > third: third = int(bank[i])
    
    if firstIndex < secondIndex: final1 = (10 * first) + second
    else: final1 = (10 * second) + first

    if firstIndex + 1 == len(bank): final2 = -100
    else: final2 = (10 * first) + third
    
    total += max(final1, final2)

print(total)