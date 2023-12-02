def convertWordToNum (word):
    word = word.lower()

    if word == "one" or word == "1": return "1"
    elif word == "two" or word == "2": return "2"
    elif word == "three" or word == "3": return "3"
    elif word == "four" or word == "4": return "4"
    elif word == "five" or word == "5": return "5"
    elif word == "six" or word == "6": return "6"
    elif word == "seven" or word == "7": return "7"
    elif word == "eight" or word == "8": return "8"
    elif word == "nine" or word == "9": return "9"
    else: return None

    # cba to update python lmao

total = 0

with open("Advent-of-Code-2023/solutions/files/day1input.txt", "r") as txtfile:
    for i in range(0, 1000):
        lineRead = txtfile.readline()
        nums = ""
        for i in range(0, len(lineRead)):
            lineReadSubs = [lineRead[i], lineRead[i:i+3], lineRead[i:i+4], lineRead[i:i+5]]
            for t in range(0, 4):
                lineReadSubs[t] = convertWordToNum(lineReadSubs[t])
            for sub in lineReadSubs:
                if sub != None: nums += sub
        if len(nums) == 1:
            nums = nums[0] + nums[0]
        else:
            nums = nums[0] + nums[-1]

        total += int(nums)

print(total)