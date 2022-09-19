from collections import deque
import os

def convertStateToInteger(state):
    storage = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    val = 0

    for i in range(9):
        index = storage.index(state[i])
        val += index * factorial[i]
        storage.pop(index)

    return val

def convertIntegerToState(stateInteger):
    storage = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    state = []

    for i in range(9):
        index = stateInteger // factorial[i]
        stateInteger %= factorial[i]
        state.append(storage[index])
        storage.pop(index)

    return state

def printState(state, counter, f = None):
    if(counter == 0):
        print("Initial State", file=f)
    elif(found == counter):
        print("Iteration", counter, "/ Goal State", file=f)
    else:
        print("Iteration", counter, file=f)

    print(state[0], state[1], state[2], file=f)
    print(state[3], state[4], state[5], file=f)
    print(state[6], state[7], state[8], file=f)
    print("", file=f)

def getNextStateInteger(direction, zeroIndex):
    index = -99

    if(direction == "LEFT"):
        index = zeroIndex - 1
    elif(direction == "RIGHT"):
        index = zeroIndex + 1
    elif(direction == "TOP"):
        index = zeroIndex - 3
    elif(direction == "BOTTOM"):
        index = zeroIndex + 3

    temp = currentState[zeroIndex]
    currentState[zeroIndex] = currentState[index]
    currentState[index] = temp

    nextStateInteger = convertStateToInteger(currentState)
    if(visited[nextStateInteger] == -1):
        visited[nextStateInteger] = currentStateInteger
        queue.append(nextStateInteger)

    temp = currentState[zeroIndex]
    currentState[zeroIndex] = currentState[index]
    currentState[index] = temp

visited = [-1 for _ in range(362880)]
factorial = [40320]
output = []

for i in range(8, 0, -1):
    factorial.append(factorial[-1] // i)

initialState = [
    8, 3, 5,
    4, 1, 6,
    2, 7, 0,
]
goalState = [
    1, 2, 3,
    8, 0, 4,
    7, 6, 5,
]

goalStateInteger = convertStateToInteger(goalState)
initialStateInteger = convertStateToInteger(initialState)
queue = deque([initialStateInteger])
visited[initialStateInteger] = -2

while(len(queue) > 0):
    currentStateInteger = queue.popleft()
    if(currentStateInteger == goalStateInteger):
        break
    currentState = convertIntegerToState(currentStateInteger)
    zeroIndex = currentState.index(0)
    x = zeroIndex % 3
    y = zeroIndex // 3

    if(x > 0):
        getNextStateInteger("LEFT", zeroIndex)
    if(x < 2):
        getNextStateInteger("RIGHT", zeroIndex)
    if(y > 0):
        getNextStateInteger("TOP", zeroIndex)
    if(y < 2):
        getNextStateInteger("BOTTOM", zeroIndex)

currentStateInteger = goalStateInteger
while(currentStateInteger != -2):
    output.append(convertIntegerToState(currentStateInteger))
    currentStateInteger = visited[currentStateInteger]

filePath = "Solution.txt";
try:
    os.remove(filePath)
except:
    print("")

found = len(output) - 1
fetched = ""
for i in range(len(output)):
    fetched = output.pop()
    printState(fetched, i)
    with open("Solution.txt", "a") as f:
        printState(fetched, i, f)
