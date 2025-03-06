from game1.constant.constnants import WIDTH, HEIGHT

WHITE_RECT_X = WIDTH // 2 - 250
WHITE_RECT_Y = HEIGHT // 2



events = [
    (1, 1, (WHITE_RECT_X-100, WHITE_RECT_Y-100), "sword1_diagonal"),
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
    (7, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "dragon_vertical"),
    (7, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 300), "dragon_horizontal"),
    (8, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "chicken_vertical"),
    (8, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 300), "chicken_horizontal"),
    (9, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "sword2_vertical"),
    (9, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 300), "sword2_horizontal_left"),
    (10, 1, (WIDTH // 2 - 50, HEIGHT // 2 - 300), "fireball_vertical"),
    (10, 1, (WIDTH // 2 - 500, HEIGHT // 2 + 300), "fireball_horizontal")


]