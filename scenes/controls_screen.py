from pygame.locals import *
from control.supports import *
from control.constants import *
from os.path import join

controls_img = pygame.image.load(join("assets", "sprites", "controls_screen", "controls.png"))


def controls_screen(screen):
    back_rect = draw_text("Back", SMALL_FONT, WHITE, screen, 306, 515)
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
        screen.blit(controls_img, (0, 0))

        draw_text("Back", SMALL_FONT, WHITE, screen, 306, 515)

        if back_rect.collidepoint((mx, my)):
            draw_text("Back", SMALL_FONT, RED, screen, 306, 515)
            if click:
                SELECT_SOUND.play()
                running = False

        click = False

        pygame.display.flip()
        clock.tick(60)
