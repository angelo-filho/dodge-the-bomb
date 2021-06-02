import pygame

from os.path import join

# Colors
WHITE = (255, 255, 255)
RED = "#FA8383"

#Fonts
pygame.font.init()
small_font = pygame.font.Font(join("assets", "fonts", "VT323-Regular.ttf"), 42)
