from queue import PriorityQueue
import os

def AStar_search(given_state, goal_state, n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    root.goal = goal_state
    evaluation = root.Manhattan_Distance(n)
    frontier.put((evaluation[1], counter, root))
    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        if current_node.check_goal():
            return current_node.solution(), len(explored)
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Manhattan_Distance(n)
                frontier.put((evaluation[1], counter, child))

class State:
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0] 
    greedy_evaluation = None
    AStar_evaluation = None
    heuristic = None

    def __init__(self, state, parent, direction, depth, cost):
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth
        if parent:
            self.cost = parent.cost + cost
        else:
            self.cost = cost

    def check_goal(self): 
        if self.state == self.goal:
            return True
        return False

    def Manhattan_Distance(self, n):
        self.heuristic = 0
        for i in range(1, n * n):
            distance = abs(self.state.index(i) - self.goal.index(i))
            self.heuristic = self.heuristic + distance / n + distance % n
        self.greedy_evaluation = self.heuristic
        self.AStar_evaluation = self.heuristic + self.cost
        return(self.greedy_evaluation, self.AStar_evaluation)

    @staticmethod
    def available_moves(x, n): 
        moves = ["Left", "Right", "Up", "Down"]
        if x % n == 0:
            moves.remove("Left")
        if x % n == n - 1:
            moves.remove("Right")
        if x - n < 0:
            moves.remove("Up")
        if x + n > n * n - 1:
            moves.remove("Down")
        return moves

    def expand(self, n): 
        x = self.state.index(0)
        moves = self.available_moves(x, n)
        children = []
        for direction in moves:
            temp = self.state.copy()
            if direction == "Left":
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == "Right":
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == "Up":
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == "Down":
                temp[x], temp[x + n] = temp[x + n], temp[x]
            children.append(State(temp, self, self.state, self.depth + 1, 1))
        return children

    def solution(self):
        solution = []
        solution.append(self.direction)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.direction)
        solution = solution[:-1]
        solution.reverse()
        return solution

def parseInput(userInput):
    state = userInput.split(" ")

    for i in range(len(state)):
        state[i] = int(state[i])

    return state

def printState(state, counter, f = None):
    print("---------------------", file=f)

    if(counter == 0):
        print("|   Initial State   |", file=f)
    else:
        print("| Iterations", ("%06d" % counter), "|", file=f)
        if(found == counter):
            print("---------------------", file=f)
            print("|    Goal/Result    |", file=f)

    print("---------------------", file=f)
    print("|   -------------   |", file=f)
    print("|   |", state[0], "|", state[1], "|", state[2], "|   |", file=f)
    print("|   -------------   |", file=f)
    print("|   |", state[3], "|", state[4], "|", state[5], "|   |", file=f)
    print("|   -------------   |", file=f)
    print("|   |", state[6], "|", state[7], "|", state[8], "|   |", file=f)
    print("|   -------------   |", file=f)

    if(found == counter):
        print("---------------------", end="\n", file=f)
    else:
        print("---------------------", file=f)
        print("          |          ", file=f)
        print("          V          ", end="\n", file=f)

i = 0
n = 3

# Initial State Example: 1 2 5 3 4 0 6 7 8
# Goal State Example: 1 2 3 4 5 6 7 8 0

initial_state = parseInput(input("Enter initial state (Separated by whitespace): "))
goal_state = parseInput(input("Enter goal state (Separated by whitespace): "))

# initial_state = [
#     1, 2, 5,
#     3, 4, 0,
#     6, 7, 8
# ]
# goal_state = [
#     1, 2, 3,
#     4, 5, 6,
#     7, 8, 0
# ]

AStar_solution = AStar_search(initial_state, goal_state, n)
AStar_solution[0].append(goal_state)
found = len(AStar_solution[0]) - 1

filePath = "Solution.txt";
try:
    os.remove(filePath)
except:
    pass

for state in AStar_solution[0]:
    printState(state, i)
    with open("Solution.txt", "a") as f:
        printState(state, i, f)
    i += 1
