import pygame
def bg_music():
    pygame.mixer.music.load("sounds/CRAZYFROG.mp3")  # музыка на фон
    pygame.mixer.music.play(-1, 0.0, 500)
    pygame.mixer.music.set_volume(0.05)
def jump():
    jumping = pygame.mixer.Sound("sounds/JUMPNEW.MP3")
    jumping.play()
    jumping.set_volume(0.6)
def hit():
    hitting = pygame.mixer.Sound("sounds/HITNEW.MP3")
    hitting.play()
def run():
    pygame.mixer.music.load("sounds/RUN.ogg")
    pygame.mixer.music.play(0, 0.0, 500)
