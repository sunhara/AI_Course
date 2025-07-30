import copy

class DFSSolver:
    def __init__(self, initial_state, goal_state, max_depth=50):
        """
        Initializes an instance of the IterativeDFSSolver class.

        Parameters:
        - initial_state (list): The initial state of the puzzle as a 3x3 list.
        - goal_state (list): The goal state of the puzzle as a 3x3 list.
        - max_depth (int): Maximum depth to search (prevents infinite loops)
        """        
        self.is_running = False
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.solution_path = []
        self.max_depth = max_depth

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
        Solves the 8-puzzle using iterative DFS with a stack.
        
        Stack contains tuples of: (current_state, path_to_current_state, visited_states_in_path)

        Returns:
        The solution path as a list of states from the initial state to the goal state.
        """
        # Initialize stack with initial state
        # Each stack item: (state, path, visited_in_current_path)
        stack = [(self.initial_state, [self.initial_state], {str(self.initial_state)})]
        
        nodes_explored = 0  # For debugging/statistics
        
        while stack:
            # Pop from stack (LIFO - Last In, First Out)
            current_state, path, visited_in_path = stack.pop()
            nodes_explored += 1
            
            # Check depth limit to prevent infinite search
            if len(path) > self.max_depth:
                continue
                
            # Check if we've reached the goal
            if self.is_goal_state(current_state):
                self.solution_path = path
                print(f"Solution found! Nodes explored: {nodes_explored}")
                return self.solution_path

            # Generate all possible next states
            next_states = self.generate_next_states(current_state)
            
            # Add valid next states to stack
            for next_state in next_states:
                state_str = str(next_state)
                
                # Only add if not visited in current path (prevents cycles)
                if state_str not in visited_in_path:
                    # Create new path and visited set for this branch
                    new_path = path + [next_state]
                    new_visited = visited_in_path.copy()
                    new_visited.add(state_str)
                    
                    # Push to stack for exploration
                    stack.append((next_state, new_path, new_visited))

        print(f"No solution found within depth {self.max_depth}. Nodes explored: {nodes_explored}")
        return None

    # def solve_with_visited_global(self):
    #     """
    #     Alternative iterative DFS that uses global visited set (like BFS).
    #     This version is more memory efficient but may miss some solutions.
    #     """
    #     stack = [self.initial_state]
    #     visited_states = set()
    #     came_from = {}
    #     visited_states.add(str(self.initial_state))
        
    #     nodes_explored = 0
        
    #     while stack:
    #         current_state = stack.pop()  # LIFO for DFS
    #         nodes_explored += 1
            
    #         if self.is_goal_state(current_state):
    #             # Reconstruct path
    #             self.solution_path = [current_state]
    #             while current_state != self.initial_state:
    #                 current_state = came_from[str(current_state)]
    #                 self.solution_path.append(current_state)
                
    #             self.solution_path.reverse()
    #             print(f"Solution found! Nodes explored: {nodes_explored}")
    #             return self.solution_path

    #         next_states = self.generate_next_states(current_state)
            
    #         for next_state in next_states:
    #             state_str = str(next_state)
    #             if state_str not in visited_states:
    #                 visited_states.add(state_str)
    #                 stack.append(next_state)
    #                 came_from[state_str] = current_state

    #     print(f"No solution found. Nodes explored: {nodes_explored}")
    #     return None
        
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
        
        for i, state in enumerate(self.solution_path):
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