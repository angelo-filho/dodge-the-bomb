import pygame

from control.constants import BLUE, WINDOW_SIZE
from entities.Bomb import Bomb


class BigBomb(Bomb):
    def __init__(self):
        super().__init__()

        self.image = pygame.surface.Surface((60, 60))
        self.image.fill(BLUE)

        self.rect = pygame.rect.Rect(0, 0, 60, 60)
        self.random_pos()

        self.speed *= 0.6

        self.damage = 3

    def update(self, bombs, apples, max_apples):
        super().update()
        self.spawn_bombs(bombs, apples, max_apples)

    def spawn_bombs(self, group, apples, max_apples):
        if apples <= int(max_apples / 2):
            for _ in range(3):
                bomb = Bomb()
                bomb.rect.center = self.rect.center

                group.add(bomb)

            self.kill()
