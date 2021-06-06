from control.constants import BOMB_SPRITE, BOMB_EATABLE_SPRITE
from entities.MovingObject import MovingObject


class Bomb(MovingObject):
    def __init__(self):
        super().__init__()

        self.image = BOMB_SPRITE

        self.rect = self.image.get_rect()
        self.random_pos()

        self.speed *= 0.8

        self.damage = 1

        self.eatable = False

    def update(self):
        super().update()
        self.set_color()

    def set_color(self):
        if self.eatable:
            self.image = BOMB_EATABLE_SPRITE
        else:
            self.image = BOMB_SPRITE
