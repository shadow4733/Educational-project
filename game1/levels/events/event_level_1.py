from game1.constant.constnants import WIDTH, HEIGHT

WHITE_RECT_X = WIDTH // 2 - 250
WHITE_RECT_Y = HEIGHT // 2
WHITE_RECT_WIDTH = 500
WHITE_RECT_HEIGHT = 500

events = [

    (2, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "sword1_diagonal2"),
    (2, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword1_diagonal"),

    (4, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "sword1_diagonal2"),
    (4, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword1_diagonal"),

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


    (5, 1, (WIDTH // 200, HEIGHT // 2 + 50), "long_sword_horizontal"),
    (5, 1, (WIDTH // 200, HEIGHT // 2 + 100), "long_sword_horizontal"),
    (5, 1, (WIDTH // 200, HEIGHT // 2 + 150), "long_sword_horizontal"),
    (5, 1, (WIDTH // 200, HEIGHT // 2 + 200), "long_sword_horizontal"),
    (5, 1, (WIDTH // 200, HEIGHT // 2 + 250), "long_sword_horizontal"),

    (6, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "sword1_vertical"),
    (6, 1, (WIDTH // 2 + 0, HEIGHT // 2 - 300), "sword1_vertical"),
    (6, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 300), "sword1_vertical"),
    (6, 1, (WIDTH // 2 + 100, HEIGHT // 2 - 300), "sword1_vertical"),

    (8.5, 1, (WIDTH // 200, HEIGHT // 2 + 300), "chicken_horizontal"),

    (9, 1, (WIDTH // 2 - 200, HEIGHT // 2 - 400), "gas_vertical"),
    (9, 1, (WIDTH // 2, HEIGHT // 2 - 400), "gas_vertical"),
    (9, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 400), "gas_vertical"),
    (9, 1, (WIDTH // 200, HEIGHT // 2+50), "gas_horizontal"),
    (9, 1, (WIDTH // 200, HEIGHT // 2+250), "gas_horizontal"),
    (9, 1, (WIDTH // 200, HEIGHT // 2+450), "gas_horizontal"),

    (10, 1, (WIDTH // 2 + 700, HEIGHT // 2 + 200), "sword2_horizontal_right"),
    (10.5, 1, (WIDTH // 2 + 700, HEIGHT // 2 + 250), "sword2_horizontal_right"),
    (11, 1, (WIDTH // 2 + 700, HEIGHT // 2 + 300), "sword2_horizontal_right"),
    (11.5, 1, (WIDTH // 2 + 700, HEIGHT // 2 + 350), "sword2_horizontal_right"),
    (12, 1, (WIDTH // 2 + 700, HEIGHT // 2 + 400), "sword2_horizontal_right"),

    (13, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 400), "sword1_vertical"),
    (13.5, 1, (WIDTH // 2 + 150, HEIGHT // 2 - 400), "sword1_vertical"),
    (14, 1, (WIDTH // 2 + 100, HEIGHT // 2 - 400), "sword1_vertical"),
    (14.5, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 400), "sword1_vertical"),
    (15, 1, (WIDTH // 2 , HEIGHT // 2 - 400), "sword1_vertical"),
    (15.5, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 400), "sword1_vertical"),
    (16, 1, (WIDTH // 2 - 100, HEIGHT // 2 - 400), "sword1_vertical"),
    (16.5, 1, (WIDTH // 2 - 150, HEIGHT // 2 - 400), "sword1_vertical"),

    (17.3, 1, (WIDTH // 2 - 80, HEIGHT), "bubble_vertical"),
    (17.6, 1, (WIDTH // 2 + 120, HEIGHT), "bubble_vertical"),
    (17.9, 1, (WIDTH // 2, HEIGHT), "bubble_vertical"),
    (18, 1, (WIDTH // 2 - 150, HEIGHT), "bubble_vertical"),
    (18.5, 1, (WIDTH // 2 + 200, HEIGHT), "bubble_vertical"),

    (19, 1, (WIDTH // 200, HEIGHT // 2 + 100), "long_sword_horizontal"),
    (19.2, 1, (WIDTH // 200, HEIGHT // 2 + 150), "long_sword_horizontal"),
    (19.4, 1, (WIDTH // 200, HEIGHT // 2 + 200), "long_sword_horizontal"),
    (19.6, 1, (WIDTH // 200, HEIGHT // 2 + 250), "long_sword_horizontal"),

    (21, 1, (WIDTH // 200, HEIGHT // 2 + 100), "chicken_horizontal"),

    (22, 1, (WIDTH // 200, HEIGHT // 2 + 240), "sword2_horizontal_left"),
    (22.5, 1, (WIDTH // 200, HEIGHT // 2 + 290), "sword2_horizontal_left"),
    (23, 1, (WIDTH // 200, HEIGHT // 2 + 340), "sword2_horizontal_left"),
    (23.5, 1, (WIDTH // 200, HEIGHT // 2 + 390), "sword2_horizontal_left"),

    (24, 1, (WIDTH // 2 - 250, HEIGHT // 2 - 400), "gas_vertical"),
    (24.3, 1, (WIDTH // 2 - 100, HEIGHT // 2 - 400), "gas_vertical"),
    (24.6, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 400), "gas_vertical"),

    (25, 1, (WIDTH // 200, HEIGHT // 2 + 100), "gas_horizontal"),
    (25.2, 1, (WIDTH // 200, HEIGHT // 2 + 300), "gas_horizontal"),
    (25.4, 1, (WIDTH // 200, HEIGHT // 2 + 500), "gas_horizontal"),

    (26, 1, (WIDTH // 2 + 300, HEIGHT // 2 + 150), "chicken_horizontal"),

    (28.5, 1, (WIDTH // 200, HEIGHT // 2 + 50), "long_sword_horizontal"),
    (28.7, 1, (WIDTH // 200, HEIGHT // 2 + 100), "long_sword_horizontal"),
    (28.9, 1, (WIDTH // 200, HEIGHT // 2 + 150), "long_sword_horizontal"),
    (29.1, 1, (WIDTH // 200, HEIGHT // 2 + 200), "long_sword_horizontal"),

    (30, 1, (WIDTH // 2 - 200, HEIGHT), "bubble_vertical"),
    (30.3, 1, (WIDTH // 2, HEIGHT), "bubble_vertical"),
    (30.6, 1, (WIDTH // 2 + 200, HEIGHT), "bubble_vertical"),

    (31, 1, (WIDTH // 2 + 700, HEIGHT // 2 + 200), "sword2_horizontal_right"),
    (31.5, 1, (WIDTH // 2 + 700, HEIGHT // 2 + 250), "sword2_horizontal_right"),

    (33, 1, (WIDTH // 200, HEIGHT // 2 + 150), "gas_horizontal"),
    (33.2, 1, (WIDTH // 200, HEIGHT // 2 + 350), "gas_horizontal"),

    (34, 1, (WIDTH // 2, HEIGHT // 2 - 400), "sword1_vertical"),
    (34.3, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 400), "sword1_vertical"),
    (34.6, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 400), "sword1_vertical"),

    (36, 1, (WIDTH // 2 - 120, HEIGHT), "bubble_vertical"),
    (36.2, 1, (WIDTH // 2 + 70, HEIGHT), "bubble_vertical"),
    (36.5, 1, (WIDTH // 2 + 180, HEIGHT), "bubble_vertical"),

    (37.5, 1, (WIDTH // 200, HEIGHT // 2 + 100), "long_sword_horizontal"),
    (37.8, 1, (WIDTH // 200, HEIGHT // 2 + 150), "long_sword_horizontal"),
    (38.1, 1, (WIDTH // 200, HEIGHT // 2 + 200), "long_sword_horizontal"),

    (40, 1, (WIDTH // 2 + 300, HEIGHT // 2 - 400), "gas_vertical"),
    (40.5, 1, (WIDTH // 2 + 100, HEIGHT // 2 - 400), "gas_vertical"),
    (41, 1, (WIDTH // 2 - 100, HEIGHT // 2 - 400), "gas_vertical"),

    (42.5, 1, (WIDTH // 200, HEIGHT // 2 + 300), "chicken_horizontal"),
    (43, 1, (WIDTH // 2 + 700, HEIGHT // 2 + 200), "sword2_horizontal_right"),
    (43.5, 1, (WIDTH // 2 + 700, HEIGHT // 2 + 250), "sword2_horizontal_right"),

    (45, 1, (WIDTH // 2 - 250, HEIGHT), "bubble_vertical"),
    (45.3, 1, (WIDTH // 2 - 50, HEIGHT), "bubble_vertical"),
    (45.6, 1, (WIDTH // 2 + 150, HEIGHT), "bubble_vertical"),

    (47, 1, (WIDTH // 200, HEIGHT // 2 + 100), "sword2_horizontal_left"),
    (47.3, 1, (WIDTH // 200, HEIGHT // 2 + 150), "sword2_horizontal_left"),
    (47.6, 1, (WIDTH // 200, HEIGHT // 2 + 200), "sword2_horizontal_left"),

    (49, 1, (WIDTH // 2 + 300, HEIGHT // 2 + 150), "chicken_horizontal"),

    (50, 1, (WIDTH // 2 - 100, HEIGHT // 2 - 400), "sword1_vertical"),
    (50.4, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 400), "sword1_vertical"),
    (50.4, 1, (WIDTH // 2, HEIGHT // 2 - 400), "sword1_vertical"),
    (50.8, 1, (WIDTH // 2 + 100, HEIGHT // 2 - 400), "sword1_vertical"),
    (51.2, 1, (WIDTH // 2 + 150, HEIGHT // 2 - 400), "sword1_vertical"),

    (52, 1, (WIDTH // 2 - 180, HEIGHT), "bubble_vertical"),
    (52.3, 1, (WIDTH // 2 - 20, HEIGHT), "bubble_vertical"),
    (52.6, 1, (WIDTH // 2 + 200, HEIGHT), "bubble_vertical"),

    (54, 1, (WIDTH // 200, HEIGHT // 2 + 120), "long_sword_horizontal"),
    (54.3, 1, (WIDTH // 200, HEIGHT // 2 + 180), "long_sword_horizontal"),
    (54.6, 1, (WIDTH // 200, HEIGHT // 2 + 240), "long_sword_horizontal"),

    (56, 1, (WIDTH // 2 - 250, HEIGHT // 2 - 400), "gas_vertical"),
    (56.3, 1, (WIDTH // 2, HEIGHT // 2 - 400), "gas_vertical"),
    (56.6, 1, (WIDTH // 2 + 250, HEIGHT // 2 - 400), "gas_vertical"),

    (58, 1, (WIDTH // 200, HEIGHT // 2 + 300), "chicken_horizontal"),

    (59.5, 1, (WIDTH // 2 - 50, HEIGHT), "bubble_vertical"),
    (59.8, 1, (WIDTH // 2 + 100, HEIGHT), "bubble_vertical"),
]