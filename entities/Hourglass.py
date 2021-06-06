from entities.MovingObject import MovingObject
from control.constants import HOURGLASS_SPRITE


class Hourglass(MovingObject):
    def __init__(self):
        super().__init__()

        self.image = HOURGLASS_SPRITE

        self.rect = self.image.get_rect()

        self.random_pos()
