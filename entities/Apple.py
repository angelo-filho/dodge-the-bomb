from control.constants import APPLE_SPRITE
from entities.MovingObject import MovingObject


class Apple(MovingObject):
    def __init__(self):
        super().__init__()

        self.image = APPLE_SPRITE

        self.rect = self.image.get_rect()
        self.random_pos()
