from control.constants import RED
from entities.MovingObject import MovingObject


class Apple(MovingObject):
    def __init__(self):
        super().__init__()

        self.image.fill(RED)
