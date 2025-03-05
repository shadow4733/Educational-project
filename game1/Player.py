# Спрайт игрока
import pygame

from game1.constant.constnants import HERO_COLOR, WIDTH, HEIGHT, HEALTH, HERO_SIZE

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((HERO_SIZE, HERO_SIZE))
        self.image.fill(HERO_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2 - HERO_SIZE // 2
        self.rect.centery = HEIGHT // 2 + 250 - HERO_SIZE // 2
        self.speedx = 0
        self.health = HEALTH

    def take_damage(self, damage):
        self.health -= damage