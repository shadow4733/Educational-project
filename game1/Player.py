# Спрайт игрока
import pygame
from os import path
from game1.constant.constnants import HERO_COLOR, WIDTH, HEIGHT, HEALTH, HERO_SIZE

player_img = pygame.image.load(path.join("../images/hero/herosleva.png")).convert()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        #self.image.fill(HERO_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2 - HERO_SIZE // 2
        self.rect.centery = HEIGHT // 2 + 250 - HERO_SIZE // 2
        self.speedx = 0
        self.health = HEALTH

    def take_damage(self, damage):
        self.health -= damage