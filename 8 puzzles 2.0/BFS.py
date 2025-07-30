from collections import deque
import copy

class BFSSolver:
    def __init__(self, initial_state, goal_state):
        """
        Initializes an instance of the BFSSolver class.

        Parameters:
        - initial_state (list): The initial state of the puzzle as a 3x3 list.
        - goal_state (list): The goal state of the puzzle as a 3x3 list.
        """        
        self.is_running = False
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.solution_path = []

    def get_blank_position(self, state):
        """
        Returns the position of the blank tile in the state.

        Parameters:
        - state (list): The current state of the puzzle as a 3x3 list.

        Returns:
        The position (row, column) of the blank tile in the state.
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)

    def is_goal_state(self, state):
        """
        Checks if the state is the goal state.

        Parameters:
        - state (list): The current state of the puzzle as a 3x3 list.

        Returns:
        True if the state is the goal state, False otherwise.
        """
        return state == self.goal_state

    def generate_next_states(self, state):
        """
        Generates the next possible states from the current state.

        Parameters:
        - state (list): The current state of the puzzle as a 3x3 list.

        Returns:
        A list of next possible states.
        """
        next_states = []
        blank_pos = self.get_blank_position(state)
        pos_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        for move in pos_moves:
            new_state = copy.deepcopy(state)
            x, y = blank_pos[0] + move[0], blank_pos[1] + move[1]

            if 0 <= x < 3 and 0 <= y < 3:
                new_state[blank_pos[0]][blank_pos[1]] = new_state[x][y]
                new_state[x][y] = 0
                next_states.append(new_state)

        return next_states

    def solve(self):
        """
        Solves the 8-puzzle using the BFS algorithm.

        Returns:
        The solution path as a list of states from the initial state to the goal state.
        """
        queue = deque([self.initial_state])
        visited_states = set()
        came_from = {}
        visited_states.add(str(self.initial_state))

        while queue:
            current_state = queue.popleft()

            if self.is_goal_state(current_state):
                self.solution_path = [current_state]
                while current_state != self.initial_state:
                    current_state = came_from[str(current_state)]
                    self.solution_path.append(current_state)

                return self.solution_path

            next_states = self.generate_next_states(current_state)

            for next_state in next_states:
                if str(next_state) not in visited_states:
                    visited_states.add(str(next_state))
                    queue.append(next_state)
                    came_from[str(next_state)] = current_state
    
    # for print out soultion              
    def print_state(self, state):
        """Print a single state in a readable format"""
        print("+-------+")
        for row in state:
            print("|", end="")
            for cell in row:
                if cell == 0:
                    print("   |", end="")  # Empty space
                else:
                    print(f" {cell} |", end="")
            print()
        print("+-------+")
       
    def print_solution_path(self):
        """Print the entire solution path step by step"""
        if not self.solution_path:
            print("No solution found or solver hasn't been run yet.")
            return
    
        print(f"Solution found in {len(self.solution_path) - 1} moves:")
        print("=" * 50)
        
        for i, state in enumerate(reversed(self.solution_path)):
            print(f"Step {i}:")
            self.print_state(state)
            if i < len(self.solution_path) - 1:
                print("    ↓")
            print()
                
    def reset(self):
        """
        Reset the solver and start a new resolution.
        """
        self.solution_path = []
        self.is_running = False