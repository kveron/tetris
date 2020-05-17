import pygame
from figures import Rectangle

WIN_WIDTH = 400
WIN_HEIGHT = 600

check_under = [0, 0, 0, 0]

background = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


class OFigure:
    @staticmethod
    def draw_figure(x, y, game_field):
        i = int(y / 30)
        j = int(x / 30)
        Rectangle.draw_rectangle_yellow(x, y)
        Rectangle.draw_rectangle_yellow(x + 30, y)
        Rectangle.draw_rectangle_yellow(x, y - 30)
        Rectangle.draw_rectangle_yellow(x + 30, y - 30)
        game_field[i][j] = 3
        game_field[i][j + 1] = 3
        game_field[i - 1][j] = 3
        game_field[i - 1][j + 1] = 3

    @staticmethod
    def draw_if_next(x, y):
        Rectangle.draw_rectangle_yellow(x, y)
        Rectangle.draw_rectangle_yellow(x + 30, y)
        Rectangle.draw_rectangle_yellow(x, y - 30)
        Rectangle.draw_rectangle_yellow(x + 30, y - 30)

    @staticmethod
    def remove_previous_position(x, y, game_field):
        i = int(y / 30)
        j = int(x / 30)
        game_field[i - 1][j] = 0
        game_field[i - 1][j + 1] = 0

    @staticmethod
    def check_under(x, y, game_field):
        i = int(y / 30)
        j = int(x / 30)
        check_under[0] = game_field[i + 1][j]
        check_under[1] = game_field[i + 1][j + 1]
        check_under[2] = 0
        check_under[3] = 0
        return check_under

    @staticmethod
    def move_left(x, y, game_field):
        i = int(y / 30)
        j = int(x / 30)
        game_field[i][j + 1] = 0
        game_field[i - 1][j + 1] = 0

    @staticmethod
    def move_right(x, y, game_field):
        i = int(y / 30)
        j = int(x / 30)
        game_field[i][j] = 0
        game_field[i - 1][j] = 0
