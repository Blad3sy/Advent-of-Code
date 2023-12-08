def getType(hand):
    scores = []
    jokerCount = 0

    for letter in hand:
        added = False
        if letter == "J":
            jokerCount += 1

        for i in range(len(scores)):
            if letter in scores[i] and letter != "J":
                scores[i].append(letter)
                added = True
        if not added and letter != "J": scores.append([letter])
    
    if len(scores) == 0:
        scores = [["J", "J", "J", "J", "J"]]
    
    added = False
    for i in range(5):
        if added: break
        for t in range(len(scores)):
            if len(scores[t]) == 5 - i:
                for z in range(jokerCount):
                    scores[t].append("J")
                    added = True
            if added: break
    
    print(jokerCount, scores)
    
    lengthArray = []
    for i in range(len(scores)):
        lengthArray.append(len(scores[i]))
    
    if max(lengthArray) >= 5: return 6 # 5Kind
    elif max(lengthArray) == 4: return 5 #4Kind
    elif max(lengthArray) == 3:
        newList = [value for value in lengthArray if value != 3]
        if len(newList) == 1: return 4 # FullHouse
        else: return 3 # 3Kind
    elif max(lengthArray) == 2:
        newList = [value for value in lengthArray if value == 2]
        if len(newList) == 2: return 2 # 2Pair
        else: return 1 # 1Pair
    else: return 0 # HighCard

def convertCardToNum(card):
    if card == "J": return 1
    elif card == "T": return 10
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
    for hand in allHands:
        print(hand)

    total = 0

    for i in range(1, len(allHands) + 1):
        total += int(allHands[i - 1][1]) * i
    
    print(total)