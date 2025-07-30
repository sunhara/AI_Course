import pygame

from tkinter import Tk, filedialog
from tkinter.messagebox import showerror
from gameplay import Game
from constants import *

from AS import AStarSolver
from BFS import BFSSolver
from DFS import DFSSolver

from buttons import*


# Initialize Pygame
pygame.init()

# Set the window caption
pygame.display.set_caption('8-PUZZLE')

# Initialize the clock
CLOCK = pygame.time.Clock()

# Create a new game instance
game = Game()

# Create 3 solvers instance
resolver_ia = AStarSolver(game.initial_state, game.goal_state)
resolver_bfs = BFSSolver(game.initial_state, game.goal_state)
resolver_dfs = DFSSolver(game.initial_state, game.goal_state)

# Create buttons
solve_button1 = Button(x=500,y=20,width=180,height=60,text="A* Solver",
color=BUTTON_COLOR,hover_color=BUTTON_HOVER_COLOR,text_color=BUTTON_TEXT_COLOR)

solve_button2 = Button(x=500,y=90,width=180,height=60,text="BFS Solver",
color=BUTTON_COLOR,hover_color=BUTTON_HOVER_COLOR,text_color=BUTTON_TEXT_COLOR)

solve_button3 = Button(x=500,y=160,width=180,height=60,text="DFS Solver",
color=BUTTON_COLOR,hover_color=BUTTON_HOVER_COLOR,text_color=BUTTON_TEXT_COLOR)

reset_button = Button(x=500,y=230,width=180,height=60,text="Reset",
color=BUTTON_COLOR,hover_color=BUTTON_HOVER_COLOR,text_color=BUTTON_TEXT_COLOR)




# Main game loop
while True:
    # Fill the screen with the background color
    SCREEN.fill(BACKGROUND)
    
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the window is closed
            pygame.quit()
            sys.exit()
        # all the mouse click events
        if reset_button.is_clicked(event):
            print("Game Reset!")
            game.reset()
        
        if solve_button1.is_clicked(event) and not game.solved and not resolver_ia.is_running:
            print("A* Solving")
            solution_path = resolver_ia.solve()
            resolver_ia.is_running = True
            resolver_ia.print_solution_path()
        
        if solve_button2.is_clicked(event) and not game.solved and not resolver_bfs.is_running:
            print("BFS Solving")
            solution_path = resolver_bfs.solve()
            resolver_bfs.is_running = True
            resolver_bfs.print_solution_path()
        
        if solve_button3.is_clicked(event) and not game.solved and not resolver_dfs.is_running:
            print("DFS Solving")
            solution_path = resolver_dfs.solve()
            resolver_dfs.is_running = True
            resolver_dfs.print_solution_path() 
         

        if event.type == pygame.MOUSEBUTTONDOWN and not game.solved:
            # Move a tile when a mouse button is clicked, if the game is not already solved
            pos_x = event.pos[1] // (WIDTH // 3 - SPACECING)
            pos_y = event.pos[0] // (HEIGHT // 3 - SPACECING)
            game.move_tile(pos_x, pos_y)
        
        # all the keyboard press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Reset the game if ENTER key is pressed
                # Generate a new game (new state)
                game.reset()
            
                resolver_ia = AStarSolver(game.initial_state, game.goal_state)
                resolver_ia.reset()
                
                resolver_bfs = BFSSolver(game.initial_state, game.goal_state)
                resolver_bfs.reset()
                
                resolver_dfs = DFSSolver(game.initial_state, game.goal_state)
                resolver_dfs.reset()

            if event.key == pygame.K_ESCAPE:
                # Quit the game if ESCAPE key is pressed
                pygame.quit()
                sys.exit()
                

            if event.key == pygame.K_SPACE and not game.solved and not resolver_ia.is_running:
                # Solve the puzzle if SPACE key is pressed and the game is not already solved or the solver is already running
                solution_path = resolver_ia.solve()
                resolver_ia.is_running = True
                resolver_ia.print_solution_path()
                
            if event.key == pygame.K_b and not game.solved and not resolver_bfs.is_running:
                # Solve the puzzle if SPACE key is pressed and the game is not already solved or the solver is already running
                solution_path = resolver_bfs.solve()
                resolver_bfs.is_running = True
                resolver_bfs.print_solution_path()


    if resolver_ia.solution_path:
        # Update the game board with the next state from the solution path, with a delay
        game.initial_state = solution_path.pop()
        pygame.time.wait(100)
    
    if resolver_bfs.solution_path:
        # Update the game board with the next state from the solution path, with a delay
        game.initial_state = solution_path.pop()
        pygame.time.wait(100) 
        
    if resolver_dfs.solution_path:
        game.initial_state = solution_path.pop(0)
        pygame.time.wait(100)
        
        
    
    # Draw the game board
    game.draw_board()
    
    
    if game.is_solved():
        # Draw the winning message if the game is solved
        game.draw_win()

    # Update the display
    solve_button1.draw(SCREEN)
    solve_button2.draw(SCREEN)
    solve_button3.draw(SCREEN)
    reset_button.draw(SCREEN)

    
    move_text = f"Moves: {game.move_count}"
    font = pygame.font.Font('freesansbold.ttf', 26)
    text_surface = font.render(move_text, True, WHITE)
    SCREEN.blit(text_surface,(500,320))


    
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    CLOCK.tick(60)
    
    # print(game.move_count)