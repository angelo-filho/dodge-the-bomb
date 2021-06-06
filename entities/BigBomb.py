import pygame

from control.constants import BOMB_SOUND, BOMB_SPRITE
from entities.Bomb import Bomb
from entities.MovingObject import MovingObject


class BigBomb(MovingObject):
    def __init__(self):
        super().__init__()

        self.image = pygame.transform.scale2x(BOMB_SPRITE)

        self.rect = self.image.get_rect()
        self.random_pos()

        self.speed *= 0.6

        self.damage = 3

        self.eatable = False

    def update(self, bombs, apples, max_apples):
        super().update()
        self.spawn_bombs(bombs, apples, max_apples)

    def spawn_bombs(self, group, apples, max_apples):
        if apples <= int(max_apples / 2):
            BOMB_SOUND.play()
            for _ in range(3):
                bomb = Bomb()
                bomb.rect.center = self.rect.center

                group.add(bomb)

            self.kill()
