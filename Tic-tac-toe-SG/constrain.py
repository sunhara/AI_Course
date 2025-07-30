import pygame

# Screen
screenWidth = 800
screnHeight = 450


# Constants
WIDTH = 450
HEIGHT = 450
BOARD_SIZE = 450
GRID_SIZE = 150
LINE_WIDTH = 12
CIRCLE_RADIUS = 50
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)




# Images
X_IMAGE = pygame.transform.scale(pygame.image.load("X.png"), (150, 150))
O_IMAGE = pygame.transform.scale(pygame.image.load("O.png"), (150, 150))


# declaring the global variables

# for storing the 'x' or 'o'
# value as character
XO = 'x'

# storing the winner's value at
# any instant of code
winner = None
# to check if the game is a draw
draw = None


# setting up a 3 * 3 board in canvas
board = [[None]*3, [None]*3, [None]*3]