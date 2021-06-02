import sys

import pygame
from pygame.locals import *

from os import path

pygame.init()

screen = pygame.display.set_mode((680, 680))
pygame.display.set_caption("Snake and Pong")
clock = pygame.time.Clock()

snake_pong = pygame.image.load(path.join("assets", "sprites", "start_screen", "start_screen.png"))

message = pygame.image.load(path.join("assets", "sprites", "start_screen", "start_screen_message.png"))
message_alpha = 255
message_alpha_dir = -5
message.set_alpha(message_alpha)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            pass

    if (message_alpha >= 255 and message_alpha_dir > 0) or (message_alpha <= 0 and message_alpha_dir < 0):
        message_alpha_dir *= -1
    message_alpha += message_alpha_dir
    message.set_alpha(message_alpha)

    screen.fill((0, 0, 0))
    screen.blit(snake_pong, (0, 0))
    screen.blit(message, (130, 535))
    pygame.display.flip()
    clock.tick(60)
