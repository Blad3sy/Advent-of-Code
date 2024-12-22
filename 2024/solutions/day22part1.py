from math import floor

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

secrets = [int(line.strip("\n")) for line in fileLines]
for i in range(2000):
    print(i + 1, "/", 2000)
    for j in range(len(secrets)):
        secrets[j] = evolve(secrets[j])

print(sum(secrets))