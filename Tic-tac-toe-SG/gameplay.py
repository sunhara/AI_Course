import pygame
from constrain import*
from normaliz import*

import sys
import time


# Initialize pygame
pygame.init()

# Font for text
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 36)
time_font = pygame.font.Font(None, 28)

# Set up the display
screen = pygame.display.set_mode((screenWidth, screnHeight))
pygame.display.set_caption("Tic Tac Toe")

class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.last_processing_time = 0.0  # Store last AI processing time
        self.total_processing_time = 0.0  # Store cumulative processing time
        self.move_count = 0  # Count AI moves made
        self.show_timing = True  # Only show timing when auto play is used
        
    
    def draw_board(self):
        # Fill background
        screen.fill(WHITE)
        
        pygame.draw.rect(screen,BLACK,(0,0,450,450),5)
        
        # Draw grid lines
        for i in range(1, 3):
            # Vertical lines
            pygame.draw.line(screen, BLACK, (i * 150, 0), (i * 150, 450), 1)
            # Horizontal lines
            pygame.draw.line(screen, BLACK, (0, i * 150), (450, i * 150), 1)
    
    def draw_marks(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 'X':
                    self.draw_x(row, col)
                elif self.board[row][col] == 'O':
                    self.draw_o(row, col)
    
    def draw_x(self, row, col):
        start_x = col * GRID_SIZE + SPACE
        start_y = row * GRID_SIZE + SPACE
        end_x = col * GRID_SIZE + GRID_SIZE - SPACE
        end_y = row * GRID_SIZE + GRID_SIZE - SPACE
        
        pygame.draw.line(screen, RED, (start_x, start_y), (end_x, end_y), CROSS_WIDTH)
        pygame.draw.line(screen, RED, (start_x, end_y), (end_x, start_y), CROSS_WIDTH)
    
    def draw_o(self, row, col):
        center_x = col * GRID_SIZE + GRID_SIZE // 2
        center_y = row * GRID_SIZE + GRID_SIZE // 2
        pygame.draw.circle(screen, BLUE, (center_x, center_y), CIRCLE_RADIUS, CIRCLE_WIDTH)
    
    def make_move(self, row, col):
        if self.board[row][col] == '' and not self.game_over:
            self.board[row][col] = self.current_player
            
            if self.check_winner():
                self.game_over = True
                self.winner = self.current_player
                
            elif self.is_board_full():
                self.game_over = True
                self.winner = 'Tie'
                
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return True
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        
        return False
    
    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True
    
    def reset_gameX(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.last_processing_time =0.0
        
    def reset_gameO(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'O'
        self.game_over = False
        self.winner = None
        self.last_processing_time =0.0
    
    def get_cell_from_pos(self, pos):
        x, y = pos
        if x < BOARD_SIZE and y < BOARD_SIZE:  # Only if click is within the board area
            row = y // GRID_SIZE
            col = x // GRID_SIZE
            return row, col
        else:
            return None,None
            
            
    ########
    # MinMax algorithm
    
    def evaluate_board(self, board):
        """Check if there's a winner on the given board"""
        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] != '':
                return row[0]
        
        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != '':
                return board[0][col]
        
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != '':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != '':
            return board[0][2]
        
        return None
    
    def is_full(self, board):
        """Check if the board is full"""
        for row in board:
            for cell in row:
                if cell == '':
                    return False
        return True
    
    
    def minimax(self, board, depth, is_maximizing, maximizing_player):
        """
        Minimax algorithm that works for any player
        maximizing_player: the player we're trying to find the best move for ('X' or 'O')
        """
        # Check if game is over
        winner = self.evaluate_board(board)
        
        if winner == maximizing_player:  # Maximizing player wins
            return 10 - depth
        elif winner is not None and winner != maximizing_player:  # Other player wins
            return depth - 10
        elif self.is_full(board):  # Tie
            return 0
        
        if is_maximizing:
            max_eval = -float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = maximizing_player
                        eval_score = self.minimax(board, depth + 1, False, maximizing_player)
                        board[row][col] = ''
                        max_eval = max(max_eval, eval_score)
                        # print("max_eval",max_eval)
            return max_eval
            
        else:
            min_eval = float('inf')
            # Determine the minimizing player (opponent)
            minimizing_player = 'X' if maximizing_player == 'O' else 'O'
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = minimizing_player
                        eval_score = self.minimax(board, depth + 1, True, maximizing_player)
                        board[row][col] = ''
                        min_eval = min(min_eval, eval_score)
                        # print("min_eval",min_eval)
            return min_eval
    
    def get_best_move(self):
        """Get the best move for current player using minimax algorithm"""
        best_score = -float('inf')
        best_move = None
 
    ####################################################                    
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    # Try this move
                    self.board[row][col] = self.current_player
                    # Evaluate the move (opponent plays next, so is_maximizing = False)
                    score = self.minimax(self.board, 0, False, self.current_player)
                    # Undo the move
                    self.board[row][col] = ''
                    
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        
        return best_move
    
    def make_ai_move(self):
        """Make the AI move for the current player using minimax algorithm"""
        
        if not self.game_over:
            # Start timing
            start_time = time.perf_counter()
            
            best_move = self.get_best_move()
            
            # End timing
            end_time = time.perf_counter()
            
            # Calculate and store processing time
            self.last_processing_time = end_time - start_time
            self.total_processing_time += self.last_processing_time
            self.move_count += 1
            self.show_timing = True  # Show timing after AI move is made
            
            if best_move:
                row, col = best_move
                self.make_move(row, col)
################################################################


    def minimax_alpha_beta(self, board, depth, is_maximizing, maximizing_player, alpha, beta):
        """
        Minimax algorithm with alpha-beta pruning for better performance
        maximizing_player: the player we're trying to find the best move for ('X' or 'O')
        alpha: best value that maximizer can guarantee
        beta: best value that minimizer can guarantee
        """
        # Check if game is over
        winner = self.evaluate_board(board)
        
        if winner == maximizing_player:  # Maximizing player wins
            return 10 - depth
        elif winner is not None and winner != maximizing_player:  # Other player wins
            return depth - 10
        elif self.is_full(board):  # Tie
            return 0
        
        if is_maximizing:
            max_eval = -float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = maximizing_player
                        eval_score = self.minimax_alpha_beta(board, depth + 1, False, maximizing_player, alpha, beta)
                        board[row][col] = ''
                        max_eval = max(max_eval, eval_score)
                        alpha = max(alpha, eval_score)
                        
                        # Alpha-beta pruning
                        if beta <= alpha:
                            break  # Beta cutoff
                if beta <= alpha:
                    break  # Beta cutoff at outer loop
            return max_eval
            
        else:
            min_eval = float('inf')
            # Determine the minimizing player (opponent)
            minimizing_player = 'X' if maximizing_player == 'O' else 'O'
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = minimizing_player
                        eval_score = self.minimax_alpha_beta(board, depth + 1, True, maximizing_player, alpha, beta)
                        board[row][col] = ''
                        min_eval = min(min_eval, eval_score)
                        beta = min(beta, eval_score)
                        
                        # Alpha-beta pruning
                        if beta <= alpha:
                            break  # Alpha cutoff
                if beta <= alpha:
                    break  # Alpha cutoff at outer loop
            return min_eval
    
    def get_best_move_alpha_beta(self):
        """Get the best move for current player using minimax with alpha-beta pruning"""
        best_score = -float('inf')
        best_move = None
        alpha = -float('inf')
        beta = float('inf')
        
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    # Try this move
                    self.board[row][col] = self.current_player
                    # Evaluate the move with alpha-beta pruning
                    score = self.minimax_alpha_beta(self.board, 0, False, self.current_player, alpha, beta)
                    # Undo the move
                    self.board[row][col] = ''
                    
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
                    
                    # Update alpha for root level
                    alpha = max(alpha, score)
        
        return best_move
    
    def make_ai_move_alpha_beta(self):
        """Make the AI move for the current player using minimax with alpha-beta pruning"""
        
        if not self.game_over:
            # Start timing
            start_time = time.perf_counter()
            
            best_move = self.get_best_move_alpha_beta()
            
            # End timing
            end_time = time.perf_counter()
            
            # Calculate and store processing time
            self.last_processing_time = end_time - start_time
            self.total_processing_time += self.last_processing_time
            self.move_count += 1
            self.show_timing = True  # Show timing after AI move is made
            
            if best_move:
                row, col = best_move
                self.make_move(row, col)
#################################################################
                
    def draw_processing_time(self):
        """Draw processing time information on the screen (only when show_timing is True)"""
        if not self.show_timing:
            return
            
        # Position for timing display (bottom right area)
        timing_x = 500
        timing_y = 340
        
        
        # Title
        title_text = time_font.render("AI Processing Time:", True, BLACK)
        screen.blit(title_text, (timing_x, timing_y))
        
        # Total AI move time
        if self.last_processing_time > 0:
            total_time_text = f"Total Move: {self.last_processing_time*1000:.2f} ms"
            total_time_surface = time_font.render(total_time_text, True, RED)
            screen.blit(total_time_surface, (timing_x, timing_y + 25))
        

            
    
###################################################
    def draw_ui(self):
        # Draw current player or game result

        if not self.game_over:
            text = f"Current Player: {self.current_player}"
            color = RED if self.current_player == 'X' else BLUE
        else:
            if self.winner == 'Tie':
                text = "It's a Tie!"
                color = GRAY
            else:
                text = f"Player {self.winner} Wins!"
                color = RED if self.winner == 'X' else BLUE
        
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(600,400))
        screen.blit(text_surface, text_rect)
        


        
        # Draw reset as X button
        button_resetX = pygame.Rect(500, 70, 180, 40)
        pygame.draw.rect(screen, LIGHT_GRAY, button_resetX)
        pygame.draw.rect(screen, BLACK, button_resetX, 1)
        
        button_resetX_text = small_font.render("Reset Player X", True, BLACK)
        button_resetX_text_rect = button_resetX_text.get_rect(center=button_resetX.center)
        screen.blit(button_resetX_text, button_resetX_text_rect)
        
        # Draw reset as O button
        button_resetO = pygame.Rect(500, 140, 180, 40)
        pygame.draw.rect(screen, LIGHT_GRAY, button_resetO)
        pygame.draw.rect(screen, BLACK, button_resetO, 1)
        
        button_resetO_text = small_font.render("Reset Player O", True, BLACK)
        button_resetO_text_rect = button_resetO_text.get_rect(center=button_resetO.center)
        screen.blit(button_resetO_text, button_resetO_text_rect)
        
        # Draw Auto Play button
        button_auto = pygame.Rect(500, 210, 180, 40)
        pygame.draw.rect(screen, LIGHT_GRAY, button_auto)
        pygame.draw.rect(screen, BLACK, button_auto, 1)
        
        button_auto_text = small_font.render("Auto Play", True, BLACK)
        button_auto_text_rect = button_auto_text.get_rect(center=button_auto.center)
        screen.blit(button_auto_text, button_auto_text_rect)
        
        # Draw Auto Play(alphl beta) button
        button_autoAB = pygame.Rect(500, 280, 280, 40)
        pygame.draw.rect(screen, LIGHT_GRAY, button_autoAB)
        pygame.draw.rect(screen, BLACK, button_autoAB, 1)
        
        button_autoAB_text = small_font.render("Auto Play Alpha-Beta", True, BLACK)
        button_autoAB_text_rect = button_autoAB_text.get_rect(center=button_autoAB.center)
        screen.blit(button_autoAB_text, button_autoAB_text_rect)
        
        # Draw processing time information
        self.draw_processing_time()
        
