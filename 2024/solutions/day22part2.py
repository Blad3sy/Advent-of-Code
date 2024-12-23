from math import floor
from datetime import datetime

with open("2024/files/day22input.txt") as file:
    fileLines = file.readlines()

def mix(num, secret): return num ^ secret
def prune(secret): return secret % 16777216

def evolve(secret):
    mult = secret * 64
    secret = mix(mult, secret)
    secret = prune(secret)

    div = secret / 32
    div = int(floor(div))
    secret = mix(div, secret)
    secret = prune(secret)

    mult = secret * 2048
    secret = mix(mult, secret)
    secret = prune(secret)

    return secret

# https://stackoverflow.com/questions/17870544/find-starting-and-ending-indices-of-sublist-in-list
def find_sub_list(sl,l):
    sll=len(sl)
    for ind in (i for i,e in enumerate(l) if e==sl[0]):
        if l[ind:ind+sll]==sl:
            return ind+sll-1

    raise ValueError()

secrets = [int(line.strip("\n")) for line in fileLines]
changes = {}
prices = {}
nines = {}
for j in range(len(secrets)): 
    changes[j] = [0]
    prices[j] = [0]
    nines[j] = []

for i in range(2000):
    for j in range(len(secrets)):
        prev = int(str(secrets[j])[-1])
        secrets[j] = evolve(secrets[j])

        price = int(str(secrets[j])[-1])
        if price == 9 and i >= 4: nines[j].append(i)
        changes[j].append(price - prev)
        prices[j].append(price)

maxsum = 0
posibs = []
for i in range(-9, 10):
    for j in range(-9, 10):
        for a in range(-9, 10):
            for b in range(-9, 10):
                posib = [i, j, a, b]
                curChange = 0
                isValid = True
                for char in posib:
                    curChange += char
                    if curChange < -9 or curChange > 9: isValid = False
                if isValid: posibs.append(posib)

starttime = datetime.now()
times = []
count = 1
length = len(posibs)
for changeStr in posibs:
    start = datetime.now()
    print(count, "/", length, end = " - ")
    total = 0
    for a in range(len(secrets)):
        try:
            index3 = find_sub_list(changeStr, changes[a])
            total += prices[a][index3]
        except ValueError: pass
    if total > maxsum: maxsum = total
    elapsed = (datetime.now() - start).total_seconds()
    times.append(elapsed)
    print(f"Estimated time remaining: {round(((sum(times) / len(times)) * (length - count)), 2)} seconds")
    count += 1

print(maxsum)
print((datetime.now() - starttime).total_seconds())

# BRUTE FORCE ALWAYS WORKS!!!!!!! 12144 SECONDS TO RUN!!!!!!!!