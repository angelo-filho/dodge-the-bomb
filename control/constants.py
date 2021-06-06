import pygame

from os.path import join

# Window size
WINDOW_SIZE = (680, 680)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = "#656565"
RED = "#FA8383"
BLUE = "#355274"
BLUE_LIGHT = "#83C1FA"
YELLOW = "#F8FA83"

# Fonts
pygame.font.init()
SMALL_FONT = pygame.font.Font(join("assets", "fonts", "VT323-Regular.ttf"), 42)
BIG_FONT = pygame.font.Font(join("assets", "fonts", "VT323-Regular.ttf"), 102)
