from entities.MovingObject import MovingObject
from control.constants import YELLOW


class Heart(MovingObject):
    def __init__(self):
        super().__init__()

        self.image.fill(YELLOW)
