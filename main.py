import pygame

from control.constants import WINDOW_SIZE
from scenes.start_screen import start_screen

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Snake and Pong")

start_screen(screen)
