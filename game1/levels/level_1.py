import pygame
import sys
from game1.constant.constnants import *
from game1.levels.tutorial import show_instructions  # Импортируем новые функции

pygame.init()

def start_level():
    """Простой уровень 1"""
    pygame.display.set_caption("Уровень 1")

    font = pygame.font.Font(None, 36)
    SCREEN.fill(BLACK)

    # Размер и начальная позиция героя
    hero_x = WIDTH // 2 - HERO_SIZE // 2  # Начальная позиция героя по X
    hero_y = HEIGHT // 2 - HERO_SIZE // 2  # Начальная позиция героя по Y

    # Отображение текста
    level_text = font.render("Уровень 1", True, WHITE)
    level_text_rect = level_text.get_rect(center=(WIDTH // 2, HEIGHT - 950))  # Сдвигаем текст выше

    # Флаг для отслеживания, показывать ли текст
    text_shown = True
    # Флаг для отображения информации о местоположении здоровья и очков
    info_shown = False

    # Переменная для отслеживания здоровья героя
    health = HEALTH
    score = SCORE
    score_timer = SCORE_TIMER

    # Начальный цвет линии
    line_color = RED
    line_delay_timer = 0  # Таймер для задержки 15 секунд
    color_change_timer = 0  # Таймер для смены цвета линии каждые 3 секунды

    pygame.display.flip()

    # Ждем события выхода или движения героя
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False

                # Если нажата одна из стрелок, скрываем текст и показываем информацию
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    text_shown = False
                    info_shown = True

        # Обработка перемещения героя
        keys = pygame.key.get_pressed()  # Получаем состояние клавиш
        if keys[pygame.K_LEFT]:  # Перемещение влево
            hero_x -= 5
        if keys[pygame.K_RIGHT]:  # Перемещение вправо
            hero_x += 5
        if keys[pygame.K_UP]:  # Перемещение вверх
            hero_y -= 5
        if keys[pygame.K_DOWN]:  # Перемещение вниз
            hero_y += 5

        # Ограничение движения героя внутри экрана
        if hero_x < 0:
            hero_x = 0
        elif hero_x + HERO_SIZE > WIDTH:
            hero_x = WIDTH - HERO_SIZE
        if hero_y < 0:
            hero_y = 0
        elif hero_y + HERO_SIZE > HEIGHT:
            hero_y = HEIGHT - HERO_SIZE

        # Обновление экрана
        SCREEN.fill(BLACK)  # Перерисовываем экран
        SCREEN.blit(level_text, level_text_rect)  # Отображаем текст уровня снова

        # Отображение здоровья в левом верхнем углу
        health_text = font.render(f"Здоровье: {health}", True, WHITE)
        health_text_rect = health_text.get_rect(topleft=(60, 120))
        SCREEN.blit(health_text, health_text_rect)

        # Отображение очков в правом верхнем углу
        score_text = font.render(f"Очки: {score}", True, WHITE)
        score_text_rect = score_text.get_rect(topright=(WIDTH - 60, 120))
        SCREEN.blit(score_text, score_text_rect)

        if text_shown:
            # Показываем инструкции, если флаг text_shown == True
            show_instructions(SCREEN, font)  # Используем функцию из tutorial.py

        line_delay_timer += 1
        if line_delay_timer >= 300:  # 10 секунд (10 секунд * 60 FPS = 300 кадров)
            # После задержки показываем линию
            line_y = HEIGHT // 2
            pygame.draw.line(SCREEN, line_color, (0, line_y), (WIDTH, line_y), 100)

            # Таймер для смены цвета линии каждые 3 секунды
            color_change_timer += 1
            if color_change_timer >= 180:  # 3 секунды (3 секунды * 60 FPS = 180 кадров)
                color_change_timer = 0
                # Сменить цвет линии
                if line_color == RED:
                    line_color = PINK
                elif line_color == PINK:
                    line_color = LIGHT_PINK
                else:
                    line_color = RED

            # Проверка на столкновение с линией (только если цвет линии LIGHT_PINK)
            if line_color == LIGHT_PINK and hero_y + HERO_SIZE > line_y - 10 and hero_y < line_y + 10:
                health -= 0.25  # Наносим урон

        # Таймер для начисления очков
        score_timer += 1
        if score_timer >= 60:  # 1 секунда (60 кадров)
            score += 10  # Начисляем очки

        # Рисуем героя
        pygame.draw.rect(SCREEN, HERO_COLOR, (hero_x, hero_y, HERO_SIZE, HERO_SIZE))  # Перерисовываем героя

        pygame.display.flip()  # Обновляем экран
        pygame.time.Clock().tick(FPS)  # Ограничиваем FPS (60 кадров в секунду)

if __name__ == "__main__":
    start_level()
