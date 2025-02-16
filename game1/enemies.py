import pygame

class Enemy:
    def __init__(self, x, y, hp, damage):
        self.rect = pygame.Rect(x, y, 50, 50)  # Прямоугольник для представления врага
        self.hp = hp  # Количество здоровья
        self.damage = damage  # Урон, который враг наносит
        self.alive = True  # Состояние врага

    def attack(self, target):
        if self.alive:
            target.take_damage(self.damage)
            print(f"Enemy attacks! Dealt {self.damage} damage to target.")

    def take_damage(self, amount):
        if self.alive:
            self.hp -= amount
            print(f"Enemy took {amount} damage. Remaining HP: {self.hp}")
            if self.hp <= 0:
                self.alive = False
                print("Enemy has been defeated!")

    def draw(self, screen):
        # Рисуем врага на экране (можно заменить на изображение)
        color = (255, 0, 0) if self.alive else (128, 128, 128)  # Красный, если жив, серый, если мертв
        pygame.draw.rect(screen, color, self.rect)