def normalize_board(board,current_player):
    def find_unique_with_numpy(arrays):

        try:
            import numpy as np
            
            # Convert to numpy arrays and reshape to 1D for uniqueness check
            np_arrays = []
            for array in arrays:
                np_array = np.array(array)
                np_arrays.append(np_array.flatten())
            
            # Stack all flattened arrays
            stacked = np.vstack(np_arrays)
            
            # Find unique rows
            unique_rows, indices = np.unique(stacked, axis=0, return_index=True)
            
            # Return original 2D arrays corresponding to unique rows
            return [arrays[i] for i in sorted(indices)]
        except ImportError:
            print("NumPy not available, falling back to tuple method")
            return find_unique_2d_arrays_tuple(arrays)
            
            
    def flip_horizontal(board):
        return [row[::-1] for row in board]     

    def flip_vertical(board):
        return board[::-1]
        
    def rotate_90_clockwise(board):
        rows = len(board)
        cols = len(board[0]) if board else 0
        
        # New dimensions: cols x rows
        rotated = [[None for _ in range(rows)] for _ in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                rotated[j][rows - 1 - i] = board[i][j]
        
        return rotated
        
    def rotate_180(board):
        rows = len(board)
        cols = len(board[0]) if board else 0
        
        rotated = [[None for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                rotated[rows - 1 - i][cols - 1 - j] = board[i][j]
        
        return rotated
    
    all_collection = []
    
    for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    # Try this move
                    board[row][col] = current_player
                    all_collection.append(board)
                    all_collection.append(flip_horizontal(board))
                    all_collection.append(flip_vertical(board))
                    # Undo the move
                    board[row][col] = ''
                    
                    
    unique_collec = find_unique_with_numpy(all_collection)
        
    return unique_collec
