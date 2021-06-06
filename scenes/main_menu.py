from pygame.locals import *
from os import path
from control.supports import *
from control.constants import *
from scenes.credits_screen import credits_screen
from scenes.controls_screen import controls_screen
from scenes.game import game

background = pygame.image.load(path.join("assets", "sprites", "main_menu", "main_menu.png"))


def main_menu(screen):
    player_rect = draw_text("Play", SMALL_FONT, WHITE, screen, 306, 314)
    controls_rect = draw_text("Controls", SMALL_FONT, WHITE, screen, 273, 376)
    credits_rect = draw_text("Credits", SMALL_FONT, WHITE, screen, 281, 438)
    exit_rect = draw_text("Exit", SMALL_FONT, WHITE, screen, 306, 500)

    click = False

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        draw_text("Play", SMALL_FONT, WHITE, screen, 306, 314)
        draw_text("Controls", SMALL_FONT, WHITE, screen, 273, 376)
        draw_text("Credits", SMALL_FONT, WHITE, screen, 281, 438)
        draw_text("Exit", SMALL_FONT, WHITE, screen, 306, 500)

        if player_rect.collidepoint((mx, my)):
            draw_text("Play", SMALL_FONT, RED, screen, 306, 314)
            if click:
                SELECT_SOUND.play()
                game(screen)
        elif controls_rect.collidepoint((mx, my)):
            draw_text("Controls", SMALL_FONT, RED, screen, 273, 376)
            if click:
                SELECT_SOUND.play()
                controls_screen(screen)
        elif credits_rect.collidepoint((mx, my)):
            draw_text("Credits", SMALL_FONT, RED, screen, 281, 438)
            if click:
                SELECT_SOUND.play()
                credits_screen(screen)
        elif exit_rect.collidepoint((mx, my)):
            draw_text("Exit", SMALL_FONT, RED, screen, 306, 500)
            if click:
                SELECT_SOUND.play()
                quit_game()

        click = False

        pygame.display.flip()
        clock.tick(60)
