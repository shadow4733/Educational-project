import pygame
import sys

from game1.Player import Player
from game1.constant.constnants import *
from game1.levels.attack import sword_vertical, sword_horizontal

pygame.init()

def start_level():
    """Уровень 2"""
    pygame.display.set_caption("Уровень 2")

    font = pygame.font.Font(None, 36)
    SCREEN.fill(BLACK)

    # Отображение текста
    level_text = font.render("Уровень 2", True, WHITE)
    level_text_rect = level_text.get_rect(center=(WIDTH // 2, HEIGHT - 950))  # Сдвигаем текст выше

    # Переменная для отслеживания здоровья героя
    health = HEALTH
    score = SCORE
    score_timer = SCORE_TIMER

    # Инициализация игрока
    player = Player()
    play_sprites = pygame.sprite.Group()
    play_sprites.add(player)

    # Группа спрайтов-проджектайлов (10 мечей вертикально)
    projectiles = pygame.sprite.Group()
    for i in range(10):
        projectile_temp = sword_vertical(pygame.image.load("../images/projectiles/sword1.png"))
        projectile_temp.image = pygame.transform.rotate(projectile_temp.image, 180) # Угол разворота
        projectiles.add(projectile_temp)

    # Группа спрайтов-проджектайлов (8 мечей горизонтально)
    for i in range(8):
        projectile_temp = sword_horizontal(pygame.image.load("../images/projectiles/sword1.png"))
        projectile_temp.image = pygame.transform.rotate(projectile_temp.image, 270) # Угол разворота
        projectiles.add(projectile_temp)

    pygame.display.flip()

    # Ждем события выхода или движения героя
    waiting = True
    while waiting:
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
        if player.rect.centerx - HERO_SIZE // 2 < WIDTH//2-245:
            player.rect.centerx = WIDTH//2-245 + HERO_SIZE // 2
        elif player.rect.centerx + HERO_SIZE // 2 > WIDTH//2+245:
            player.rect.centerx = WIDTH//2+245 - HERO_SIZE // 2
        if player.rect.centery - HERO_SIZE // 2 < HEIGHT//2+5:
            player.rect.centery = HEIGHT//2+5 + HERO_SIZE // 2
        elif player.rect.centery + HERO_SIZE // 2 > HEIGHT//2+495:
            player.rect.centery = HEIGHT//2+495 - HERO_SIZE // 2

    # Обновление экрана
        SCREEN.fill(BLACK)  # Перерисовываем экран
        SCREEN.blit(level_text, level_text_rect)  # Отображаем текст уровня снова

        # Отрисовываем игровую область (белый квадрат)
        pygame.draw.rect(SCREEN, WHITE,(WIDTH//2-250, HEIGHT//2, 500, 500), 5)

        # Отображение здоровья в левом верхнем углу
        health_text = font.render(f"Здоровье: {health}", True, WHITE)
        health_text_rect = health_text.get_rect(topleft=(60, 120))
        SCREEN.blit(health_text, health_text_rect)

        # Отображение очков в правом верхнем углу
        score_text = font.render(f"Очки: {score}", True, WHITE)
        score_text_rect = score_text.get_rect(topright=(WIDTH - 60, 120))
        SCREEN.blit(score_text, score_text_rect)

        # Таймер для таймингов
        clock = pygame.time.Clock()

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
                health -= 1


        pygame.display.flip()  # Обновляем экран
        pygame.time.Clock().tick(FPS)  # Ограничиваем FPS (60 кадров в секунду)

if __name__ == "__main__":
    start_level()