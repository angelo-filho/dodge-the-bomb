import pygame

from pygame.locals import K_a, K_s, K_w, K_d
from control.constants import WHITE, WINDOW_SIZE
from entities.SnakePiece import SnakePiece
from entities.Hourglass import Hourglass
from entities.Heart import Heart
from entities.Star import Star


class Snake:
    def __init__(self, x, y):
        self.lives = 3

        self.speed = 20

        self.body = [SnakePiece(x, y, 20, 20), SnakePiece(x - 20, y, 20, 20), SnakePiece(x - 40, y, 20, 20)]
        self.head = self.body[0]

        self.LEFT = 0
        self.RIGHT = 1
        self.UP = 2
        self.DOWN = 3

        self.current_dir = self.RIGHT

        self.VALID_KEYS = [K_a, K_s, K_w, K_d]

        self.NORMAL_STATE = 1
        self.FROZEN_TIME_STATE = 2
        self.STAR_STATE = 3

        self.state = self.NORMAL_STATE

        self.state_frames = 0
        self.MAX_STATE_FRAMES = 60

    def update(self):
        self.change_direction()

        self.body = self.move_body()
        self.move_head()

        self.collision_with_walls()

        if self.state != self.NORMAL_STATE:
            self.state_frames += 1

            if self.state_frames > self.MAX_STATE_FRAMES:
                self.state_frames = 0
                self.state = self.NORMAL_STATE

    def move_head(self):
        if self.current_dir == self.LEFT:
            self.head.rect.x -= self.speed
        elif self.current_dir == self.RIGHT:
            self.head.rect.x += self.speed
        elif self.current_dir == self.UP:
            self.head.rect.y -= self.speed
        elif self.current_dir == self.DOWN:
            self.head.rect.y += self.speed

    def move_body(self):
        support_body = [self.head]

        for i in range(1, len(self.body)):
            support_body.append(SnakePiece(self.body[i - 1].rect.x, self.body[i - 1].rect.y, 20, 20))

        return support_body

    def change_direction(self):
        keys = pygame.key.get_pressed()
        if keys[K_a] and not self.current_dir == self.RIGHT:
            self.current_dir = self.LEFT
        elif keys[K_d] and not self.current_dir == self.LEFT:
            self.current_dir = self.RIGHT
        elif keys[K_w] and not self.current_dir == self.DOWN:
            self.current_dir = self.UP
        elif keys[K_s] and not self.current_dir == self.UP:
            self.current_dir = self.DOWN

    def collision_with_walls(self):
        if self.head.rect.x <= -20 or self.head.rect.x >= WINDOW_SIZE[0] or \
                self.head.rect.y <= -20 or self.head.rect.y >= WINDOW_SIZE[0]:
            self.lives = 0

    def collision_with_bomb(self, bomb):
        for piece in self.body:
            if piece.rect.colliderect(bomb.rect) and not bomb.eatable:
                self.lives -= bomb.damage
                bomb.kill()
                break

    def collision_with_items(self, item):
        if type(item) == Hourglass:
            self.state = self.FROZEN_TIME_STATE
        elif type(item) == Heart:
            self.lives = 3
        elif type(item) == Star:
            self.state = self.STAR_STATE

        item.kill()

    def render(self, screen):
        for piece in self.body:
            pygame.draw.rect(screen, WHITE, piece.rect)
