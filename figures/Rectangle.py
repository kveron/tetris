import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600

background = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


def draw_rectangle_background(x, y):
    pygame.draw.rect(background, (25, 25, 25), (x + 15, y + 15, 28, 28))
    pygame.draw.rect(background, (75, 75, 75), (x + 18, y + 18, 22, 22))
    pygame.draw.polygon(background, (100, 100, 100), [[x + 18, y + 18], [x + 38, y + 18], [x + 28, y + 28]])
    pygame.draw.polygon(background, (50, 50, 50), [[x + 18, y + 38], [x + 38, y + 38], [x + 28, y + 28]])


def draw_rectangle_gray(x, y):
    # pygame.draw.rect(background, (200, 200, 200), (x + 1, y + 1, 27, 27))
    # pygame.draw.rect(background, (100, 100, 100), (x + 3, y + 3, 25, 25))
    # pygame.draw.rect(background, (150, 150, 150), (x + 3, y + 3, 23, 23))
    pygame.draw.rect(background, (100, 100, 100), (x, y, 28, 28))
    pygame.draw.rect(background, (170, 170, 170), (x + 3, y + 3, 22, 22))
    pygame.draw.polygon(background, (200, 200, 200), [[x + 3, y + 3], [x + 23, y + 3], [x + 13, y + 13]])
    pygame.draw.polygon(background, (150, 150, 150), [[x + 3, y + 23], [x + 23, y + 23], [x + 13, y + 13]])


def draw_rectangle_blue(x, y):
    # pygame.draw.rect(background, (100, 133, 188), (x + 1, y + 1, 27, 27))
    # pygame.draw.rect(background, (0, 33, 88), (x + 3, y + 3, 25, 25))
    # pygame.draw.rect(background, (50, 83, 138), (x + 3, y + 3, 23, 23))
    pygame.draw.rect(background, (0, 33, 88), (x, y, 28, 28))
    pygame.draw.rect(background, (70, 103, 158), (x + 3, y + 3, 22, 22))
    pygame.draw.polygon(background, (100, 133, 188), [[x + 3, y + 3], [x + 23, y + 3], [x + 13, y + 13]])
    pygame.draw.polygon(background, (50, 83, 138), [[x + 3, y + 23], [x + 23, y + 23], [x + 13, y + 13]])


def draw_rectangle_yellow(x, y):
    # pygame.draw.rect(background, (255, 255, 50), (x + 1, y + 1, 27, 27))
    # pygame.draw.rect(background, (150, 150, 0), (x + 3, y + 3, 25, 25))
    # pygame.draw.rect(background, (200, 200, 0), (x + 3, y + 3, 23, 23))
    pygame.draw.rect(background, (150, 150, 0), (x, y, 28, 28))
    pygame.draw.rect(background, (200, 200, 0), (x + 3, y + 3, 22, 22))
    pygame.draw.polygon(background, (235, 235, 50), [[x + 3, y + 3], [x + 23, y + 3], [x + 13, y + 13]])
    pygame.draw.polygon(background, (180, 180, 0), [[x + 3, y + 23], [x + 23, y + 23], [x + 13, y + 13]])


def draw_rectangle_red(x, y):
    # pygame.draw.rect(background, (255, 40, 40), (x + 1, y + 1, 27, 27))
    # pygame.draw.rect(background, (200, 0, 0), (x + 3, y + 3, 25, 25))
    # pygame.draw.rect(background, (255, 0, 0), (x + 3, y + 3, 23, 23))
    pygame.draw.rect(background, (160, 0, 0), (x, y, 28, 28))
    pygame.draw.rect(background, (200, 0, 0), (x + 3, y + 3, 22, 22))
    pygame.draw.polygon(background, (235, 0, 0), [[x + 3, y + 3], [x + 23, y + 3], [x + 13, y + 13]])
    pygame.draw.polygon(background, (180, 0, 0), [[x + 3, y + 23], [x + 23, y + 23], [x + 13, y + 13]])


def draw_rectangle_orange(x, y):
    # pygame.draw.rect(background, (255, 145, 30), (x + 1, y + 1, 27, 27))
    # pygame.draw.rect(background, (200, 100, 0), (x + 3, y + 3, 25, 25))
    # pygame.draw.rect(background, (240, 120, 0), (x + 3, y + 3, 23, 23))
    pygame.draw.rect(background, (200, 100, 0), (x, y, 28, 28))
    pygame.draw.rect(background, (240, 120, 0), (x + 3, y + 3, 22, 22))
    pygame.draw.polygon(background, (255, 145, 30), [[x + 3, y + 3], [x + 23, y + 3], [x + 13, y + 13]])
    pygame.draw.polygon(background, (220, 100, 0), [[x + 3, y + 23], [x + 23, y + 23], [x + 13, y + 13]])


def draw_rectangle_green(x, y):
    # pygame.draw.rect(background, (0, 255, 0), (x + 1, y + 1, 27, 27))
    # pygame.draw.rect(background, (0, 170, 0), (x + 3, y + 3, 25, 25))
    # pygame.draw.rect(background, (0, 210, 0), (x + 3, y + 3, 23, 23))
    pygame.draw.rect(background, (0, 150, 0), (x, y, 28, 28))
    pygame.draw.rect(background, (0, 200, 0), (x + 3, y + 3, 22, 22))
    pygame.draw.polygon(background, (0, 235, 0), [[x + 3, y + 3], [x + 23, y + 3], [x + 13, y + 13]])
    pygame.draw.polygon(background, (0, 170, 0), [[x + 3, y + 23], [x + 23, y + 23], [x + 13, y + 13]])


def draw_rectangle_purple(x, y):
    # pygame.draw.rect(background, (255, 40, 150), (x + 1, y + 1, 27, 27))
    # pygame.draw.rect(background, (160, 0, 80), (x + 3, y + 3, 25, 25))
    # pygame.draw.rect(background, (220, 0, 110), (x + 3, y + 3, 23, 23))
    pygame.draw.rect(background, (160, 0, 80), (x, y, 28, 28))
    pygame.draw.rect(background, (220, 0, 110), (x + 3, y + 3, 22, 22))
    pygame.draw.polygon(background, (200, 0, 100), [[x + 3, y + 3], [x + 23, y + 3], [x + 13, y + 13]])
    pygame.draw.polygon(background, (235, 40, 150), [[x + 3, y + 23], [x + 23, y + 23], [x + 13, y + 13]])


def draw_rectangle_light_blue(x, y):
    # pygame.draw.rect(background, (0, 255, 255), (x + 1, y + 1, 27, 27))
    # pygame.draw.rect(background, (0, 190, 190), (x + 3, y + 3, 25, 25))
    # pygame.draw.rect(background, (0, 220, 220), (x + 3, y + 3, 23, 23))
    pygame.draw.rect(background, (0, 150, 150), (x, y, 28, 28))
    pygame.draw.rect(background, (0, 190, 190), (x + 3, y + 3, 22, 22))
    pygame.draw.polygon(background, (0, 170, 170), [[x + 3, y + 3], [x + 23, y + 3], [x + 13, y + 13]])
    pygame.draw.polygon(background, (0, 235, 235), [[x + 3, y + 23], [x + 23, y + 23], [x + 13, y + 13]])
