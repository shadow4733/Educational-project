import pygame
import sys
import enemies
from sounds_game import bg_music
# from enemies import Enemy


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

# class Room:
#     def __init__(self, name, enemies, doors, font):
#         self.name = name
#         self.enemies = enemies
#         self.doors = doors  # Список дверей
#         self.font = font
#
#     def draw(self, screen):
#         screen.fill((0, 0, 0))
#         title_text = self.font.render(f"Комната: {self.name}", True, WHITE)
#         screen.blit(title_text, (800, 50))
#         for door in self.doors:  # Отрисовка дверей
#             door.draw(screen)

class Door:
    def __init__(self, x, y, width, height, target_room_index):
        self.rect = pygame.Rect(x, y, width, height)
        self.target_room_index = target_room_index

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)  # Цвет двери (желтый)

def run():
    pygame.init()

    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w  # Ширина экрана
    screen_height = screen_info.current_h  # Высота экрана

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("GAME")
    bg_color = (0, 0, 0)
    player = Character(screen)

    # font = pygame.font.Font(None, 74)
    #
    # rooms = [
    #     Room("A", [Enemy(1200, 750, 100, 10)], [Door(950, 300, 50, 100, 1)], font),  # Дверь в комнату B
    #     Room("B", [Enemy(1200, 750, 100, 10)], [Door(50, 300, 50, 100, 0)], font),  # Дверь в комнату A
    #     Room("C", [], [Door(950, 300, 50, 100, 1)], font),  # Дверь в комнату D
    #     Room("D", [], [Door(50, 300, 50, 100, 2)], font)  # Дверь в комнату C
    #     # Добавьте другие комнаты и двери по аналогии
    # ]
    #
    # current_room_index = 0  # Индекс текущей комнаты

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
        #
        #
        #     # Переход между комнатами
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_RIGHT:  # Перейти в следующую комнату
        #             current_room_index = (current_room_index + 1) % len(rooms)
        #         if event.key == pygame.K_LEFT:  # Вернуться в предыдущую комнату
        #             current_room_index = (current_room_index - 1) % len(rooms)
        #
        #     # Управление движением персонажа
        # player.move(keys, delta_time, pygame.Rect(0, 300, screen_width, 500), rooms[current_room_index].enemies)
        #
        # screen.fill(bg_color)
        # # Отобразить текущую комнату
        # rooms[current_room_index].draw(screen)
        # player.output(rooms[current_room_index].enemies)

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