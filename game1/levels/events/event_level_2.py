from game1.constant.constnants import WIDTH, HEIGHT

events = [
    # Мечи сверху
    (2, 1, (WIDTH // 2 - 230, 0), "drop"),
    (2.2, 1, (WIDTH // 2 - 200, 0), "drop"),
    (2.4, 1, (WIDTH // 2 - 170, 0), "drop"),
    (2.6, 1, (WIDTH // 2 - 140, 0), "drop"),
    (2.8, 1, (WIDTH // 2 - 110, 0), "drop"),
    (3, 1, (WIDTH // 2 - 80, 0), "drop"),
    (3.2, 1, (WIDTH // 2 - 50, 0), "drop"),
    (3.4, 1, (WIDTH // 2 - 20, 0), "drop"),
    (3.6, 1, (WIDTH // 2 + 10, 0), "drop"),
    (3.8, 1, (WIDTH // 2 + 40, 0), "drop"),
    (4, 1, (WIDTH // 2 + 70, 0), "drop"),
    (4.2, 1, (WIDTH // 2 + 100, 0), "drop"),
    (4.4, 1, (WIDTH // 2 + 130, 0), "drop"),
    (4.6, 1, (WIDTH // 2 + 160, 0), "drop"),
    ###
    # Мечи справа налево
    (2, 1, (WIDTH, HEIGHT // 2 + 30), "crocodile_right"),
    (2.2, 1, (WIDTH, HEIGHT // 2 + 60), "crocodile_right"),
    (2.4, 1, (WIDTH, HEIGHT // 2 + 90), "crocodile_right"),
    (2.6, 1, (WIDTH, HEIGHT // 2 + 120), "crocodile_right"),
    (2.8, 1, (WIDTH, HEIGHT // 2 + 150), "crocodile_right"),
    (3, 1, (WIDTH, HEIGHT // 2 + 180), "crocodile_right"),
    ###
    # Мечи слева направо
    (2.6, 1, (0, HEIGHT // 2 + 470), "crocodile_left"),
    (2.8, 1, (0, HEIGHT // 2 + 440), "crocodile_left"),
    (3, 1, (0, HEIGHT // 2 + 410), "crocodile_left"),
    (3.2, 1, (0, HEIGHT // 2 + 380), "crocodile_left"),
    (3.4, 1, (0, HEIGHT // 2 + 350), "crocodile_left"),
    (3.6, 1, (0, HEIGHT // 2 + 320), "crocodile_left"),

    # Пузыри
    (3.4, 1, (WIDTH // 2 - 200, HEIGHT), "bubble_vertical"),
    (3.5, 1, (WIDTH // 2 - 10, HEIGHT), "bubble_vertical"),
    (3.6, 1, (WIDTH // 2 - 140, HEIGHT), "bubble_vertical"),
    (3.6, 1, (WIDTH // 2 + 50, HEIGHT), "bubble_vertical"),
    (3.8, 1, (WIDTH // 2 - 60, HEIGHT), "bubble_vertical"),
    (4, 1, (WIDTH // 2 + 120, HEIGHT), "bubble_vertical"),
    (4.1, 1, (WIDTH // 2 + 180, HEIGHT), "bubble_vertical"),

    (5.5, 1, (WIDTH // 2 - 140, HEIGHT), "bubble_vertical"),
    (5.8, 1, (WIDTH // 2 - 70, HEIGHT), "bubble_vertical"),
    (6, 1, (WIDTH // 2 - 200, HEIGHT), "bubble_vertical"),
    (6, 1, (WIDTH // 2 + 50, HEIGHT), "bubble_vertical"),
    (6.3, 1, (WIDTH // 2 - 30, HEIGHT), "bubble_vertical"),
    (6.5, 1, (WIDTH // 2 + 10, HEIGHT), "bubble_vertical"),
    (6.7, 1, (WIDTH // 2 + 180, HEIGHT), "bubble_vertical"),

]