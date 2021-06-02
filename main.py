import pygame
from screens.start_screen import start_screen

pygame.init()

screen = pygame.display.set_mode((680, 680))
pygame.display.set_caption("Snake and Pong")

start_screen(screen)
