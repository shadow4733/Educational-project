import random
import pygame
from game1.constant.constnants import HEIGHT, WIDTH

# Спрайт для вертикально летящих мечей
class sword_vertical(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(700, 1200)
        self.rect.y = random.randrange(-200, -70)
        self.speedy = 12

    def reset_position(self):
        self.rect.x = random.randrange(500, 1400)
        self.rect.y = random.randrange(-200, -70)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 50:
            self.reset_position()
            self.speedy = 1

# Спрайт для горизонтально летящих мечей
class sword_horizontal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-200, -70)
        self.rect.y = random.randrange(500, 1000)
        self.speedx = 12

    def reset_position(self):
        self.rect.x = random.randrange(-200, -70)
        self.rect.y = random.randrange(500, 1000)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > WIDTH + 80:
            self.reset_position()
            self.speedx = 1
