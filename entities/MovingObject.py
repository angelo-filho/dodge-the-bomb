import pygame

from random import randint, choice
from math import radians, cos, sin

from control.constants import WINDOW_SIZE


class MovingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.dx = 0
        self.dy = 0

        self.random_angle()

        self.speed = 14

        self.image = pygame.Surface((20, 20))

        self.rect = pygame.Rect(0, 0, 20, 20)
        self.random_pos()

    def update(self):
        self.movement()
        self.collision_with_walls()

    def movement(self):
        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

    def collision_with_walls(self):
        if (self.rect.x <= 0 and self.dx < 0) or (self.rect.right >= WINDOW_SIZE[0] and self.dx > 0):
            self.dx *= -1
        elif (self.rect.y <= 0 and self.dy < 0) or (self.rect.bottom >= WINDOW_SIZE[0] and self.dy > 0):
            self.dy *= -1

    def random_pos(self):
        self.rect.x = randint(0, WINDOW_SIZE[0] - 20)
        self.rect.y = randint(0, WINDOW_SIZE[0] - 20)

    def random_angle(self, ):
        angle = radians(randint(30, 50))
        self.dx = cos(angle)
        self.dy = sin(angle)

        self.dx *= choice([1, -1])
        self.dy *= choice([1, -1])
