import pygame
import sys
import subprocess
import os
from os import path
from pyvidplayer import Video
from game1.Player import Player
from game1.constant.constnants import *
from game1.levels.attack import sword1_vertical, sword1_horizontal_left, get_attack_damage, chicken_vertical, \
    chicken_horizontal, chicken_diagonal2, chicken_diagonal, sword1_horizontal_right, chicken_horizontal_right, bubble_vertical
from game1.levels.events.event_level_2 import events


pygame.init()

current_level = "level_2.py"
player_health_on_death = 0
player_score_on_death = 0

def display_game_over_screen(screen, font):
    """Отображает экран 'Игра окончена' с опциями."""

    game_over_image = pygame.image.load("../images/bg/game_over.png")
    game_over_rect = game_over_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    restart_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 50)
    main_menu_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 120, 300, 50)
    restart_button_color = WHITE
    main_menu_button_color = WHITE
    mouse_pos = pygame.mouse.get_pos()

    if restart_button_rect.collidepoint(mouse_pos):
        restart_button_color = (200, 200, 200)
    if main_menu_button_rect.collidepoint(mouse_pos):
        main_menu_button_color = (200, 200, 200)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button_rect.collidepoint(event.pos):
                    print("Выйти")
                    pygame.quit()
                    sys.exit()
                elif main_menu_button_rect.collidepoint(event.pos):
                    print("Главное меню")
                    try:
                        subprocess.Popen(["python", "../menu/main_menu.py"])
                    except FileNotFoundError:
                        print("Ошибка: main_menu.py не найден.")

                    pygame.quit()
                    sys.exit()

                    running = False
                    break

        # Отрисовка
        screen.fill(BLACK)
        screen.blit(game_over_image, game_over_rect)

        pygame.draw.rect(screen, restart_button_color, restart_button_rect)
        pygame.draw.rect(screen, main_menu_button_color, main_menu_button_rect)

        restart_text = font.render("Выйти", True, BLACK)
        main_menu_text = font.render("Главное меню", True, BLACK)

        restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)
        main_menu_text_rect = main_menu_text.get_rect(center=main_menu_button_rect.center)

        screen.blit(restart_text, restart_text_rect)
        screen.blit(main_menu_text, main_menu_text_rect)

        pygame.display.flip()



def start_level():
    """Уровень 2"""
    pygame.display.set_caption("Уровень 2")



    font = pygame.font.Font(None, 36)

    SCREEN.fill(BLACK)

    # Загрузка фонового изображения
    #background = pygame.image.load("../images/bg/menu_background_3.png")
    #background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Отображение текста
    level_text = font.render("Уровень 2", True, WHITE)
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

    pygame.mixer.music.load('sounds/MM 8 bit 2.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    # Игровой цикл
    waiting = True
    while waiting:
        #SCREEN.blit(background, (0, 0))  # Устанавливаем фон

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



        # Загружаем изображения проджектайлов
        drop_image = pygame.image.load("../images/projectiles/drop.png")
        crocodile_image_left = pygame.image.load("../images/projectiles/crocodile_left.png")
        crocodile_image_right = pygame.image.load("../images/projectiles/crocodile_right.png")
        bubble_image = pygame.image.load("../images/projectiles/bubble.png")
        chicken_image = pygame.image.load("../images/projectiles/chicken.png")

        # Проверка событий
        for event in events[:]:
            event_time, num_swords, start_pos, direction = event
            if event_time <= current_time < event_time + 1:
                for _ in range(num_swords):

                    if direction == "drop":
                        rotated_sword1 = pygame.transform.rotate(drop_image.copy(), 0)
                        projectile_temp = sword1_vertical(rotated_sword1)
                    elif direction == "crocodile_left":
                        rotated_sword1 = pygame.transform.rotate(crocodile_image_right.copy(), 0)
                        projectile_temp = sword1_horizontal_left(rotated_sword1)
                    elif direction == "crocodile_right":
                        rotated_sword1 = pygame.transform.rotate(crocodile_image_left.copy(), 0)
                        projectile_temp = sword1_horizontal_right(rotated_sword1)
                    elif direction == "bubble_vertical":
                        rotated_bubble = pygame.transform.rotate(bubble_image.copy(), 0)
                        projectile_temp = bubble_vertical(rotated_bubble)



                    elif direction == "chicken_vertical":
                        rotated_chicken = pygame.transform.rotate(chicken_image.copy(), 180)
                        projectile_temp = chicken_vertical(rotated_chicken)
                    elif direction == "chicken_horizontal":
                        rotated_chicken = pygame.transform.rotate(chicken_image.copy(), 270)
                        projectile_temp = chicken_horizontal(rotated_chicken)
                    elif direction == "chicken_horizontal_right":
                        rotated_chicken = pygame.transform.rotate(chicken_image.copy(), 135)
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
        SCREEN.fill(BLACK)  # Перерисовываем экран
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
                    #print("игра закончена")
                    player_health_on_death = health
                    player_score_on_death = score
                    display_game_over_screen(SCREEN, font)
                    running = False  # Прерываем игровой цикл.
                    break  # Важно!



        pygame.display.flip()
        clock.tick(FPS)
        if not running:
            pygame.time.delay(500)
            display_game_over_screen(SCREEN, font, "level_2.py", score)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    start_level()