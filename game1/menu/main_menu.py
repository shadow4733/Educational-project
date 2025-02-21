import pygame
import sys

from game1.constant.constnants import WIDTH, HEIGHT, GRAY, WHITE, BLACK, GREEN, SCREEN
from game1.levels import level_1

pygame.init()

# Инициализация экрана
pygame.display.set_caption("Главное меню")

# Шрифт
font = pygame.font.Font(None, 36)

# Кнопки главного меню
buttons = ["Начать сначала", "Выбрать уровень", "Настройки", "Выход"]
selected_level = None

# Доступные уровни
levels = ["Уровень 1", "Уровень 2", "Уровень 3", "Уровень 4", "Уровень 5", "Уровень 6", "Уровень 7", "Уровень 8", "Уровень 9", "Уровень 10"]

# Текущее состояние меню
menu_state = "main"

# Списки прямоугольников кнопок для определения нажатий
button_rects = []
level_rects = []

def draw_menu():
    """Отрисовка главного меню"""
    SCREEN.fill(BLACK)  # Заливка фона черным
    button_rects.clear()  # Очистка списка кнопок перед обновлением
    mouse_x, mouse_y = pygame.mouse.get_pos()  # Получение координат курсора
    y = 200  # Начальная координата Y
    for text in buttons:
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
        color = GREEN if text_rect.collidepoint(mouse_x, mouse_y) else WHITE  # Подсветка кнопки при наведении
        draw_text(text, WIDTH // 2, y, color)
        button_rects.append(text_rect)  # Добавление кнопки в список
        y += 50  # Смещение вниз
    pygame.display.flip()

def draw_levels():
    """Отрисовка списка уровней"""
    SCREEN.fill(BLACK)  # Заливка фона черным
    level_rects.clear()  # Очистка списка кнопок уровней
    mouse_x, mouse_y = pygame.mouse.get_pos()  # Получение координат курсора
    y = 200  # Начальная координата Y
    for level in levels:
        text_surface = font.render(level, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
        color = GREEN if text_rect.collidepoint(mouse_x, mouse_y) else WHITE  # Подсветка кнопки при наведении
        draw_text(level, WIDTH // 2, y, color)
        level_rects.append(text_rect)  # Добавление кнопки в список
        y += 50  # Смещение вниз

    # Кнопка "Назад"
    back_surface = font.render("Назад", True, WHITE)
    back_rect = back_surface.get_rect(center=(WIDTH // 2, y))
    draw_text("Назад", WIDTH // 2, y, GREEN if back_rect.collidepoint(mouse_x, mouse_y) else WHITE)
    level_rects.append(back_rect)  # Добавление кнопки "Назад" в список
    pygame.display.flip()

def draw_text(text, x, y, color):
    """Функция для отрисовки текста"""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    SCREEN.blit(text_surface, text_rect)  # Отображение текста на экране

def main():
    """Основной игровой цикл"""
    global menu_state, selected_level
    while True:
        SCREEN.fill(WHITE)  # Очистка экрана
        if menu_state == "main":
            draw_menu()
        elif menu_state == "levels":
            draw_levels()
        elif menu_state == "game":
            if selected_level == "Уровень 1":
                level_1.start_level()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Обработка выхода из игры
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Обработка нажатия Escape для возврата в главное меню
                    menu_state = "main"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  # Получение координат клика
                if menu_state == "main":
                    for i, rect in enumerate(button_rects):
                        if rect.collidepoint(x, y):  # Проверка, попал ли клик в кнопку
                            if i == 0:
                                print("Игра начинается заново")
                            elif i == 1:
                                menu_state = "levels"  # Переход к выбору уровня
                            elif i == 2:
                                print("Открыть настройки")
                            elif i == 3:
                                pygame.quit()
                                sys.exit()
                elif menu_state == "levels":
                    for i, rect in enumerate(level_rects):
                        if rect.collidepoint(x, y):
                            if i < len(levels):  # Если выбрали уровень
                                selected_level = levels[i]
                                menu_state = "game"
                            else:
                                menu_state = "main"  # Если выбрали "Назад", вернуться в главное меню

        pygame.display.flip()  # Обновление экрана

if __name__ == "__main__":
    main()
