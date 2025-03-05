import pygame
import sys

from game1.Player import Player
from game1.constant.constnants import *
from game1.levels.attack import sword_vertical, sword_horizontal, dragon_vertical, get_attack_damage

pygame.init()

def start_level():
    """Уровень 1"""
    pygame.display.set_caption("Уровень 1")

    font = pygame.font.Font(None, 36)
    SCREEN.fill(BLACK)

    # Отображение текста
    level_text = font.render("Уровень 1", True, WHITE)
    level_text_rect = level_text.get_rect(center=(WIDTH // 2, HEIGHT - 950))  # Сдвигаем текст выше

    # Переменная для отслеживания здоровья героя
    health = HEALTH
    score = SCORE
    score_timer = SCORE_TIMER

    # Инициализация игрока
    player = Player()
    play_sprites = pygame.sprite.Group()
    play_sprites.add(player)

    # Группа спрайтов-проджектайлов
    projectiles = pygame.sprite.Group()

    events = [
        (2, 1, (WIDTH // 2 + 100, HEIGHT // 2 - 300), "sword_vertical"),
        (2, 1, (WIDTH // 2 + 150, HEIGHT // 2 - 300), "sword_vertical"),
        (2, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 300), "sword_vertical"),
        (2, 1, (WIDTH // 2, HEIGHT // 2 - 300), "sword_vertical"),
        (2, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 300), "sword_vertical"),
        (3, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 300), "sword_horizontal_left"),
        (3, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 350), "sword_horizontal_left"),
        (3, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 400), "sword_horizontal_left"),
        (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 100), "sword_horizontal_left"),
        (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 100), "sword_horizontal_left"),
        (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 100), "sword_horizontal_left"),
        (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 150), "sword_horizontal_left"),
        (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 200), "sword_horizontal_left"),
        (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 250), "sword_horizontal_left"),
        (6, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "sword_vertical"),
        (6, 1, (WIDTH // 2, HEIGHT // 2 - 300), "sword_vertical"),
        (6, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 300), "sword_vertical"),
        (6, 1, (WIDTH // 2 + 100, HEIGHT // 2 - 300), "sword_vertical"),
        (6, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 200), "sword_horizontal_left"),
        (6, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 250), "sword_horizontal_left"),
        (6, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 300), "sword_horizontal_left"),
        (7, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "dragon_vertical"),



        (8, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 400), "horizontal_left"),
        (9, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 200), "horizontal_left"),
        (9, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 200), "horizontal_left"),
        (11, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 270), "horizontal_left"),
        (12, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 350), "horizontal_left"),
    ]

    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()  # Время начала уровня

    pygame.display.flip()

    # Ждем события выхода или движения героя
    waiting = True
    while waiting:
        current_time = (pygame.time.get_ticks() - start_time) / 1000  # Текущее время в секундах

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False

        keys = pygame.key.get_pressed()  # Получаем состояние клавиш
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # Перемещение влево
            player.rect.centerx -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Перемещение вправо
            player.rect.centerx += 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:  # Перемещение вверх
            player.rect.centery -= 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:  # Перемещение вниз
            player.rect.centery += 5

        # Ограничение движения героя внутри игровой области
        if player.rect.centerx - HERO_SIZE // 2 < WIDTH // 2 - 245:
            player.rect.centerx = WIDTH // 2 - 245 + HERO_SIZE // 2
        elif player.rect.centerx + HERO_SIZE // 2 > WIDTH // 2 + 245:
            player.rect.centerx = WIDTH // 2 + 245 - HERO_SIZE // 2
        if player.rect.centery - HERO_SIZE // 2 < HEIGHT // 2 + 5:
            player.rect.centery = HEIGHT // 2 + 5 + HERO_SIZE // 2
        elif player.rect.centery + HERO_SIZE // 2 > HEIGHT // 2 + 495:
            player.rect.centery = HEIGHT // 2 + 495 - HERO_SIZE // 2

        # Загружаем изображение меча заранее
        sword_image = pygame.image.load("../images/projectiles/sword1.png")
        dragon_image = pygame.image.load("../images/projectiles/dragon.png")

        # Проверяем события
        for event in events[:]:
            event_time, num_swords, start_pos, direction = event
            if event_time <= current_time < event_time + 1:  # Проверяем, наступило ли время события
                for _ in range(num_swords):
                    # Выбираем направление меча
                    if direction == "sword_vertical":
                        rotated_sword = pygame.transform.rotate(sword_image.copy(), 180)
                        projectile_temp = sword_vertical(rotated_sword)
                    elif direction == "sword_horizontal_left":
                        rotated_sword = pygame.transform.rotate(sword_image.copy(), 270)
                        projectile_temp = sword_horizontal(rotated_sword)
                    elif direction == "dragon_vertical":
                        rotated_dragon = pygame.transform.rotate(dragon_image.copy(), 180)
                        projectile_temp = dragon_vertical(rotated_dragon)

                    # Устанавливаем начальные координаты меча
                    projectile_temp.rect = projectile_temp.image.get_rect(center=start_pos)
                    projectiles.add(projectile_temp)

                events.remove(event)

        # Удаляем мечи, которые вышли за пределы экрана
        for projectile in projectiles.sprites():
            if (projectile.rect.bottom < 0 or projectile.rect.top > HEIGHT or
                    projectile.rect.right < 0 or projectile.rect.left > WIDTH):
                projectile.kill()


        # Обновление экрана
        SCREEN.fill(BLACK)  # Перерисовываем экран
        SCREEN.blit(level_text, level_text_rect)  # Отображаем текст уровня снова

        # Отрисовываем игровую область (белый квадрат)
        pygame.draw.rect(SCREEN, WHITE, (WIDTH // 2 - 250, HEIGHT // 2, 500, 500), 5)

        # Отображение здоровья в левом верхнем углу
        health_text = font.render(f"Здоровье: {health}", True, WHITE)
        health_text_rect = health_text.get_rect(topleft=(60, 120))
        SCREEN.blit(health_text, health_text_rect)

        # Отображение очков в правом верхнем углу
        score_text = font.render(f"Очки: {score}", True, WHITE)
        score_text_rect = score_text.get_rect(topright=(WIDTH - 60, 120))
        SCREEN.blit(score_text, score_text_rect)

        # Таймер для начисления очков
        score_timer += 1
        if score_timer >= 60:  # 1 секунда (60 кадров)
            score_timer = 0
            score += 10  # Начисляем очки

        # Рисуем героя
        play_sprites.update()
        play_sprites.draw(SCREEN)

        # Обновляем и отрисовываем мечи
        projectiles.update()
        projectiles.draw(SCREEN)

        # Проверяем коллизию проджектайлов
        for projectile in projectiles:
            if projectile.rect.colliderect(player):
                attack_type = projectile.__class__.__name__.lower()
                damage = get_attack_damage(attack_type)
                health -= damage
                player.take_damage(damage)


        pygame.display.flip()  # Обновляем экран
        clock.tick(FPS)  # Ограничиваем FPS (60 кадров в секунду)

if __name__ == "__main__":
    start_level()