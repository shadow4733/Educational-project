import pygame
def bg_music():
    pygame.mixer.music.load("sounds/BACKGROUND.mp3")  # музыка на фон
    pygame.mixer.music.play(-1, 0.0, 500)
    pygame.mixer.music.set_volume(0.05)
def jump():
    jumping = pygame.mixer.Sound("sounds/JUMP.ogg")
    jumping.play()
    jumping.set_volume(0.6)
def hit():
    hitting = pygame.mixer.Sound("sounds/HIT.ogg")
    hitting.play()
def run():
    pygame.mixer.music.load("sounds/RUN.ogg")
    pygame.mixer.music.play(0, 0.0, 500)
