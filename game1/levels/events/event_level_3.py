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

    (1, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "dragon1_diagonal2"),
    (1, 1, (WHITE_RECT_X, WHITE_RECT_Y), "dragon1_diagonal"),

    (1.5, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "chicken_diagonal2"),
    (1.5, 1, (WHITE_RECT_X, WHITE_RECT_Y), "chicken_diagonal"),

    (1.9, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "sword1_diagonal2"),
    (1.9, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword1_diagonal"),


    (2, 1, (WIDTH // 2, HEIGHT // 2 - 300), "sword1_vertical"),
    (2, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 300), "sword1_vertical"),
    (2, 1, (WIDTH // 2 + 100, HEIGHT // 2 - 300), "sword1_vertical"),
    (2, 1, (WIDTH // 2 + 150, HEIGHT // 2 - 300), "sword1_vertical"),
    (2, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 300), "sword1_vertical"),

    (2.5, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 60), "sword1_horizontal_right"),
    (2.5, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 160), "sword1_horizontal_right"),
    (2.5, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 270), "sword1_horizontal_right"),


    (3, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 350), "sword1_horizontal_left"),
    (3, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 400), "sword1_horizontal_left"),

    (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 40), "sword1_horizontal_left"),
    (5, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 90), "sword1_horizontal_left"),
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
    (13, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 300), "fireball_horizontal"),

    (14.5, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 60), "sword1_horizontal_right"),
    (14.5, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 160), "sword1_horizontal_right"),
    (14.5, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 300), "sword1_horizontal_right"),

    (15, 1, (WIDTH // 2, HEIGHT // 2 - 300), "sword1_vertical"),
    (15, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 300), "sword1_vertical"),
    (15, 1, (WIDTH // 2 + 100, HEIGHT // 2 - 300), "sword1_vertical"),
    (15, 1, (WIDTH // 2 + 150, HEIGHT // 2 - 300), "sword1_vertical"),
    (15, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 300), "sword1_vertical"),

    (16, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "dragon1_diagonal2"),
    (16, 1, (WHITE_RECT_X, WHITE_RECT_Y), "dragon1_diagonal"),
    (16, 1, (WIDTH // 2 - 150, HEIGHT // 2 - 300), "sword1_vertical"),
    (16, 1, (WIDTH // 2 + 150, HEIGHT // 2 - 300), "sword1_vertical"),

    (17, 1, (WIDTH // 2-300, HEIGHT // 2+50), "dragon_horizontal"),
    (17, 1, (WIDTH // 2-300, HEIGHT // 2+250), "dragon_horizontal"),
    (17, 1, (WIDTH // 2-300, HEIGHT // 2+450), "dragon_horizontal"),

    (18, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 60), "fireball_horizontal_right"),
    (18, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 160), "fireball_horizontal_right"),
    (18, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 270), "fireball_horizontal_right"),
    (18, 1,  (WIDTH // 2 - 100, HEIGHT // 2 - 300), "sword1_vertical"),
    (18, 1, (WIDTH // 2 - 150, HEIGHT // 2 - 300), "sword1_vertical"),
    (18, 1, (WIDTH // 2 - 200, HEIGHT // 2 - 300), "sword1_vertical"),

    (19, 1, (WIDTH // 2, HEIGHT // 2 - 300), "sword1_vertical"),
    (19, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 300), "sword1_vertical"),
    (19, 1,  (WIDTH // 2 - 50, HEIGHT // 2 - 300), "sword1_vertical"),
    (19, 1,  (WIDTH // 2 - 150, HEIGHT // 2 - 300), "sword1_vertical"),

    (20, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 40), "sword1_horizontal_left"),
    (20, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 90), "sword1_horizontal_left"),
    (20, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 140), "sword1_horizontal_left"),

    (21, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 40), "sword1_horizontal_right"),
    (21, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 90), "sword1_horizontal_right"),

    (22, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword1_diagonal"),
    (22, 1, (WIDTH // 2, HEIGHT // 2 - 300), "sword1_vertical"),

    (23, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 90), "dragon_horizontal"),
    (23, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 190), "dragon_horizontal"),
    (23, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 350), "dragon_horizontal"),

    (24, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 300), "dragon_vertical"),
    (24, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 300), "dragon_vertical"),
    (24, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 300), "dragon_vertical"),
    (24.5, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "chicken_diagonal2"),
    (25.5, 1, (WHITE_RECT_X, WHITE_RECT_Y), "chicken_diagonal"),

    (27, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 140), "sword1_horizontal_right"),
    (28, 1, (WIDTH // 2, HEIGHT // 2 - 300), "sword1_vertical"),
    (29, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword1_diagonal"),


    (30, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 290), "sword2_horizontal_left"),
    (30, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 90), "sword2_horizontal_left"),
    (30, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword2_diagonal"),
    (30, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "sword2_diagonal2"),

    (31, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "chicken_diagonal2"),


    (34, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "sword2_diagonal2"),
    (34, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 350), "fireball_horizontal"),
    (34, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 240), "fireball_horizontal_right"),
    (34, 1, (WIDTH // 2 + 100, HEIGHT // 2 - 300), "fireball_vertical"),
    (34, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 290), "sword1_horizontal_right"),

    (35, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword1_diagonal"),
    (35, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "sword1_diagonal2"),

    (37, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "chicken_diagonal2"),
    (37, 1, (WHITE_RECT_X, WHITE_RECT_Y), "chicken_diagonal"),

    (39, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 40), "sword1_horizontal_left"),
    (39, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 300), "sword1_vertical"),

    # Секунда 40 (3 атаки)
    (40, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 90), "sword1_horizontal_right"),
    (40, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword1_diagonal"),
    (40, 1, (WIDTH // 2, HEIGHT // 2 - 300), "sword2_vertical"),

    # Секунда 41 (4 атаки)
    (41, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 140), "dragon_horizontal"),
    (41, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 140), "dragon_horizontal_right"),
    (41, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 300), "dragon_vertical"),
    (41, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "fireball_diagonal2"),

    # Секунда 42 (5 атак)
    (42, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 190), "sword1_horizontal"),
    (42, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 190), "dragon_horizontal_right"),
    (42, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "chicken_vertical"),
    (42, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword2_diagonal"),
    (42, 1, (WIDTH // 2 + 150, HEIGHT // 2 - 300), "sword1_vertical"),

    # Секунда 43 (6 атак)
    (43, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 240), "sword2_horizontal_left"),
    (43, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 240), "fireball_horizontal_right"),
    (43, 1, (WIDTH // 2 - 100, HEIGHT // 2 - 300), "fireball_vertical"),
    (43, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "dragon1_diagonal2"),
    (43, 1, (WIDTH // 2 - 150, HEIGHT // 2 - 300), "sword1_vertical"),
    (43, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 40), "sword1_horizontal_right"),

    (43.5, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "chicken_diagonal2"),
    (43.5, 1, (WHITE_RECT_X, WHITE_RECT_Y), "chicken_diagonal"),

    # Секунда 44 (2 атаки)
    (44, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 290), "sword1_horizontal_left"),
    (44, 1, (WIDTH // 2, HEIGHT // 2 - 300), "dragon_vertical"),

    # Секунда 45 (3 атаки)
    (45, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 290), "fireball_horizontal_right"),
    (45, 1, (WHITE_RECT_X, WHITE_RECT_Y), "dragon_diagonal"),
    (45, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "dragon_diagonal2"),
    (45, 1, (WIDTH // 2 + 100, HEIGHT // 2 - 300), "sword2_vertical"),

     # Секунда 46 (4 атаки)
    (46, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 350), "dragon_horizontal"),
    (46, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 350), "chicken_horizontal_right"),
    (46, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 300), "sword1_vertical"),
    (46, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "fireball_diagonal2"),

    # Секунда 47 (5 атак)
    (47, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 395), "fireball_horizontal"),
    (47, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 395), "fireball_horizontal_right"),
    (47, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "chicken_vertical"),
    (47, 1, (WHITE_RECT_X, WHITE_RECT_Y), "dragon1_diagonal"),
    (47, 1, (WIDTH // 2 - 150, HEIGHT // 2 - 300), "fireball_vertical"),

    # Секунда 48 (6 атак)
    (48, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 450), "sword1_horizontal"),
    (48, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 450), "sword2_horizontal_right"),
    (48, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 300), "sword1_vertical"),
    (48, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "sword1_diagonal2"),
    (48, 1, (WIDTH // 2 - 200, HEIGHT // 2 - 300), "sword2_vertical"),
    (48, 1, (WIDTH // 2, HEIGHT // 2 - 300), "dragon_vertical"),

    # Секунда 49 (2 атаки)
    (49, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 40), "sword1_horizontal_left"),
    (49, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 40), "sword1_horizontal_right"),

    (50, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "chicken_diagonal2"),
    (50, 1, (WHITE_RECT_X, WHITE_RECT_Y), "chicken_diagonal"),

    # Секунда 51 (4 атаки)
    (51, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 90), "chicken_horizontal_right"),
    (51, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "dragon1_diagonal2"),
    (51, 1, (WIDTH // 2 - 100, HEIGHT // 2 - 300), "dragon_vertical"),
    (51, 1, (WIDTH // 2 + 150, HEIGHT // 2 - 300), "sword1_vertical"),

    # Секунда 52 (5 атак)
    (52, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 140), "fireball_horizontal"),
    (52, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 140), "dragon_horizontal_right"),
    (52, 1, (WHITE_RECT_X, WHITE_RECT_Y), "fireball_diagonal"),
    (52, 1, (WIDTH // 2 - 150, HEIGHT // 2 - 300), "sword2_vertical"),
    (52, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 300), "sword1_vertical"),

    # Секунда 53 (6 атак)
    (53, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 190), "chicken_horizontal"),
    (53, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 190), "chicken_horizontal_right"),
    (53, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "chicken_diagonal2"),
    (53, 1, (WIDTH // 2 - 200, HEIGHT // 2 - 300), "sword1_vertical"),
    (53, 1, (WIDTH // 2, HEIGHT // 2 - 300), "dragon_vertical"),
    (53, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "fireball_vertical"),

    # Секунда 54 (2 атаки)
    (54, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 240), "sword2_horizontal_left"),
    (54, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 240), "fireball_horizontal_right"),

    # Секунда 55 (3 атаки)
    (55, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword2_diagonal"),
    (55, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 300), "chicken_vertical"),
    (55, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 290), "fireball_horizontal"),

    # Секунда 56 (4 атаки)
    (56, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 290), "sword1_horizontal_right"),
    (56, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "dragon1_diagonal"),
    (56, 1, (WIDTH // 2 - 100, HEIGHT // 2 - 300), "sword1_vertical"),
    (56, 1, (WIDTH // 2 + 150, HEIGHT // 2 - 300), "fireball_vertical"),

    (56.5, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "chicken_diagonal2"),
    (56.5, 1, (WHITE_RECT_X, WHITE_RECT_Y), "chicken_diagonal"),

    # Секунда 57 (5 атак)
    (57, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 350), "dragon_horizontal"),
    (57, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 350), "sword2_horizontal_right"),
    (57, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword1_diagonal"),
    (57, 1, (WIDTH // 2 - 150, HEIGHT // 2 - 300), "sword2_vertical"),
    (57, 1, (WIDTH // 2 + 200, HEIGHT // 2 - 300), "fireball_vertical"),

    # Секунда 58 (6 атак)
    (58, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 395), "fireball_horizontal"),
    (58, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 395), "fireball_horizontal_right"),
    (58, 1, (WHITE_RECT_X + WHITE_RECT_WIDTH, WHITE_RECT_Y), "sword1_diagonal2"),
    (58, 1, (WIDTH // 2 - 200, HEIGHT // 2 - 300), "dragon_vertical"),
    (58, 1, (WIDTH // 2, HEIGHT // 2 - 300), "fireball_vertical"),
    (58, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "dragon_vertical"),

    # Секунда 59 (2 атаки)
    (59, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 450), "fireball_horizontal"),
    (59, 1, (WIDTH // 2 + 350, HEIGHT // 2 + 450), "chicken_horizontal_right"),

    # Секунда 60 (3 атаки)
    (60, 1, (WHITE_RECT_X, WHITE_RECT_Y), "sword1_diagonal"),
    (60, 1, (WIDTH // 2 + 50, HEIGHT // 2 - 300), "sword2_vertical"),
    (60, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 40), "sword1_horizontal_left"),

]

