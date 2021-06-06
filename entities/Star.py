from entities.MovingObject import MovingObject
from control.constants import GRAY


class Star(MovingObject):
    def __init__(self):
        super().__init__()

        self.image.fill(GRAY)