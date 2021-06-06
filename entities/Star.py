from entities.MovingObject import MovingObject
from control.constants import STAR_SPRITE


class Star(MovingObject):
    def __init__(self):
        super().__init__()

        self.image = STAR_SPRITE

        self.rect = self.image.get_rect()

        self.random_pos()
