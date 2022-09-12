from collections import deque

factorial = [40320]

for i in range(8, 0, -1):
    factorial.append(factorial[-1] // i)

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

def printState(stateInteger):
    state = convertIntegerToState(stateInteger)
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])

visited = [-1 for _ in range(362880)]
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
        temp = currentState[zeroIndex]
        currentState[zeroIndex] = currentState[zeroIndex - 1]
        currentState[zeroIndex - 1] = temp

        nextStateInteger = convertStateToInteger(currentState)
        if(visited[nextStateInteger] == -1):
            visited[nextStateInteger] = currentStateInteger
            queue.append(nextStateInteger)

        temp = currentState[zeroIndex]
        currentState[zeroIndex] = currentState[zeroIndex - 1]
        currentState[zeroIndex - 1] = temp

    if(x < 2):
        temp = currentState[zeroIndex]
        currentState[zeroIndex] = currentState[zeroIndex + 1]
        currentState[zeroIndex + 1] = temp

        nextStateInteger = convertStateToInteger(currentState)
        if(visited[nextStateInteger] == -1):
            visited[nextStateInteger] = currentStateInteger
            queue.append(nextStateInteger)

        temp = currentState[zeroIndex]
        currentState[zeroIndex] = currentState[zeroIndex + 1]
        currentState[zeroIndex + 1] = temp

    if(y > 0):
        temp = currentState[zeroIndex]
        currentState[zeroIndex] = currentState[zeroIndex - 3]
        currentState[zeroIndex - 3] = temp

        nextStateInteger = convertStateToInteger(currentState)
        if(visited[nextStateInteger] == -1):
            visited[nextStateInteger] = currentStateInteger
            queue.append(nextStateInteger)

        temp = currentState[zeroIndex]
        currentState[zeroIndex] = currentState[zeroIndex - 3]
        currentState[zeroIndex - 3] = temp

    if(y < 2):
        temp = currentState[zeroIndex]
        currentState[zeroIndex] = currentState[zeroIndex + 3]
        currentState[zeroIndex + 3] = temp

        nextStateInteger = convertStateToInteger(currentState)
        if(visited[nextStateInteger] == -1):
            visited[nextStateInteger] = currentStateInteger
            queue.append(nextStateInteger)

        temp = currentState[zeroIndex]
        currentState[zeroIndex] = currentState[zeroIndex + 3]
        currentState[zeroIndex + 3] = temp

currentStateInteger = goalStateInteger
while(currentStateInteger != -2):
    # print(currentStateInteger)
    printState(currentStateInteger)
    print("")
    currentStateInteger = visited[currentStateInteger]
