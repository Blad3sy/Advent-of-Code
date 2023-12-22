import sys

with open("Advent-of-Code-2023/2023/files\day17input.txt", "r") as file:
    grid = file.readlines()

    for i in range(len(grid)):
        grid[i] = [int(value) for value in grid[i] if value != "\n"]

def moveAndAddState(cost, x, y, dx, dy, distance):
    x += dx
    y += dy

    if x < 0 or y < 0 or x >= width or y >= height:
        return
    
    newCost = cost + grid[y][x]

    if x == endx and y == endy:
        print(f"> {newCost} <")
        sys.exit(0)
    
    state = (x, y, dx, dy, distance)
    if state not in seenCostsByState:
        stateQueuesByCost.setdefault(newCost, []).append(state)
        seenCostsByState[state] = newCost


height = len(grid)
width = len(grid[0])

endx = width - 1
endy = height - 1

stateQueuesByCost = {}
seenCostsByState = {}

moveAndAddState(0, 0, 0, 1, 0, 1)
moveAndAddState(0, 0, 0, 0, 1, 1)

while True:
    currentCost = min(stateQueuesByCost.keys())

    nextStates = stateQueuesByCost.pop(currentCost)

    for state in nextStates:
        (x, y, dx, dy, distance) = state

        moveAndAddState(currentCost, x, y, dy, -dx, distance=1)
        moveAndAddState(currentCost, x, y, -dy, dx, distance=1)

        if distance < 3:
            moveAndAddState(currentCost, x, y, dx, dy, distance + 1)