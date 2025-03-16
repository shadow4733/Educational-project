import pygame
import sys
from game1.constant.constnants import SCREEN, buttons, WHITE, WIDTH, GREEN, BLACK, levels
from game1.levels import level_1, level_2, level_3, level_4, level_5, level_6

pygame.init()

# Инициализация экрана
pygame.display.set_caption("Главное меню")

# Текущее состояние меню
menu_state = "main"
selected_level = None  # Добавляем переменную для выбранного уровня

# Шрифт
font = pygame.font.Font(None, 36)

# Списки прямоугольников кнопок для определения нажатий
button_rects = []
level_rects = []

# Загружаем фоновое изображение 1 раз
background = pygame.image.load("../images/bg/menu_background_3 prev.png")

# Загрузка и настройка музыки
pygame.mixer.music.load('sounds/MM usual castle.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

# Список кнопок для настроек
settings_rects = []

def draw_menu():
    """Отрисовка главного меню"""
    SCREEN.blit(background, (0, 0))

    button_rects.clear()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    y = 200

    for text in buttons:
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
        color = GREEN if text_rect.collidepoint(mouse_x, mouse_y) else WHITE
        draw_text(text, WIDTH // 2, y, color)
        button_rects.append(text_rect)
        y += 50

    pygame.display.flip()

def draw_levels():
    """Отрисовка списка уровней"""
    SCREEN.blit(background, (0, 0))
    level_rects.clear()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    y = 200

    for level in levels:
        text_surface = font.render(level, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
        color = GREEN if text_rect.collidepoint(mouse_x, mouse_y) else WHITE
        draw_text(level, WIDTH // 2, y, color)
        level_rects.append(text_rect)
        y += 50

    back_surface = font.render("Назад", True, WHITE)
    back_rect = back_surface.get_rect(center=(WIDTH // 2, y))
    draw_text("Назад", WIDTH // 2, y, GREEN if back_rect.collidepoint(mouse_x, mouse_y) else WHITE)
    level_rects.append(back_rect)

    pygame.display.flip()

def draw_settings():
    """Отрисовка меню настроек"""
    SCREEN.blit(background, (0, 0))

    settings_rects.clear()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    y = 200

    settings_options = ["Громкость", "Управление", "Полноэкранный режим", "Назад"]
    for option in settings_options:
        text_surface = font.render(option, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
        color = GREEN if text_rect.collidepoint(mouse_x, mouse_y) else WHITE
        draw_text(option, WIDTH // 2, y, color)
        settings_rects.append(text_rect)
        y += 50

    pygame.display.flip()

def handle_settings_events(event, menu_state):
    """Обработка событий в меню настроек"""
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        for i, rect in enumerate(settings_rects):
            if rect.collidepoint(x, y):
                if i == 0:
                    print("Изменить громкость")
                elif i == 1:
                    print("Изменить управление")
                elif i == 2:
                    pygame.display.toggle_fullscreen()
                elif i == 3:
                    return "main"  # Вернуться в главное меню
    return menu_state

def draw_text(text, x, y, color):
    """Функция для отрисовки текста"""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    SCREEN.blit(text_surface, text_rect)

def main():
    """Основной игровой цикл"""
    global menu_state, selected_level

    while True:
        SCREEN.fill(WHITE)  # Очистка экрана

        if menu_state == "main":
            draw_menu()
        elif menu_state == "levels":
            draw_levels()
        elif menu_state == "settings":
            draw_settings()
        elif menu_state == "game":
            pygame.mixer.music.pause()
            if selected_level == "Уровень 1":
                level_1.start_level()
            elif selected_level == "Уровень 2":
                level_2.start_level()
            elif selected_level == "Уровень 3":
                level_3.start_level()
            elif selected_level == "Уровень 4":
                level_4.start_level()
            elif selected_level == "Уровень 5":
                level_5.start_level()
            elif selected_level == "Уровень 6":
                level_6.start_level()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_state = "main"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if menu_state == "main":
                    for i, rect in enumerate(button_rects):
                        if rect.collidepoint(x, y):
                            if i == 0:
                                print("Игра начинается заново")
                            elif i == 1:
                                menu_state = "levels"
                            elif i == 2:
                                menu_state = "settings"  # Открываем настройки
                            elif i == 3:
                                pygame.quit()
                                sys.exit()
                elif menu_state == "levels":
                    for i, rect in enumerate(level_rects):
                        if rect.collidepoint(x, y):
                            if i < len(levels):
                                selected_level = levels[i]
                                menu_state = "game"
                            else:
                                menu_state = "main"
                elif menu_state == "settings":
                    menu_state = handle_settings_events(event, menu_state)

        pygame.display.flip()

if __name__ == "__main__":
    main()
