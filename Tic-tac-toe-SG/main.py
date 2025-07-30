import pygame
import sys
from constrain import*
from gameplay import*


def main():
    game = TicTacToe()
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                # Check if button was clicked
                button_resetX = pygame.Rect((500, 70, 150, 40))
                button_resetO = pygame.Rect((500, 140, 180, 40))
                button_auto = pygame.Rect((500, 210, 180, 40))
                button_autoAB = pygame.Rect(500, 280, 280, 40)
                
                if button_resetX.collidepoint(mouse_pos):
                    game.reset_gameX()
                    
                elif button_resetO.collidepoint(mouse_pos):
                    game.reset_gameO()
                
                elif button_auto.collidepoint(mouse_pos):
                    game.make_ai_move()
                    
                elif button_autoAB.collidepoint(mouse_pos):
                    
                    game.make_ai_move_alpha_beta()
                    
                else:
                    # Check if a board cell was clicked
                    row, col = game.get_cell_from_pos(mouse_pos)
                    if row is not None and col is not None:
                        game.make_move(row, col)
        
        # Draw everything
        game.draw_board()
        game.draw_marks()
        reset_button_rect = game.draw_ui()
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()