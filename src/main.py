import pygame

from src.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, FPS
from ui.menus import MainMenu

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Roguelike")

    menu = MainMenu(screen)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            menu.handle_event(event)

        screen.fill(BLACK)

        menu.draw()

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()