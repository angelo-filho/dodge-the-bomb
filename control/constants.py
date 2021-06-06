import pygame

from os.path import join

# Window size
WINDOW_SIZE = (680, 680)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = "#656565"
RED = "#FA8383"
BLUE = "#355274"
BLUE_LIGHT = "#83C1FA"
YELLOW = "#F8FA83"

# Fonts
pygame.font.init()
SMALL_FONT = pygame.font.Font(join("assets", "fonts", "VT323-Regular.ttf"), 42)
BIG_FONT = pygame.font.Font(join("assets", "fonts", "VT323-Regular.ttf"), 102)

# Sounds
pygame.mixer.init()
SELECT_SOUND = pygame.mixer.Sound(join("assets", "sounds", "select_sound.wav"))
COUNT_SOUND = pygame.mixer.Sound(join("assets", "sounds", "count_sound.wav"))
HURT_SOUND = pygame.mixer.Sound(join("assets", "sounds", "hurt_sound.wav"))
APPLE_SOUND = pygame.mixer.Sound(join("assets", "sounds", "apple_sound.wav"))
BOMB_SOUND = pygame.mixer.Sound(join("assets", "sounds", "bomb_sound.wav"))
ITEM_SOUND = pygame.mixer.Sound(join("assets", "sounds", "item_sound.wav"))

# Images
SNAKE_HEAD_VERTICAL = pygame.image.load(join("assets", "sprites", "snake", "snake_head_vertical.png"))
SNAKE_HEAD_HORIZONTAL = pygame.image.load(join("assets", "sprites", "snake", "snake_head_horizontal.png"))
SNAKE_TAIL_VERTICAL = pygame.image.load(join("assets", "sprites", "snake", "snake_tail_vertical.png"))
SNAKE_TAIL_HORIZONTAL = pygame.image.load(join("assets", "sprites", "snake", "snake_tail_horizontal.png"))
SNAKE_BODY = pygame.image.load(join("assets", "sprites", "snake", "snake_body.png"))

APPLE_SPRITE = pygame.image.load(join("assets", "sprites", "items", "apple.png"))
BOMB_SPRITE = pygame.image.load(join("assets", "sprites", "items", "bomb.png"))
BOMB_EATABLE_SPRITE = pygame.image.load(join("assets", "sprites", "items", "bomb_eatable.png"))
HOURGLASS_SPRITE = pygame.image.load(join("assets", "sprites", "items", "hourglass.png"))
HEART_SPRITE = pygame.image.load(join("assets", "sprites", "items", "heart.png"))
STAR_SPRITE = pygame.image.load(join("assets", "sprites", "items", "star.png"))
