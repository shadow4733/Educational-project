import pygame
from game1.constant.constnants import WIDTH, HEIGHT, WHITE

def show_instructions(screen, font):
    """Отображает инструкции для игрока"""
    instructions_text1 = font.render("Используйте стрелки для передвижения", True, WHITE)
    instructions_text2 = font.render("→ Вправо", True, WHITE)
    instructions_text3 = font.render("← Влево", True, WHITE)
    instructions_text4 = font.render("↑ Вверх", True, WHITE)
    instructions_text5 = font.render("↓ Вниз", True, WHITE)

    instructions_text_rect1 = instructions_text1.get_rect(center=(WIDTH // 2, HEIGHT - 900))
    instructions_text_rect2 = instructions_text2.get_rect(center=(WIDTH // 2, HEIGHT - 860))
    instructions_text_rect3 = instructions_text3.get_rect(center=(WIDTH // 2, HEIGHT - 820))
    instructions_text_rect4 = instructions_text4.get_rect(center=(WIDTH // 2, HEIGHT - 780))
    instructions_text_rect5 = instructions_text5.get_rect(center=(WIDTH // 2, HEIGHT - 740))

    screen.blit(instructions_text1, instructions_text_rect1)
    screen.blit(instructions_text2, instructions_text_rect2)
    screen.blit(instructions_text3, instructions_text_rect3)
    screen.blit(instructions_text4, instructions_text_rect4)
    screen.blit(instructions_text5, instructions_text_rect5)

def show_info(screen, font):
    """Отображает информацию о местоположении здоровья и очков"""
    info_text1 = font.render("В левом верхнем углу ваше здоровье", True, WHITE)
    info_text2 = font.render("В правом верхнем углу ваши очки", True, WHITE)
    info_text3 = font.render("Основной смысл игры заключается в том, чтобы уклоняться от атак и набирать очки", True, WHITE)
    info_text4 = font.render("Каждую секунду дается по 10 очков, чтобы перейти на следующий уровень необходимо набрать 1000 очков", True, WHITE)

    screen.blit(info_text1, (WIDTH // 2 - 200, HEIGHT - 900))
    screen.blit(info_text2, (WIDTH // 2 - 200, HEIGHT - 840))
    screen.blit(info_text3, (WIDTH // 2 - 500, HEIGHT - 780))
    screen.blit(info_text4, (WIDTH // 2 - 700, HEIGHT - 720))
