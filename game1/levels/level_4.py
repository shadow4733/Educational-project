import pygame
import sys
from pyvidplayer import Video
from game1.Player import Player
from game1.constant.constnants import *
from game1.levels.attack import sword1_vertical, sword1_horizontal_left, dragon_vertical, get_attack_damage, \
    dragon_horizontal, chicken_vertical, chicken_horizontal, fireball_vertical, fireball_horizontal, \
    sword2_vertical, sword2_horizontal_left, sword1_diagonal, sword1_diagonal2, dragon1_diagonal2, \
    dragon1_diagonal, chicken_diagonal2, chicken_diagonal, sword2_diagonal, sword2_diagonal2, fireball_diagonal2, fireball_diagonal, \
    fireball_horizontal_right, sword1_horizontal_right, sword2_horizontal_right, chicken_horizontal_right, dragon_horizontal_right
from game1.levels.events.event_level_3 import events

pygame.init()


def start_level():
    """Уровень 4"""
    pygame.display.set_caption("Уровень 4")




    font = pygame.font.Font(None, 36)

    SCREEN.fill(BLACK)

    # Загрузка фонового изображения
    #background = pygame.image.load("../images/bg/menu_background_3.png")
    #background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Отображение текста
    level_text = font.render("Уровень 3", True, WHITE)
    level_text_rect = level_text.get_rect(center=(WIDTH // 2, HEIGHT - 950))

    # Переменные для здоровья и очков
    health = HEALTH
    score = SCORE
    score_timer = SCORE_TIMER

    # Инициализация игрока
    player = Player()
    play_sprites = pygame.sprite.Group()
    play_sprites.add(player)

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
            player.rect.centerx -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
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
        sword1_image = pygame.image.load("../images/projectiles/sword1.png")
        dragon_image = pygame.image.load("../images/projectiles/dragon_main.png")
        chicken_image = pygame.image.load("../images/projectiles/chicken.png")
        sword2_image = pygame.image.load("../images/projectiles/sword2.png")
        fireball_image = pygame.image.load("../images/projectiles/fireball.gif")

        # Проверка событий
        for event in events[:]:
            event_time, num_swords, start_pos, direction = event
            if event_time <= current_time < event_time + 1:
                for _ in range(num_swords):

                    if direction == "sword1_vertical":
                        rotated_sword1 = pygame.transform.rotate(sword1_image.copy(), 180)
                        projectile_temp = sword1_vertical(rotated_sword1)
                    elif direction == "sword1_diagonal":
                        rotated_sword1 = pygame.transform.rotate(sword1_image.copy(), -135)
                        projectile_temp = sword1_diagonal(rotated_sword1)
                    elif direction == "sword1_diagonal2":
                        rotated_sword1 = pygame.transform.rotate(sword1_image.copy(), 135)
                        projectile_temp = sword1_diagonal2(rotated_sword1)
                    elif direction == "sword1_horizontal_left":
                        rotated_sword1 = pygame.transform.rotate(sword1_image.copy(), 270)
                        projectile_temp = sword1_horizontal_left(rotated_sword1)
                    elif direction == "sword1_horizontal_right":
                        rotated_sword1 = pygame.transform.rotate(sword1_image.copy(), 90)
                        projectile_temp = sword1_horizontal_right(rotated_sword1)


                    elif direction == "dragon_vertical":
                        rotated_dragon = pygame.transform.rotate(dragon_image.copy(), 180)
                        projectile_temp = dragon_vertical(rotated_dragon)
                    elif direction == "dragon_horizontal":
                        rotated_dragon = pygame.transform.rotate(dragon_image.copy(), 270)
                        projectile_temp = dragon_horizontal(rotated_dragon)
                    elif direction == "dragon_horizontal_right":
                        rotated_dragon = pygame.transform.rotate(dragon_image.copy(), 90)
                        projectile_temp = dragon_horizontal_right(rotated_dragon)
                    elif direction == "dragon1_diagonal":
                        rotated_dragon = pygame.transform.rotate(dragon_image.copy(), -135)
                        projectile_temp = dragon1_diagonal(rotated_dragon)
                    elif direction == "dragon1_diagonal2":
                        rotated_dragon = pygame.transform.rotate(dragon_image.copy(), 135)
                        projectile_temp = dragon1_diagonal2(rotated_dragon)



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



                    elif direction == "sword2_vertical":
                        rotated_sword2 = pygame.transform.rotate(sword2_image.copy(), 180)
                        projectile_temp = sword2_vertical(rotated_sword2)
                    elif direction == "sword2_horizontal_left":
                        rotated_sword2 = pygame.transform.rotate(sword2_image.copy(), 270)
                        projectile_temp = sword2_horizontal_left(rotated_sword2)
                    elif direction == "sword2_horizontal_right":
                        rotated_sword2 = pygame.transform.rotate(sword2_image.copy(), 135)
                        projectile_temp = sword2_horizontal_right(rotated_sword2)
                    elif direction == "sword2_diagonal":
                        rotated_sword2 = pygame.transform.rotate(sword2_image.copy(), 270)
                        projectile_temp = sword2_diagonal(rotated_sword2)
                    elif direction == "sword2_diagonal2":
                        rotated_sword2 = pygame.transform.rotate(sword2_image.copy(), 180)
                        projectile_temp = sword2_diagonal2(rotated_sword2)


                    elif direction == "fireball_vertical":
                        rotated_fireball = pygame.transform.rotate(fireball_image.copy(), 180)
                        projectile_temp = fireball_vertical(rotated_fireball)
                    elif direction == "fireball_horizontal":
                        rotated_fireball = pygame.transform.rotate(fireball_image.copy(), 270)
                        projectile_temp = fireball_horizontal(rotated_fireball)
                    elif direction == "fireball_horizontal_right":
                        rotated_fireball = pygame.transform.rotate(fireball_image.copy(), 180)
                        projectile_temp = fireball_horizontal_right(rotated_fireball)

                    elif direction == "fireball_diagonal":
                        rotated_fireball = pygame.transform.rotate(fireball_image.copy(), -45)
                        projectile_temp = fireball_diagonal(rotated_fireball)
                    elif direction == "fireball_diagonal2":
                        rotated_fireball = pygame.transform.rotate(fireball_image.copy(), 225)
                        projectile_temp = fireball_diagonal2(rotated_fireball)



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

        # Проверка коллизий
        for projectile in projectiles:
            if projectile.rect.colliderect(player):
                attack_type = projectile.__class__.__name__.lower()
                damage = get_attack_damage(attack_type)
                health -= damage
                player.take_damage(damage)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    start_level()