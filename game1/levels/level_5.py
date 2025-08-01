import sys
import subprocess

import pygame.image
from pyvidplayer import Video
from game1.Player import Player
from game1.constant.constnants import *
from game1.levels.attack import sword1_vertical, get_attack_damage, chicken_vertical, \
    chicken_horizontal, chicken_diagonal2, chicken_diagonal, chicken_horizontal_right, \
     sword2_vertical, sword2_horizontal_left, sword2_horizontal_right, \
    sword2_diagonal, sword2_diagonal2, long_sword_vertical, long_sword_horizontal_left, long_sword_horizontal_right, \
    long_sword_diagonal, long_sword_diagonal2, gas_vertical, gas_horizontal_left, gas_horizontal_right, gas_diagonal, \
    gas_diagonal2
from game1.levels.events.event_level_5 import events


pygame.init()

def display_win_level(screen, font, score):
    background = pygame.image.load("../images/bg/level_5.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    next_level_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 50)
    main_menu_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 120, 300, 50)

    clock = pygame.time.Clock()

    while True:
        screen.blit(background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # Определение цвета кнопок при наведении
        next_level_color = GREEN if next_level_button_rect.collidepoint(mouse_pos) else WHITE
        menu_color = GREEN if main_menu_button_rect.collidepoint(mouse_pos) else WHITE

        # Рисуем кнопки
        pygame.draw.rect(screen, next_level_color, next_level_button_rect, border_radius=10)
        pygame.draw.rect(screen, menu_color, main_menu_button_rect, border_radius=10)

        draw_text_centered(screen, "Следующий уровень", font, BLACK, next_level_button_rect.center)
        draw_text_centered(screen, "Главное меню", font, BLACK, main_menu_button_rect.center)

        # Отображаем текст "Вы победили!" в центре экрана
        draw_text_centered(screen, "Вы победили!", font, (255, 255, 0), (WIDTH // 2, HEIGHT // 4))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_level_button_rect.collidepoint(event.pos):
                    from game1.levels import level_6
                    level_6.start_level()
                elif main_menu_button_rect.collidepoint(event.pos):
                    from game1.menu import main_menu
                    main_menu.main()

        clock.tick(60)

def draw_text_centered(surface, text, font, color, center):
    """Отрисовка текста по центру"""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    surface.blit(text_surface, text_rect)
    return text_rect

def display_game_over_screen(screen, font):
    """Отображает экран 'Игра окончена' с опциями и возвращает выбранное действие"""
    background = pygame.image.load("../images/bg/level_5.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    restart_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 50)
    main_menu_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 120, 300, 50)

    clock = pygame.time.Clock()

    while True:
        screen.blit(background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # Определение цвета кнопок при наведении
        restart_color = GREEN if restart_button_rect.collidepoint(mouse_pos) else WHITE
        menu_color = GREEN if main_menu_button_rect.collidepoint(mouse_pos) else WHITE

        # Рисуем кнопки
        pygame.draw.rect(screen, restart_color, restart_button_rect, border_radius=10)
        pygame.draw.rect(screen, menu_color, main_menu_button_rect, border_radius=10)

        draw_text_centered(screen, "Повторить", font, BLACK, restart_button_rect.center)
        draw_text_centered(screen, "Главное меню", font, BLACK, main_menu_button_rect.center)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button_rect.collidepoint(event.pos):
                    start_level()
                elif main_menu_button_rect.collidepoint(event.pos):
                    from game1.menu import main_menu
                    main_menu.main()

        clock.tick(60)

def start_level():
    """Уровень 5"""
    pygame.display.set_caption("Уровень 5")
    font = pygame.font.Font(None, 36)

    background = pygame.image.load("../images/bg/level_5.png")  # Загружаем фон
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Масштабируем под размер окна

    level_text = font.render("Уровень 5", True, WHITE)
    level_text_rect = level_text.get_rect(center=(WIDTH // 2, HEIGHT - 950))

    # Переменные для здоровья и очков
    health = HEALTH
    score = SCORE
    score_timer = SCORE_TIMER

    # Инициализация игрока
    player = Player()
    play_sprites = pygame.sprite.Group()
    play_sprites.add(player)
    player_images_right = pygame.image.load("../images/hero/herosprava.png")
    player_images_left = pygame.image.load("../images/hero/herosleva.png")

    # Группа спрайтов-проджектайлов
    projectiles = pygame.sprite.Group()

    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()  # Время начала уровня

    all_projectiles = pygame.sprite.Group() # Создаем группу для хранения всех снарядов

    pygame.display.flip()

    pygame.mixer.music.load('../menu/sounds/level 5.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    # Игровой цикл
    player.image = player_images_right
    waiting = True
    while waiting:
        SCREEN.blit(background, (0, 0))  # Устанавливаем фон

        current_time = (pygame.time.get_ticks() - start_time) / 1000  # Время в секундах

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.image = player_images_left
            player.rect.centerx -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.image = player_images_right
            player.rect.centerx += 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.rect.centery -= 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.rect.centery += 5

        # Ограничение движения героя
        if player.rect.centerx - HERO_SIZE // 2 < WIDTH // 2 - 245:
            player.rect.centerx = WIDTH // 2 - 245 + HERO_SIZE // 2
        elif player.rect.centerx + HERO_SIZE // 2 > WIDTH // 2 + 245:
            player.rect.centerx = WIDTH // 2 + 245 - HERO_SIZE // 2
        if player.rect.centery - HERO_SIZE // 2 < HEIGHT // 2 + 5:
            player.rect.centery = HEIGHT // 2 + 5 + HERO_SIZE // 2
        elif player.rect.centery + HERO_SIZE // 2 > HEIGHT // 2 + 495:
            player.rect.centery = HEIGHT // 2 + 495 - HERO_SIZE // 2

        chicken_image = pygame.image.load("../images/projectiles/general/chicken.png")
        gas_image = pygame.image.load("../images/projectiles/level_5/ball.png")
        arrow_image = pygame.image.load("../images/projectiles/general/arrow.png")
        stone_image = pygame.image.load("../images/projectiles/level_5/stone.png")
        sword2_image = pygame.image.load("../images/projectiles/level_5/dragon_right.png")
        dragon_image = pygame.image.load("../images/projectiles/level_5/dragon_left.png")

        # Проверка событий
        for event in events[:]:
            event_time, num_swords, start_pos, direction = event
            if event_time <= current_time < event_time + 1:
                for _ in range(num_swords):

                    if direction == "sword1_vertical":
                        rotated_sword1 = pygame.transform.rotate(arrow_image.copy(), 225)
                        projectile_temp = sword1_vertical(rotated_sword1)

                    elif direction == "sword2_vertical":
                        rotated_sword1 = pygame.transform.rotate(sword2_image.copy(), 225)
                        projectile_temp = sword2_vertical(rotated_sword1)
                    elif direction == "sword2_diagonal":
                        rotated_sword1 = pygame.transform.rotate(sword2_image.copy(), 135)
                        projectile_temp = sword2_diagonal(rotated_sword1)
                    elif direction == "sword2_diagonal2":
                        rotated_sword1 = pygame.transform.rotate(sword2_image.copy(), 45)
                        projectile_temp = sword2_diagonal2(rotated_sword1)
                    elif direction == "sword2_horizontal_left":
                        rotated_sword1 = pygame.transform.rotate(dragon_image.copy(), 0)
                        projectile_temp = sword2_horizontal_left(rotated_sword1)
                    elif direction == "sword2_horizontal_right":
                        rotated_sword1 = pygame.transform.rotate(sword2_image.copy(), 0)
                        projectile_temp = sword2_horizontal_right(rotated_sword1)

                    elif direction == "gas_vertical":
                        rotated_sword1 = pygame.transform.rotate(gas_image.copy(), 225)
                        projectile_temp = gas_vertical(rotated_sword1)
                    elif direction == "gas_diagonal":
                        rotated_sword1 = pygame.transform.rotate(gas_image.copy(), 135)
                        projectile_temp = gas_diagonal(rotated_sword1)
                    elif direction == "gas_diagonal2":
                        rotated_sword1 = pygame.transform.rotate(gas_image.copy(), 45)
                        projectile_temp = gas_diagonal2(rotated_sword1)
                    elif direction == "gas_horizontal_left":
                        rotated_sword1 = pygame.transform.rotate(gas_image.copy(), 180)
                        projectile_temp = gas_horizontal_left(rotated_sword1)
                    elif direction == "gas_horizontal_right":
                        rotated_sword1 = pygame.transform.rotate(gas_image.copy(), 0)
                        projectile_temp = gas_horizontal_right(rotated_sword1)

                    elif direction == "stone_vertical":
                        rotated_sword1 = pygame.transform.rotate(stone_image.copy(), 225   )
                        projectile_temp = long_sword_vertical(rotated_sword1)
                    elif direction == "stone_diagonal":
                        rotated_sword1 = pygame.transform.rotate(stone_image.copy(), 135)
                        projectile_temp = long_sword_diagonal(rotated_sword1)
                    elif direction == "stone_diagonal2":
                        rotated_sword1 = pygame.transform.rotate(stone_image.copy(), 45)
                        projectile_temp = long_sword_diagonal2(rotated_sword1)
                    elif direction == "stone_horizontal_left":
                        rotated_sword1 = pygame.transform.rotate(stone_image.copy(), 0)
                        projectile_temp = long_sword_horizontal_left(rotated_sword1)
                    elif direction == "stone_horizontal_right":
                        rotated_sword1 = pygame.transform.rotate(stone_image.copy(), 0)
                        projectile_temp = long_sword_horizontal_right(rotated_sword1)

                    elif direction == "chicken_vertical":
                        rotated_chicken = pygame.transform.rotate(chicken_image.copy(), 270)
                        projectile_temp = chicken_vertical(rotated_chicken)
                    elif direction == "chicken_horizontal":
                        rotated_chicken = pygame.transform.rotate(chicken_image.copy(), 0)
                        projectile_temp = chicken_horizontal(rotated_chicken)
                    elif direction == "chicken_horizontal_right":
                        rotated_chicken = pygame.transform.rotate(chicken_image.copy(), 180)
                        projectile_temp = chicken_horizontal_right(rotated_chicken)
                    elif direction == "chicken_diagonal":
                        rotated_chicken = pygame.transform.rotate(chicken_image.copy(), -135)
                        projectile_temp = chicken_diagonal(rotated_chicken)
                    elif direction == "chicken_diagonal2":
                        rotated_chicken = pygame.transform.rotate(chicken_image.copy(), 135)
                        projectile_temp = chicken_diagonal2(rotated_chicken)

                    projectile_temp.rect = projectile_temp.image.get_rect(center=start_pos)
                    projectiles.add(projectile_temp)

                events.remove(event)

        # Удаление снарядов, вышедших за пределы экрана
        for projectile in projectiles.sprites():
            if (projectile.rect.bottom < 0 or projectile.rect.top > HEIGHT or
                    projectile.rect.right < 0 or projectile.rect.left > WIDTH):
                projectile.kill()

        # Обновление экрана
        SCREEN.blit(level_text, level_text_rect)  # Отображаем текст уровня снова

        # Отображение текстовых элементов
        SCREEN.blit(level_text, level_text_rect)
        pygame.draw.rect(SCREEN, WHITE, (WIDTH // 2 - 250, HEIGHT // 2, 500, 500), 5)

        health_text = font.render(f"Здоровье: {health}", True, WHITE)
        SCREEN.blit(health_text, (60, 120))

        score_text = font.render(f"Очки: {score}", True, WHITE)
        SCREEN.blit(score_text, (WIDTH - 160, 120))

        # Таймер начисления очков
        score_timer += 1
        if score_timer >= 60:
            score_timer = 0
            score += 10

        if score > 450:
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
                            display_win_level(SCREEN, font, score)

            intro()
            break

        # Отрисовка игрока и снарядов
        play_sprites.update()
        play_sprites.draw(SCREEN)

        projectiles.update()
        projectiles.draw(SCREEN)
        running = True
        # Проверка коллизий
        for projectile in projectiles:
            if projectile.rect.colliderect(player.rect):
                attack_type = projectile.__class__.__name__.lower()
                damage = get_attack_damage(attack_type)
                health -= damage
                player.take_damage(damage)
                projectile.kill()

                if health <= 0:
                    pygame.mixer.music.pause()
                    pygame.mixer.music.load("sounds/death.mp3")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.2)
                    display_game_over_screen(SCREEN, font)
                    running = False  # Прерываем игровой цикл.
                    break  # Важно!

        pygame.display.flip()
        clock.tick(FPS)
        if not running:
            pygame.time.delay(500)
            display_game_over_screen(SCREEN, font, "level_1.py", score)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    start_level()