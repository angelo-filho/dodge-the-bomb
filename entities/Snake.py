from pygame.locals import K_a, K_s, K_w, K_d
from control.constants import *
from entities.SnakePiece import SnakePiece
from entities.Hourglass import Hourglass
from entities.Heart import Heart
from entities.Star import Star


class Snake:
    def __init__(self, x, y):
        self.lives = 3

        size = 30

        self.speed = size

        self.body = [SnakePiece(x, y, size, size), SnakePiece(x - size, y, size, size),
                     SnakePiece(x - size * 2, y, size, size)]
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
        self.START_STATE = 4

        self.state = self.START_STATE

        self.state_frames = 0
        self.MAX_STATE_FRAMES = 46

    def update(self):
        self.change_direction()

        self.body = self.move_body()
        self.move_head()

        self.collision_with_walls()

        if self.state != self.NORMAL_STATE:

            if self.state == self.START_STATE:
                self.state_frames += 10
            else:
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
            HURT_SOUND.play()
            self.lives = 0

    def collision_with_bomb(self, bomb):
        for piece in self.body:
            if piece.rect.colliderect(bomb.rect) and not bomb.eatable and self.state != self.START_STATE:
                BOMB_SOUND.play()
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

        self.state_frames = 0
        ITEM_SOUND.play()
        item.kill()

    def set_head_image(self):
        if self.current_dir == self.LEFT:
            self.head.image = SNAKE_HEAD_HORIZONTAL
        elif self.current_dir == self.RIGHT:
            self.head.image = pygame.transform.rotate(SNAKE_HEAD_HORIZONTAL, 180)
        elif self.current_dir == self.UP:
            self.head.image = SNAKE_HEAD_VERTICAL
        elif self.current_dir == self.DOWN:
            self.head.image = pygame.transform.rotate(SNAKE_HEAD_VERTICAL, 180)

    def set_body_image(self):
        for i in range(1, len(self.body) - 1):
            self.body[i].image = SNAKE_BODY

    def set_tail_image(self):
        if self.body[-2].rect.y < self.body[-1].rect.y:
            self.body[-1].image = pygame.transform.rotate(SNAKE_TAIL_VERTICAL, 180)
        elif self.body[-2].rect.y > self.body[-1].rect.y:
            self.body[-1].image = SNAKE_TAIL_VERTICAL
        else:
            if self.body[-2].rect.x > self.body[-1].rect.x:
                self.body[-1].image = pygame.transform.rotate(SNAKE_TAIL_HORIZONTAL, 180)
            elif self.body[-2].rect.x < self.body[-1].rect.x:
                self.body[-1].image = SNAKE_TAIL_HORIZONTAL

    def render(self, screen):
        self.set_head_image()
        self.set_body_image()
        self.set_tail_image()

        for piece in self.body:
            screen.blit(piece.image, piece.rect)
