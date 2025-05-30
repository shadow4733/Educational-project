import os

import pygame

# Экран
HEALTH = 100
SCORE = 0
SCORE_TIMER = 0
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

# ФПС
FPS = 60

# Цвет
WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255,102,102)
LIGHT_PINK = (255,204,204)

# Герой
HERO_COLOR = (0, 255, 0)
HERO_SIZE = 32

# Кнопки главного меню
buttons = ["Начать сначала", "Выбрать уровень", "Выход"]

# Доступные уровни
levels = ["Уровень 1", "Уровень 2", "Уровень 3", "Уровень 4", "Уровень 5", "Уровень 6"]
selected_level = None
