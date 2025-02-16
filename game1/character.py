import pygame
import math

class Character:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.Surface((30, 50))  # Создание поверхности для персонажа
        self.image.fill((0, 255, 0))  # Заливка красным цветом для видимости
        self.rect = self.image.get_rect(center=(960, 790))  # Центрирование на экране
        self.velocity_y = 0  # Вертикальная скорость для прыжка
        self.is_jumping = False  # Флаг, указывающий, находится ли персонаж в прыжке
        self.gravity = 1400  # Сила гравитации
        self.jump_strength = -600  # Сила прыжка (отрицательное значение для движения вверх)
        self.is_attacking = False  # Флаг атаки
        self.attack_duration = 0.5  # Продолжительность атаки в секундах
        self.attack_timer = 0  # Таймер для отслеживания времени атаки

        # Добавление атрибутов здоровья и урона
        self.health = 100  # Начальное количество здоровья
        self.damage = 20  # Урон, наносимый атакой

    def output(self, enemies_list):  # Добавляем аргумент enemies_list
        self.screen.blit(self.image, self.rect)  # Рисуем персонажа на экране
        if self.is_attacking:  # Если персонаж атакует, рисуем полуокружность
            self.attack(enemies_list)  # Передаем список врагов в метод attack

    def move(self, keys, delta_time, area_rect, enemies):
        speed = 200 * delta_time  # Устанавливаем скорость, умноженную на delta_time для плавности

        # Управление прыжком
        if keys[pygame.K_SPACE] and not self.is_jumping:  # Прыжок при нажатии пробела
            self.is_jumping = True
            self.velocity_y = self.jump_strength

        # Применение гравитации
        if self.is_jumping:
            self.velocity_y += self.gravity * delta_time  # Увеличиваем скорость падения
            self.rect.y += self.velocity_y * delta_time  # Перемещаем персонажа по вертикали

        # Проверка на приземление
        if self.rect.bottom >= area_rect.bottom:
            self.rect.bottom = area_rect.bottom  # Устанавливаем персонажа на землю
            self.is_jumping = False  # Персонаж больше не в прыжке
            self.velocity_y = 0  # Сбрасываем вертикальную скорость

        # Движение влево и вправо
        if keys[pygame.K_a]:  # Движение влево
            self.rect.x -= speed
        if keys[pygame.K_d]:  # Движение вправо
            self.rect.x += speed

        # Атака при нажатии левой кнопки мыши
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0] and not self.is_attacking:  # Если атака не активна
            self.is_attacking = True
            self.attack_timer = self.attack_duration  # Сбрасываем таймер атаки
            self.attack(enemies)  # Вызываем метод атаки и передаем список врагов

        # Обновляем таймер атаки
        if self.is_attacking:
            self.attack_timer -= delta_time
            if self.attack_timer <= 0:  # Если время атаки истекло
                self.is_attacking = False  # Сбрасываем флаг атаки

        # Ограничение движения в пределах игровой области
        self.rect.clamp_ip(area_rect)  # Ограничиваем движения персонажа в области

    def attack(self, enemies):
        # Создание радиуса атаки
        attack_radius = 50  # Радиус атаки
        attack_angle = math.pi  # Угол полуокружности (180 градусов)

        # Получаем координаты курсора мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Получаем координаты центра персонажа
        center_x = self.rect.centerx
        center_y = self.rect.centery

        # Вычисляем угол между персонажем и курсором
        angle = math.atan2(mouse_y - center_y, mouse_x - center_x)

        # Создаем поверхность для атаки
        attack_surface = pygame.Surface((attack_radius * 2, attack_radius * 2), pygame.SRCALPHA)
        attack_surface.fill((0, 0, 0, 0))  # Заполняем прозрачным цветом

        # Рисуем дугу на поверхности атаки (полуокружность)
        pygame.draw.arc(attack_surface, (0, 255, 0), (0, 0, attack_radius * 2, attack_radius * 2),
                        math.pi * 1.65, 0, 5)  # Зелёная полуокружность

        # Поворачиваем поверхность атаки на нужный угол
        attack_surface = pygame.transform.rotate(attack_surface, -math.degrees(angle))

        # Получаем прямоугольник поверхности после поворота
        rotated_rect = attack_surface.get_rect(center=(center_x, center_y))

        # Рисуем атаку на экране
        self.screen.blit(attack_surface, rotated_rect.topleft)

        # Проверка на столкновение с врагами
        for enemy in enemies:
            if enemy.alive and rotated_rect.colliderect(enemy.rect):  # Если враг жив и атака пересекается с врагом
                enemy.take_damage(self.damage)  # Наносим урон врагу
                print("Enemy hit!")  # Для отладки