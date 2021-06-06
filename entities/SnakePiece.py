import pygame


class SnakePiece:
    def __init__(self, x, y, width, height):
        self.image = None

        self.rect = pygame.Rect(x, y, width, height)
        self.last = self.rect

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
