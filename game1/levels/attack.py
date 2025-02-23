import random

import pygame

from game1.constant.constnants import HEIGHT, WIDTH


# Спрайт для вертикально летящих мечей
class sword_vertical(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load("../images/projectiles/sword1.png")
        #self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(700,  1200)
        self.rect.y = random.randrange(-200, -70)
        self.speedy = 15

    # Возвращение проджектайлов на исходные позиции
    def reset_position(self):
        self.rect.x = random.randrange(500,  1400)
        self.rect.y = random.randrange(-200, -70)  # Начало падения мечей за пределами видимости

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 50:
            self.reset_position()
            self.speedy = 15

# Спрайт для горизонтально летящих мечей
class sword_horizontal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load("../images/projectiles/sword1.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-200,  -70)
        self.rect.y = random.randrange(500, 1000)
        self.speedy = 20

    # Возвращение проджектайлов на исходные позиции
    def reset_position(self):
        self.rect.x = random.randrange(-200, -70)
        self.rect.y = random.randrange(500, 1000)  # Начало движения мечей за пределами видимости

    def update(self):
        self.rect.x += self.speedy
        if self.rect.left > WIDTH + 80:
            self.reset_position()
            self.speedy = 20
