import pygame
import sys
from game1.constant.constnants import SCREEN, buttons, WHITE, WIDTH, GREEN, BLACK, levels
from game1.levels import level_1, level_3, level_2, level_4, level_5, level_6
from game1.levels.pyvidplayer import Video
pygame.init()
# Инициализация экрана
pygame.display.set_caption("Главное меню")

# Текущее состояние меню
menu_state = "main"

# Шрифт
font = pygame.font.Font(None, 36)

# Списки прямоугольников кнопок для определения нажатий
button_rects = []
level_rects = []

pygame.mixer.music.load('sounds/MM usual castle.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

def draw_menu():
    """Отрисовка главного меню"""
    # Бэкграунд меню
    background = pygame.image.load("../images/bg/menu_background_3 prev.png")
    SCREEN.blit(background, (0, 0))

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
    background = pygame.image.load("../images/bg/menu_background_3 prev.png")
    SCREEN.blit(background, (0, 0))
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
                pygame.mixer.music.pause()
                vid = Video("../video/start-scene.mp4")
                vid.set_size((1920, 1080))

                def intro():
                    while True:
                        vid.draw(SCREEN, (0, 0))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                vid.close()
                                level_1.start_level()
                intro()

            elif selected_level == "Уровень 2":
                pygame.mixer.music.pause()
                vid = Video("../video/cat 1-2.mp4")
                vid.set_size((1920, 1080))

                def intro():
                    while True:
                        vid.draw(SCREEN, (0, 0))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                vid.close()
                                level_2.start_level()

                intro()

            elif selected_level == "Уровень 3":
                pygame.mixer.music.pause()
                vid = Video("../video/cat 2-3.mp4")
                vid.set_size((1920, 1080))

                def intro():
                    while True:
                        vid.draw(SCREEN, (0, 0))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                vid.close()
                                level_3.start_level()
                intro()


            elif selected_level == "Уровень 4":
                pygame.mixer.music.pause()
                vid = Video("../video/cat 3-4.mp4")
                vid.set_size((1920, 1080))
                def intro():
                    while True:
                        vid.draw(SCREEN, (0, 0))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                vid.close()
                                level_4.start_level()
                intro()

            elif selected_level == "Уровень 5":
                pygame.mixer.music.pause()
                vid = Video("../video/cat 4-5.mp4")
                vid.set_size((1920, 1080))

                def intro():
                    while True:
                        vid.draw(SCREEN, (0, 0))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                vid.close()
                                level_5.start_level()

                intro()

            elif selected_level == "Уровень 6":
                pygame.mixer.music.pause()
                vid = Video("../video/cat 5-6.mp4")
                vid.set_size((1920, 1080))

                def intro():
                    while True:
                        vid.draw(SCREEN, (0, 0))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                vid.close()
                                level_6.start_level()

                intro()

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
                                selected_level = "Уровень 1"
                                menu_state = "game"
                                print("Игра начинается заново")
                            elif i == 1:
                                menu_state = "levels"  # Переход к выбору уровня
                            elif i == 2:
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
