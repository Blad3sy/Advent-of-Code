total = 0

with open("Advent-of-Code-2023/solutions/files/day2input.txt", "r") as file:
    for i in range(0, 100):
        currentLine = file.readline()

        # OPEN : GET ID AND REMOVE GAME + ID TEXT

        id = ""
        
        for i in range(len(currentLine)):
            if currentLine[i].isdigit():
                id += currentLine[i]
            elif currentLine[i] == ":":
                currentLine = currentLine[i + 1:]
                break
        
        id = int(id)

        # OPEN : ADD SEMICOLON TO CURRENT LINE AND CHANGE COMMAS TO SEMICOLONS
        currentLine = currentLine.strip()
        currentLine = currentLine.replace(",", ";") + ";"

        # OPEN : ITERATE THROUGH IN SECTIONS OF {num, value, ;}

        maxRedValue = 0
        maxBlueValue = 0
        maxGreenValue = 0

        substring = ""
        for letter in currentLine:
            if letter == ";":
                # OPEN : CHECK CURRENT SUBSTRING FOR NUMBER AND COLOUR

                thisnum = ""
                thiscolour = ""

                for letter2 in substring:
                    if letter2.isdigit():
                        thisnum += letter2
                    elif not letter2.isdigit():
                        thiscolour += letter2
                
                thisnum = int(thisnum.replace(" ", ""))
                thiscolour = thiscolour.replace(" ", "")

                if thiscolour == "red" and thisnum > maxRedValue:
                    maxRedValue = thisnum
                elif thiscolour == "green" and thisnum > maxGreenValue:
                    maxGreenValue = thisnum
                elif thiscolour == "blue" and thisnum > maxBlueValue:
                    maxBlueValue = thisnum

                substring = ""
            else:
                substring += letter

        # CHECK IF GAME INSTANCE IS VALID

        # if maxRedValue <= 12 and maxGreenValue <= 13 and maxBlueValue <= 14:
            # total += id
        
        total += (maxRedValue * maxGreenValue * maxBlueValue)


    print(total)