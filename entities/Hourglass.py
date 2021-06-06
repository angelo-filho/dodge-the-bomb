from entities.MovingObject import MovingObject
from control.constants import YELLOW


class Hourglass(MovingObject):
    def __init__(self):
        super().__init__()

        self.image.fill(YELLOW)
