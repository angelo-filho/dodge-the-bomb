import pygame

from pygame.locals import *
from os import path
from screens.main_menu import main_menu
from control.suports import quit_game

snake_pong = pygame.image.load(path.join("assets", "sprites", "start_screen", "start_screen.png"))

message = pygame.image.load(path.join("assets", "sprites", "start_screen", "start_screen_message.png"))


def start_screen(screen):
    clock = pygame.time.Clock()

    message_alpha = 255
    message_alpha_dir = -5
    message.set_alpha(message_alpha)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            elif event.type == KEYDOWN:
                main_menu(screen)

        if (message_alpha >= 255 and message_alpha_dir > 0) or (message_alpha <= 0 and message_alpha_dir < 0):
            message_alpha_dir *= -1
        message_alpha += message_alpha_dir
        message.set_alpha(message_alpha)

        screen.fill((0, 0, 0))
        screen.blit(snake_pong, (0, 0))
        screen.blit(message, (155, 535))
        pygame.display.flip()
        clock.tick(60)
