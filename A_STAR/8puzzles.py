from queue import PriorityQueue

initial_state = [1,2,5,
3,4,0,
6,7,8]
goal_state = [1,2,3,
4,5,6,
7,8,0]
n = 3

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
    return

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
        
    def Manhattan_Distance(self ,n): 
        self.heuristic = 0
        for i in range(1 , n*n):
            distance = abs(self.state.index(i) - self.goal.index(i))
            
            self.heuristic = self.heuristic + distance/n + distance%n

        self.greedy_evaluation = self.heuristic    
        self.AStar_evaluation = self.heuristic + self.cost
        
        return( self.greedy_evaluation, self.AStar_evaluation)


    @staticmethod
    
    def available_moves(x,n): 
        moves = ['Left', 'Right', 'Up', 'Down']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n-1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n*n - 1:
            moves.remove('Down')

        return moves

    def expand(self , n): 
        x = self.state.index(0)
        moves = self.available_moves(x,n)
        
        children = []
        for direction in moves:
            temp = self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
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


AStar_solution = AStar_search(initial_state, goal_state, 3)
for state in AStar_solution[0]:
    print("---------------------")
    print("|   -------------   |")
    print("|   |", state[0], "|", state[1], "|", state[2], "|   |")
    print("|   -------------   |")
    print("|   |", state[3], "|", state[4], "|", state[5], "|   |")
    print("|   -------------   |")
    print("|   |", state[6], "|", state[7], "|", state[8], "|   |")
    print("|   -------------   |")
    print("---------------------")