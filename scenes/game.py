import pygame.mouse
from pygame.locals import *

from random import choice

from control.constants import *
from control.supports import quit_game, draw_text
from entities.Snake import Snake
from entities.Apple import Apple
from entities.Bomb import Bomb
from entities.BigBomb import BigBomb
from entities.Hourglass import Hourglass
from entities.Heart import Heart
from entities.Snake import Star

# Setting up game states
NORMAL_STATE = 0
PAUSE_STATE = 1
START_STATE = 2
GAME_OVER_STATE = 3

# Setting up images
game_over_img = pygame.image.load(join("assets", "sprites", "game", "game_over.png"))
pause_img = pygame.image.load(join("assets", "sprites", "game", "pause.png"))
background_img = pygame.image.load(join("assets", "sprites", "game", "background.png"))


def spawn_entities(group, entity, length):
    for _ in range(length):
        group.add(entity())


def random_item():
    item = choice([Hourglass, Heart, Star])

    return item


# Game main function
def game(screen):
    # Setting up basic game variables
    running = True
    click = False

    clock = pygame.time.Clock()
    fps = 15

    score = 0
    rounds = 0

    game_state = START_STATE

    # Setting up game over state
    try_again_rect = draw_text("Try again", SMALL_FONT, WHITE, screen, 264, 440)
    back_rect_go = draw_text("Back to menu", SMALL_FONT, WHITE, screen, 239, 502)

    # Setting up start state
    start_timer = 0
    start_counter = 1

    # Setting up pause state
    start_bg = pygame.Surface(WINDOW_SIZE)
    start_bg.set_alpha(150)

    resume_rect = draw_text(f"Resume game", SMALL_FONT, WHITE, screen, 247, 376)
    back_rect = draw_text(f"Back to menu", SMALL_FONT, WHITE, screen, 239, 438)

    # Setting up normal state
    max_apple = 6
    max_bombs = 2

    snake = Snake(300, 300)

    apples = pygame.sprite.Group()
    spawn_entities(apples, Apple, max_apple)

    bombs = pygame.sprite.Group()
    spawn_entities(bombs, Bomb, max_bombs)

    big_bombs = pygame.sprite.Group()

    items = pygame.sprite.Group()

    # Setting frozen time snake state
    frozen_bg = pygame.Surface(WINDOW_SIZE)
    frozen_bg.fill(GRAY)
    frozen_bg.set_alpha(150)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE and game_state == NORMAL_STATE:
                    # Put in pause state
                    game_state = PAUSE_STATE
            elif event.type == MOUSEBUTTONDOWN and game_state != NORMAL_STATE:
                if event.button == 1:
                    click = True

        if game_state == NORMAL_STATE:
            # Snake update
            snake.update()

            # Groups update
            if snake.state != snake.FROZEN_TIME_STATE:
                apples.update()
                bombs.update()
                big_bombs.update(bombs, len(apples), max_apple)
                items.update()

            for bomb in bombs:
                if snake.state == snake.STAR_STATE:
                    bomb.eatable = True
                else:
                    bomb.eatable = False

                if snake.head.rect.colliderect(bomb.rect) and bomb.eatable:
                    APPLE_SOUND.play()
                    score += 10
                    bomb.kill()
                    continue

                snake.collision_with_bomb(bomb)

            for big_bomb in big_bombs:
                snake.collision_with_bomb(big_bomb)

            for apple in apples:
                # Checking collision between snake's head and apples
                if snake.head.rect.colliderect(apple):
                    APPLE_SOUND.play()
                    score += 5
                    apple.kill()

            for item in items:
                if snake.head.rect.colliderect(item):
                    ITEM_SOUND.play()
                    snake.collision_with_items(item)

            if snake.lives <= 0:
                game_state = GAME_OVER_STATE

        # Cleaning the screen
        screen.fill((0, 0, 0))

        # Rendering entities
        apples.draw(screen)
        bombs.draw(screen)
        big_bombs.draw(screen)
        items.draw(screen)

        if snake.state == snake.FROZEN_TIME_STATE:
            screen.blit(frozen_bg, (0, 0))

        # Rendering snake
        snake.render(screen)

        # Rendering Fonts
        draw_text(f"Score: {score}", SMALL_FONT, WHITE, screen, 48, 20)
        draw_text(f"Round {rounds}", SMALL_FONT, WHITE, screen, 281, 20)
        draw_text(f"Lives: {snake.lives}", SMALL_FONT, WHITE, screen, 497, 20)

        if len(apples) == 0:
            rounds += 1

            game_state = START_STATE
            snake.state = snake.STAR_STATE

            lives = snake.lives

            snake = Snake(300, 300)
            snake.lives = lives

            max_bombs += 1

            if len(items) > 0:
                score += 20

            apples.empty()
            bombs.empty()
            items.empty()

            spawn_entities(items, random_item(), 1)
            spawn_entities(apples, Apple, max_apple)

            if max_bombs % 6 == 0:
                max_big_bombs = max_bombs // 6

                spawn_entities(big_bombs, BigBomb, max_big_bombs)
            else:
                max_big_bombs = 0

            spawn_entities(bombs, Bomb, max_bombs - (max_big_bombs * 3))

        if game_state != NORMAL_STATE:
            mx, my = pygame.mouse.get_pos()

            if game_state == PAUSE_STATE:
                # Rendering background
                screen.blit(pause_img, (0, 0))

                # Rendering Fonts
                draw_text("Resume game", SMALL_FONT, WHITE, screen, 247, 376)
                draw_text("Back to menu", SMALL_FONT, WHITE, screen, 239, 438)

                if resume_rect.collidepoint((mx, my)):
                    draw_text("Resume game", SMALL_FONT, RED, screen, 247, 376)
                    if click:
                        SELECT_SOUND.play()
                        game_state = START_STATE
                elif back_rect.collidepoint((mx, my)):
                    draw_text("Back to menu", SMALL_FONT, RED, screen, 239, 438)
                    if click:
                        SELECT_SOUND.play()
                        running = False
            elif game_state == START_STATE:
                start_timer += 1

                screen.blit(start_bg, (0, 0))
                draw_text(f"{start_counter}", BIG_FONT, WHITE, screen, 331, 289)

                if start_timer > fps:
                    COUNT_SOUND.play()
                    start_timer = 0
                    start_counter += 1

                if start_counter > 3:
                    start_counter = 1

                    game_state = NORMAL_STATE
            elif game_state == GAME_OVER_STATE:
                screen.blit(game_over_img, (0, 0))

                draw_text(str(score), SMALL_FONT, WHITE, screen, 392, 292)
                draw_text(str(rounds), SMALL_FONT, WHITE, screen, 392, 334)

                draw_text("Try again", SMALL_FONT, WHITE, screen, 264, 446)
                draw_text("Back to menu", SMALL_FONT, WHITE, screen, 239, 498)

                if try_again_rect.collidepoint((mx, my)):
                    draw_text("Try again", SMALL_FONT, RED, screen, 264, 446)
                    if click:
                        SELECT_SOUND.play()
                        game(screen)
                        running = False
                elif back_rect_go.collidepoint((mx, my)):
                    draw_text("Back to menu", SMALL_FONT, RED, screen, 239, 498)
                    if click:
                        SELECT_SOUND.play()
                        running = False

            click = False

        pygame.display.flip()
        clock.tick(fps)
