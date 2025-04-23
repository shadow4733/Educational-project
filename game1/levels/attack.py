import random
import pygame
from game1.constant.constnants import HEIGHT, WIDTH

ATTACK_DAMAGE = {
    "sword1_vertical": 7,
    "sword1_horizontal_left": 7,
    "sword1_horizontal_right": 7,
    "sword1_diagonal":7,
    "sword1_diagonal2":7,

    "dragon_vertical": 30,
    "dragon_horizontal": 30,
    "dragon_horizontal_right": 30,
    "dragon1_diagonal":30,
    "dragon1_diagonal2":30,

    "chicken_vertical": -20,
    "chicken_horizontal": -20,
    "chicken_horizontal_right": -20,
    "chicken_diagonal":-20,
    "chicken_diagonal2":-20,

    "sword2_vertical": 10,
    "sword2_horizontal_left": 10,
    "sword2_horizontal_right": 10,
    "sword2_diagonal": 10,
    "sword2_diagonal2": 10,

    "fireball_vertical": 20,
    "fireball_horizontal": 20,
    "fireball_horizontal_right": 20,
    "fireball_diagonal": 20,
    "fireball_diagonal2": 20,

    "bubble_vertical": 3,

    "gas_vertical": 15,
    "gas_horizontal_left": 15,
    "gas_horizontal_right": 15,
    "gas_diagonal": 15,
    "gas_diagonal2": 15,

    "long_sword_vertical": 10,
    "long_sword_horizontal_left": 10,
    "long_sword_horizontal_right": 10,
    "long_sword_diagonal": 10,
    "long_sword_diagonal2": 10,
}

def get_attack_damage(attack_type):
    """Получить урон для определенного типа атаки"""
    return ATTACK_DAMAGE.get(attack_type, 0)

# Спрайт для вертикально летящих мечей
class sword1_vertical(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 12

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 50:
            self.speedy = 1

# Спрайт для вертикально летящих пузырей (вверх)
class bubble_vertical(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 1

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.top > HEIGHT + 50:
            self.speedy = 1

# Спрайт для горизонтально летящих мечей
class sword1_horizontal_left(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedx = 12  # Скорость движения по оси x

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x += self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место

class sword1_horizontal_right(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedx = 12  # Скорость движения по оси x

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x -= self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место

class sword1_diagonal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9  # Скорость по вертикали
        self.speedx = 9  # Скорость по горизонтали (добавлено)
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50: # обработка края экрана
            self.kill()

class sword1_diagonal2(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9
        self.speedx = -9
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50: # обработка края экрана
            self.kill()

# Спрайт для вертикально летящих драконов
class dragon_vertical(pygame.sprite.Sprite):
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

# Спрайт для горизонтально летящих драконов
class dragon_horizontal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-200, -70)
        self.rect.y = random.randrange(500, 1000)
        self.speedx = 12  # Скорость движения по оси x

    def reset_position(self):
        self.rect.x = random.randrange(-200, -70)
        self.rect.y = random.randrange(500, 1000)

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x += self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место
        if self.rect.left > WIDTH + 80:
            self.reset_position()

class dragon_horizontal_right(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedx = 12  # Скорость движения по оси x

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x -= self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место


class dragon1_diagonal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9  # Скорость по вертикали
        self.speedx = 9  # Скорость по горизонтали (добавлено)
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50: # обработка края экрана
            self.kill()

class dragon1_diagonal2(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9
        self.speedx = -9
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50: # обработка края экрана
            self.kill()

# Спрайт для вертикально летящей курицы
class chicken_vertical(pygame.sprite.Sprite):
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

# Спрайт для горизонтально летящей курицы
class chicken_horizontal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-200, -70)
        self.rect.y = random.randrange(500, 1000)
        self.speedx = 12  # Скорость движения по оси x

    def reset_position(self):
        self.rect.x = random.randrange(-200, -70)
        self.rect.y = random.randrange(500, 1000)

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x += self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место
        if self.rect.left > WIDTH + 80:
            self.reset_position()

class chicken_horizontal_right(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedx = 12  # Скорость движения по оси x

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x -= self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место

class chicken_diagonal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9  # Скорость по вертикали
        self.speedx = 9  # Скорость по горизонтали (добавлено)
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50: # обработка края экрана
            self.kill()

class chicken_diagonal2(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9
        self.speedx = -9
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50: # обработка края экрана
            self.kill()

# Спрайт для вертикально летящих мечей2
class sword2_vertical(pygame.sprite.Sprite):
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

# Спрайт для горизонтально летящих мечей2
class sword2_horizontal_left(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-200, -70)
        self.rect.y = random.randrange(500, 1000)
        self.speedx = 12  # Скорость движения по оси x

    def reset_position(self):
        self.rect.x = random.randrange(-200, -70)
        self.rect.y = random.randrange(500, 1000)

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x += self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место
        if self.rect.left > WIDTH + 80:
            self.reset_position()

class sword2_horizontal_right(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedx = 12  # Скорость движения по оси x

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x -= self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место

class sword2_diagonal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9  # Скорость по вертикали
        self.speedx = 9  # Скорость по горизонтали (добавлено)
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50:  # обработка края экрана
            self.kill()

class sword2_diagonal2(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9
        self.speedx = -9
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50:  # обработка края экрана
            self.kill()


# Спрайт для вертикально летящего фаербола
class fireball_vertical(pygame.sprite.Sprite):
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

# Спрайт для горизонтально летящего фаербола
class fireball_horizontal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-200, -70)
        self.rect.y = random.randrange(500, 1000)
        self.speedx = 12  # Скорость движения по оси x

    def reset_position(self):
        self.rect.x = random.randrange(-200, -70)
        self.rect.y = random.randrange(500, 1000)

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x += self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место
        if self.rect.left > WIDTH + 80:
            self.reset_position()

class fireball_horizontal_right(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedx = 12  # Скорость движения по оси x

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x -= self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место


class fireball_diagonal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9  # Скорость по вертикали
        self.speedx = 9  # Скорость по горизонтали (добавлено)
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50:  # обработка края экрана
            self.kill()

class fireball_diagonal2(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9
        self.speedx = -9
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50:  # обработка края экрана
            self.kill()

# Спрайт для вертикально летящего gas
class gas_vertical(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 12

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 50:
            self.speedy = 1

# Спрайт для горизонтально летящего gas
class gas_horizontal_left(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedx = 12  # Скорость движения по оси x

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x += self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место

class gas_horizontal_right(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedx = 12  # Скорость движения по оси x

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x -= self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место

class gas_diagonal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9  # Скорость по вертикали
        self.speedx = 9  # Скорость по горизонтали (добавлено)
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50: # обработка края экрана
            self.kill()

class gas_diagonal2(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9
        self.speedx = -9
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50: # обработка края экрана
            self.kill()

class long_sword_vertical(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 12

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 50:
            self.speedy = 1

class long_sword_horizontal_left(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedx = 12  # Скорость движения по оси x

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x += self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место

class long_sword_horizontal_right(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedx = 12  # Скорость движения по оси x

    def update(self):
        # Обновляем позицию объекта, двигаясь по оси x
        self.rect.x -= self.speedx
        # Если объект выходит за пределы экрана, сбрасываем его на новое место

class long_sword_diagonal(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9  # Скорость по вертикали
        self.speedx = 9  # Скорость по горизонтали (добавлено)
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50: # обработка края экрана
            self.kill()

class long_sword_diagonal2(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image  # Используем переданное изображение
        self.rect = self.image.get_rect()
        self.speedy = 9
        self.speedx = -9
        self.rect.center = (WIDTH // 2 - 250, HEIGHT // 2)  # начальная позиция, можно задавать тут

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx  # Движение по горизонтали
        if self.rect.top > HEIGHT + 50 or self.rect.left < -50 or self.rect.right > WIDTH + 50: # обработка края экрана
            self.kill()