import z3 
# Thank god for this!

with open("Advent-of-Code-2023/2023/files\day24input.txt", "r") as file:
    fileLines = file.readlines()

posray = []
velray = []

for line in fileLines:
    line = line.strip().split("@")
    line[0] = line[0].strip().split(",")
    line[1] = line[1].strip().split(",")

    line[0] = [int(value) for value in line[0]]
    line[1] = [int(value) for value in line[1]]

    posray.append(line[0])
    velray.append(line[1])

# I'd like to apologise for this solution specifically - it's very cheaty but I had... zero idea how to go about this one. I looked online
# for any semblance of an idea of anything (the only thing I had was trying every possible combination of hailstone orders... there are
# 3.0605751221 x10^614 different possible orders (300!). Nope. When looking I found out about a lovely tool called z3 Solver, created
# by Microsoft for exactly this sort of situation.
# https://ericpony.github.io/z3py-tutorial/guide-examples.htm , https://github.com/Z3Prover/z3
# I decided, at my wit's end, to use this. Because I was absolutely clueless in solving this and just followed a tutorial on how to use z3,
# I'm trying to explain how this program works so that I can say I solved this part legit - which I don't really think I can claim I did.
# I read a lot of z3 documentation for this, and still had to refer to https://gist.github.com/hcs64/dd4089b45cec036ae8015eed12b93e80
# in the end because I couldn't get it quite right.

# Defines the variables xPosition, yPosition, zPosition (all 3d coords), xVelocity, yVelocity, zVelocity (all 3d vector components)
x, y, z, vx, vy, vz = z3.Reals("x y z vx vy vz")

# Initialises the solver which does all the heavy lifting
solver = z3.Solver()

# Loops through each position and velocity
for i in range(len(posray)):
    # Grabs the xPosition, yPosition, zPosition, xVelocity, yVelocity and zVelocity of the given hailstone from the input
    thisx, thisy, thisz = posray[i]
    thisvx, thisvy, thisvz = velray[i]

    # Creates a seperate time variable for each hailstone
    thisTime = z3.Real(f"Time : {i}")

    # Adds constraints : x, y, z, vx, vy, vz must all equal their equivalents at each time
    # This confuses me ; it was what I needed help with in the end.
    # I think what it basically does is says that the rock's position must equal the position of each hailstone at each given time?
    # This position is of course calculated using the formula ' original + velocity * time elapsed '
    solver.add(thisx + thisvx * thisTime == x + vx * thisTime)
    solver.add(thisy + thisvy * thisTime == y + vy * thisTime)
    solver.add(thisz + thisvz * thisTime == z + vz * thisTime)

# Outputs whether the problem is solvable or not : sat = solvable (z3 satisfied the set of constraints).
print(solver.check())

# Creates a dictionary (?) for which z3 assigns all unassigned variables according to the constraints - in this case, all of them!
model = solver.model()

# Outputs results from the given dict (here, the values of all the variables at time = 1)
print(model[x], model[y], model[z], "|", model[vx], model[vy], model[vz], "|", model[thisTime])

# Outputs the x,y,z input to get the actual puzzle solution
print(model[x] + model[y] + model[z])

# Outputs the actual puzzle solution so I can copy/paste it into the website.
print(229734616875628 + 192049388333190 + 146602352667782)

# Side note : from what I can tell, nearly everyone solved today's part 2 with some sort of maths solver ; z3, Mathematica and Wolfram Alpha were most common.