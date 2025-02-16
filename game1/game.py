import pygame
import sys
import enemies
from sounds_game import bg_music

# Убедитесь, что класс Character находится в этом же файле или импортирован корректно
from character import Character  # Импортируем класс Character

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("GAME")
    font = pygame.font.Font(None, 74)  # Шрифт для текста
    bg_color = (0, 0, 0)  # Цвет фона



    while True:
        screen.fill(bg_color)
        pygame.draw.rect(screen, WHITE, (775, 175, 415, 100))
        title_text = font.render("Главное Меню", True, (0, 0, 0))
        start_text = font.render("Нажмите 'Enter' для начала", True, (255, 255, 255))
        exit_text = font.render("Нажмите 'Escape' для выхода", True, (255, 255, 255))

        screen.blit(title_text, (800, 200))
        screen.blit(start_text, (600, 400))
        screen.blit(exit_text, (600, 500))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Нажатие клавиши Enter

                    return  # Переход к игре
                if event.key == pygame.K_ESCAPE:  # Нажатие клавиши Escape
                    pygame.quit()
                    sys.exit()

def run():
    pygame.init()

    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w  # Ширина экрана
    screen_height = screen_info.current_h  # Высота экрана

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("GAME")
    bg_color = (0, 0, 0)
    player = Character(screen)

    area_color = (255, 255, 255)  # Белый цвет
    area_rect = pygame.Rect(0, 300, screen_width, 500)  # Параметры области (x, y, ширина, высота)

    # Создаем врага с 100 HP и 10 уроном
    enemies_list = [enemies.Enemy(1200, 750, 100, 10)]  # Список врагов

    clock = pygame.time.Clock()  # Создаем объект Clock для отслеживания времени

    #Запуск музыки
    bg_music()



    while True:
        delta_time = clock.tick(240) / 1000.0  # Устанавливаем FPS и получаем время в секундах

        keys = pygame.key.get_pressed()  # Получаем состояние клавиш

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

        # Управление движением персонажа
        player.move(keys, delta_time, area_rect, enemies_list)  # Передаем список врагов

        screen.fill(bg_color)
        pygame.draw.rect(screen, area_color, area_rect, 2)  # Рисуем игровую область
        player.output(enemies_list)  # Передаем enemies_list в метод output
        for enemy in enemies_list:  # Рисуем всех врагов на экране
            enemy.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()  # Запуск главного меню
    run()  # Запуск функции run