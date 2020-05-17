import pygame
from figures import Rectangle

WIN_WIDTH = 400
WIN_HEIGHT = 600

check_under = [0, 0, 0, 0]

background = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


class IFigure:
    @staticmethod
    def draw_figure(x, y, game_field, position):
        i = int(y / 30)
        j = int(x / 30)
        if position == 1:
            Rectangle.draw_rectangle_blue(x, y)
            Rectangle.draw_rectangle_blue(x + 30, y)
            Rectangle.draw_rectangle_blue(x + 60, y)
            Rectangle.draw_rectangle_blue(x + 90, y)
            game_field[i][j] = 2
            game_field[i][j + 1] = 2
            game_field[i][j + 2] = 2
            game_field[i][j + 3] = 2
        elif position == 2:
            Rectangle.draw_rectangle_blue(x, y)
            Rectangle.draw_rectangle_blue(x, y - 30)
            Rectangle.draw_rectangle_blue(x, y - 60)
            Rectangle.draw_rectangle_blue(x, y - 90)
            game_field[i][j] = 2
            game_field[i - 1][j] = 2
            game_field[i - 2][j] = 2
            game_field[i - 3][j] = 2

    @staticmethod
    def draw_if_next(x, y):
        Rectangle.draw_rectangle_blue(x, y)
        Rectangle.draw_rectangle_blue(x + 30, y)
        Rectangle.draw_rectangle_blue(x + 60, y)
        Rectangle.draw_rectangle_blue(x + 90, y)

    @staticmethod
    def remove_previous_position(x, y, game_field, position):
        i = int(y / 30)
        j = int(x / 30)
        if position == 1:
            game_field[i][j] = 0
            game_field[i][j + 1] = 0
            game_field[i][j + 2] = 0
            game_field[i][j + 3] = 0
        elif position == 2:
            game_field[i - 3][j] = 0
            game_field[i - 2][j] = 0
            game_field[i - 1][j] = 0

    @staticmethod
    def check_under(x, y, game_field, position):
        i = int(y / 30)
        j = int(x / 30)
        if position == 1:
            check_under[0] = game_field[i + 1][j]
            check_under[1] = game_field[i + 1][j + 1]
            check_under[2] = game_field[i + 1][j + 2]
            check_under[3] = game_field[i + 1][j + 3]
        elif position == 2:
            check_under[0] = game_field[i + 1][j]
            check_under[1] = 0
            check_under[2] = 0
            check_under[3] = 0
        return check_under

    @staticmethod
    def move_left(x, y, game_field, position):
        i = int(y / 30)
        j = int(x / 30)
        if position == 1:
            game_field[i][j + 3] = 0
        elif position == 2:
            game_field[i][j] = 0
            game_field[i - 1][j] = 0
            game_field[i - 2][j] = 0
            game_field[i - 3][j] = 0

    @staticmethod
    def move_right(x, y, game_field,position):
        i = int(y / 30)
        j = int(x / 30)
        if position == 1:
            game_field[i][j] = 0
        elif position == 2:
            game_field[i][j] = 0
            game_field[i - 1][j] = 0
            game_field[i - 2][j] = 0
            game_field[i - 3][j] = 0

    @staticmethod
    def can_turn(x, y, game_field, position):
        i = int(y / 30)
        j = int(x / 30)
        if position == 1:
            if i > 3 and game_field[i - 1][j] == 0 and game_field[i - 2][j] == 0 and game_field[i - 3][j] == 0:
                position = 2
        elif position == 2:
            if j < 8 and game_field[i][j + 1] == 0 and game_field[i][j + 2] == 0 and game_field[i][j + 3] == 0:
                position = 1
        return position
