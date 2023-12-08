def getType(hand):
    scores = []

    for letter in hand:
        added = False
        for i in range(len(scores)):
            if letter in scores[i]:
                scores[i].append(letter)
                added = True
        if not added: scores.append([letter])
    
    if len(scores) == 1:
        cardType = 6 # 5Kind

    elif len(scores) == 2:
        if len(scores[0]) == 4 or len(scores[1]) == 4:
            cardType = 5 # 4Kind
        else:
            cardType = 4 # FullHouse

    elif len(scores) == 3:
        if len(scores[0]) == 3 or len(scores[1]) == 3 or len(scores[2]) == 3:
            cardType = 3 # 3Kind
        else:
            cardType = 2 # 2Pair
    
    elif len(scores) == 4:
        cardType = 1 # 1Pair
    
    else:
        cardType = 0 # HighCard
    
    return cardType

def convertCardToNum(card):
    if card == "T": return 10
    elif card == "J": return 11
    elif card == "Q": return 12
    elif card == "K": return 13
    elif card == "A": return 14
    else: return int(card)

def bubble_Sort(array):
    change = True

    while change == True:
        change = False
        
        for i in range(0, len(array) - 1):
            bubbleLeft = array[i]

            if bubbleLeft[2] > array[i+1][2]:
                array[i] = array[i+1]
                array[i+1] = bubbleLeft
                change = True

            elif bubbleLeft[2] == array[i+1][2]:
                
                t = 0
                resolved = False

                while not resolved and t < 5:
                    leftNum = convertCardToNum(bubbleLeft[0][t])
                    rightNum = convertCardToNum(array[i+1][0][t])

                    if leftNum > rightNum:
                        array[i] = array[i+1]
                        array[i+1] = bubbleLeft
                        change = True
                        resolved = True

                    if rightNum > leftNum:
                        resolved = True

                    t += 1                      

    return array

with open("Advent-of-Code-2023/solutions/files/day7input.txt", "r") as file:
    fileLines = file.readlines()
    allHands = []

    for line in fileLines:
        sub = line.split()
        sub.append(getType(sub[0]))
        allHands.append(sub)
    
    allHands = bubble_Sort(allHands)

    total = 0

    for i in range(1, len(allHands) + 1):
        total += int(allHands[i - 1][1]) * i
    
    print(total)