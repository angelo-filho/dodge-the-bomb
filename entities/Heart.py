from entities.MovingObject import MovingObject
from control.constants import HEART_SPRITE


class Heart(MovingObject):
    def __init__(self):
        super().__init__()

        self.image = HEART_SPRITE

        self.rect = self.image.get_rect()

        self.random_pos()
