# import pygame
# import sys
# from enemies import Enemy  # Импортируем класс Enemy
#
# class Room:
#     def __init__(self, name, enemies, font):
#         self.name = name
#         self.enemies = enemies
#         self.font = font
#
#     def draw(self, screen):
#         screen.fill((0, 0, 0))
#         title_text = self.font.render(f"Комната: {self.name}", True, WHITE)
#         screen.blit(title_text, (800, 50))
#
# def run():
#     pygame.init()
#
#     screen_info = pygame.display.Info()
#     screen_width = screen_info.current_w
#     screen_height = screen_info.current_h
#
#     screen = pygame.display.set_mode((screen_width, screen_height))
#     pygame.display.set_caption("GAME")
#     bg_color = (0, 0, 0)
#     player = Character(screen)
#
#     # Создаем шрифт
#     font = pygame.font.Font(None, 74)
#
#     # Определение комнат
#     rooms = [
#         Room("A", [Enemy(1200, 750, 100, 10)], font),
#         Room("B", [Enemy(1200, 750, 100, 10)], font),
#         Room("C", [], font),
#         Room("D", [], font),
#         Room("E", [], font),
#         Room("F", [], font),
#         Room("G", [], font)
#     ]
#
#     current_room_index = 0
#     clock = pygame.time.Clock()
#
#     while True:
#         delta_time = clock.tick(240) / 1000.0
#
#         keys = pygame.key.get_pressed()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
#                 pygame.quit()
#                 sys.exit()
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RIGHT:
#                     current_room_index = (current_room_index + 1) % len(rooms)
#                 if event.key == pygame.K_LEFT:
#                     current_room_index = (current_room_index - 1) % len(rooms)
#
#         # Управление движением персонажа
#         player.move(keys, delta_time, pygame.Rect(0, 300, screen_width, 500), rooms[current_room_index].enemies)
#
#         screen.fill(bg_color)
#         rooms[current_room_index].draw(screen)
#         player.output(rooms[current_room_index].enemies)
#         for enemy in rooms[current_room_index].enemies:
#             enemy.draw(screen)
#         pygame.display.flip()
#
# if __name__ == "__main__":
#     main_menu()
#     run()