from game1.constant.constnants import WIDTH, HEIGHT

events = [
    # Мечи сверху
    (2, 1, (WIDTH // 2 - 230, 0), "sword1_vertical"),
    (2.2, 1, (WIDTH // 2 - 200, 0), "sword1_vertical"),
    (2.4, 1, (WIDTH // 2 - 170, 0), "sword1_vertical"),
    (2.6, 1, (WIDTH // 2 - 140, 0), "sword1_vertical"),
    (2.8, 1, (WIDTH // 2 - 110, 0), "sword1_vertical"),
    (3, 1, (WIDTH // 2 - 80, 0), "sword1_vertical"),
    (3.2, 1, (WIDTH // 2 - 50, 0), "sword1_vertical"),
    (3.4, 1, (WIDTH // 2 - 20, 0), "sword1_vertical"),
    (3.6, 1, (WIDTH // 2 + 10, 0), "sword1_vertical"),
    (3.8, 1, (WIDTH // 2 + 40, 0), "sword1_vertical"),
    (4, 1, (WIDTH // 2 + 70, 0), "sword1_vertical"),
    (4.2, 1, (WIDTH // 2 + 100, 0), "sword1_vertical"),
    (4.4, 1, (WIDTH // 2 + 130, 0), "sword1_vertical"),
    (4.6, 1, (WIDTH // 2 + 160, 0), "sword1_vertical"),
    ###
    # Мечи справа налево
    (2, 1, (WIDTH, HEIGHT // 2 + 30), "sword1_horizontal_right"),
    (2.2, 1, (WIDTH, HEIGHT // 2 + 60), "sword1_horizontal_right"),
    (2.4, 1, (WIDTH, HEIGHT // 2 + 90), "sword1_horizontal_right"),
    (2.6, 1, (WIDTH, HEIGHT // 2 + 120), "sword1_horizontal_right"),
    (2.8, 1, (WIDTH, HEIGHT // 2 + 150), "sword1_horizontal_right"),
    (3, 1, (WIDTH, HEIGHT // 2 + 180), "sword1_horizontal_right"),
    ###
    # Мечи слева направо
    (2.6, 1, (0, HEIGHT // 2 + 470), "sword1_horizontal_left"),
    (2.8, 1, (0, HEIGHT // 2 + 440), "sword1_horizontal_left"),
    (3, 1, (0, HEIGHT // 2 + 410), "sword1_horizontal_left"),
    (3.2, 1, (0, HEIGHT // 2 + 380), "sword1_horizontal_left"),
    (3.4, 1, (0, HEIGHT // 2 + 350), "sword1_horizontal_left"),
    (3.6, 1, (0, HEIGHT // 2 + 320), "sword1_horizontal_left"),
]