import sys
import pygame


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, False, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

    return text_rect


def quit_game():
    pygame.quit()
    sys.exit()
