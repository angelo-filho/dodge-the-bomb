from pygame.locals import *
from os import path
from control.supports import *
from control.constants import *
from screens.credits_screen import credits_screen
from screens.controls_screen import controls_screen
from screens.game import game

background = pygame.image.load(path.join("assets", "sprites", "main_menu", "main_menu.png"))


def main_menu(screen):
    player_rect = draw_text("Play", small_font, WHITE, screen, 306, 314)
    controls_rect = draw_text("Controls", small_font, WHITE, screen, 273, 376)
    credits_rect = draw_text("Credits", small_font, WHITE, screen, 281, 438)
    exit_rect = draw_text("Exit", small_font, WHITE, screen, 306, 500)

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

        draw_text("Play", small_font, WHITE, screen, 306, 314)
        draw_text("Controls", small_font, WHITE, screen, 273, 376)
        draw_text("Credits", small_font, WHITE, screen, 281, 438)
        draw_text("Exit", small_font, WHITE, screen, 306, 500)

        if player_rect.collidepoint((mx, my)):
            draw_text("Play", small_font, RED, screen, 306, 314)
            if click:
                game(screen)
        elif controls_rect.collidepoint((mx, my)):
            draw_text("Controls", small_font, RED, screen, 273, 376)
            if click:
                controls_screen(screen)
        elif credits_rect.collidepoint((mx, my)):
            draw_text("Credits", small_font, RED, screen, 281, 438)
            if click:
                credits_screen(screen)
        elif exit_rect.collidepoint((mx, my)):
            draw_text("Exit", small_font, RED, screen, 306, 500)
            if click:
                quit_game()

        click = False

        pygame.display.flip()
        clock.tick(60)
