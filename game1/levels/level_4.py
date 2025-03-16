import pygame

from game1.constant.constnants import SCREEN, BLACK, WIDTH, WHITE, HEIGHT


def start_level():
    """Уровень 4"""
    pygame.mixer.music.load('sounds/MM 8 bit 2.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    font = pygame.font.Font(None, 36)

    SCREEN.fill(BLACK)

    # Отображение текста
    level_text = font.render("Уровень 3", True, WHITE)
    level_text_rect = level_text.get_rect(center=(WIDTH // 2, HEIGHT - 950))