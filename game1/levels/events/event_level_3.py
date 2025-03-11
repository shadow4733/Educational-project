from game1.constant.constnants import WIDTH, HEIGHT

WHITE_RECT_X = WIDTH // 2 - 250
WHITE_RECT_Y = HEIGHT // 2
WHITE_RECT_WIDTH = 500
WHITE_RECT_HEIGHT = 500


# "topleft": (WHITE_RECT_X, WHITE_RECT_Y, 1, 1),  # Нижний правый угол
# "topright": (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y, -1, 1),  # Нижний левый угол
# "bottomleft": (WHITE_RECT_X, WHITE_RECT_Y + WHITE_RECT_HEIGHT, 1, -1),  # Верхний правый угол
# "bottomright": (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y + WHITE_RECT_HEIGHT, -1, -1), # Верхний левый угол



events = [
    (0.5, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "sword2_diagonal2"),
    (0.5, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword2_diagonal"),

    (1, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "dragon1_diagonal2"),
    (1, 1, (WHITE_RECT_X, WHITE_RECT_Y), "dragon1_diagonal"),

    (1.5, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "chicken_diagonal2"),
    (1.5, 1, (WHITE_RECT_X, WHITE_RECT_Y), "chicken_diagonal"),

    (1.8, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "fireball_diagonal2"),
    (1.8, 1, (WHITE_RECT_X, WHITE_RECT_Y), "fireball_diagonal"),

    (1.9, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "sword1_diagonal2"),
    (1.9, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword1_diagonal"),


    (2, 1, (WIDTH // 2, HEIGHT // 2 - 300), "sword1_vertical"),
    (2, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 300), "sword1_vertical"),
    (2, 1, (WIDTH // 2 + 100, HEIGHT // 2 - 300), "sword1_vertical"),
    (2, 1, (WIDTH // 2 + 150, HEIGHT // 2 - 300), "sword1_vertical"),
    (2, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 300), "sword1_vertical"),

    (3, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 350), "sword1_horizontal_left"),
    (3, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 400), "sword1_horizontal_left"),

    (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 100), "sword1_horizontal_left"),
    (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 100), "sword1_horizontal_left"),
    (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 100), "sword1_horizontal_left"),
    (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 150), "sword1_horizontal_left"),
    (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 200), "sword1_horizontal_left"),
    (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 250), "sword1_horizontal_left"),

    (6, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "sword1_vertical"),
    (6, 1, (WIDTH // 2, HEIGHT // 2 - 300), "sword1_vertical"),
    (6, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 300), "sword1_vertical"),
    (6, 1, (WIDTH // 2 + 100, HEIGHT // 2 - 300), "sword1_vertical"),
    (6, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 200), "sword1_horizontal_left"),
    (6, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 250), "sword1_horizontal_left"),
    (6, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 300), "sword1_horizontal_left"),

    (7, 1, (WIDTH // 2 - 100, HEIGHT // 2 - 200), "dragon_vertical"),
    (7, 1, (WIDTH // 2 - 400, HEIGHT // 2 + 200), "dragon_horizontal"),

    (8, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "chicken_vertical"),
    (8, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 300), "chicken_horizontal"),

    (9, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "sword1_diagonal2"),
    (9, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword1_diagonal"),

    (10, 1, (WIDTH // 2-200, HEIGHT // 2 - 250), "dragon_vertical"),
    (10, 1, (WIDTH // 2, HEIGHT // 2 - 250), "dragon_vertical"),
    (10, 1, (WIDTH // 2+200, HEIGHT // 2 - 250), "dragon_vertical"),
    (10, 1, (WIDTH // 2-300, HEIGHT // 2+50), "dragon_horizontal"),
    (10, 1, (WIDTH // 2-300, HEIGHT // 2+250), "dragon_horizontal"),
    (10, 1, (WIDTH // 2-300, HEIGHT // 2+450), "dragon_horizontal"),

    (13, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "fireball_vertical"),
    (13, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 300), "fireball_horizontal")
]