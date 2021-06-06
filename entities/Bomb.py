from control.constants import BLUE, BLUE_LIGHT
from entities.MovingObject import MovingObject


class Bomb(MovingObject):
    def __init__(self):
        super().__init__()

        self.image.fill(BLUE)

        self.speed *= 0.8

        self.damage = 1

        self.eatable = False

    def update(self):
        super().update()
        self.set_color()

    def set_color(self):
        if self.eatable:
            self.image.fill(BLUE_LIGHT)
        else:
            self.image.fill(BLUE)
