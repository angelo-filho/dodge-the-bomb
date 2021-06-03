from pygame.locals import *

from control.supports import *
from control.constants import *

credits_img = pygame.image.load(join("assets", "sprites", "credits_screen", "credits.png"))


def credits_screen(screen):
    back_rect = draw_text("Back", small_font, WHITE, screen, 306, 558)

    click = False
    running = True

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))
        screen.blit(credits_img, (0, 0))

        draw_text("Back", small_font, WHITE, screen, 306, 558)

        if back_rect.collidepoint((mx, my)):
            draw_text("Back", small_font, RED, screen, 306, 558)
            if click:
                running = False

        click = False

        pygame.display.flip()
        clock.tick(60)
