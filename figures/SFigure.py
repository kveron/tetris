import pygame
from figures import Rectangle

WIN_WIDTH = 400
WIN_HEIGHT = 600

check_under = [0, 0, 0, 0]

background = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


class SFigure:
    @staticmethod
    def draw_figure(x, y, game_field, position):
        i = int(y / 30)
        j = int(x / 30)
        if position == 1:
            Rectangle.draw_rectangle_green(x, y)
            Rectangle.draw_rectangle_green(x + 30, y)
            Rectangle.draw_rectangle_green(x + 30, y - 30)
            Rectangle.draw_rectangle_green(x + 60, y - 30)
            game_field[i][j] = 7
            game_field[i][j + 1] = 7
            game_field[i - 1][j + 2] = 7
            game_field[i - 1][j + 1] = 7
        elif position == 2:
            Rectangle.draw_rectangle_green(x, y - 30)
            Rectangle.draw_rectangle_green(x + 30, y)
            Rectangle.draw_rectangle_green(x + 30, y - 30)
            Rectangle.draw_rectangle_green(x, y - 60)
            game_field[i - 1][j] = 7
            game_field[i][j + 1] = 7
            game_field[i-2][j] = 7
            game_field[i - 1][j + 1] = 7

    @staticmethod
    def draw_if_next(x, y):
        Rectangle.draw_rectangle_green(x, y)
        Rectangle.draw_rectangle_green(x + 30, y)
        Rectangle.draw_rectangle_green(x + 30, y - 30)
        Rectangle.draw_rectangle_green(x + 60, y - 30)

    @staticmethod
    def remove_previous_position(x, y, game_field, position):
        i = int(y / 30)
        j = int(x / 30)
        if position == 1:
            game_field[i][j] = 0
            game_field[i - 1][j + 2] = 0
            game_field[i - 1][j + 1] = 0
        elif position == 2:
            game_field[i - 1][j] = 0
            game_field[i][j + 1] = 0
            game_field[i - 2][j] = 0
            game_field[i - 1][j + 1] = 0

    @staticmethod
    def check_under(x, y, game_field, position):
        i = int(y / 30)
        j = int(x / 30)
        if position == 1:
            check_under[0] = game_field[i + 1][j]
            check_under[1] = game_field[i + 1][j + 1]
            check_under[2] = game_field[i][j + 2]
            check_under[3] = 0
        elif position == 2:
            check_under[0] = game_field[i][j]
            check_under[1] = game_field[i + 1][j + 1]
            check_under[2] = 0
            check_under[3] = 0
        return check_under

    @staticmethod
    def move_left(x, y, game_field, position):
        i = int(y / 30)
        j = int(x / 30)
        if position == 1:
            game_field[i][j + 1] = 0
            game_field[i - 1][j + 2] = 0
        elif position == 2:
            game_field[i][j + 1] = 0
            game_field[i - 1][j + 1] = 0
            game_field[i - 2][j] = 0

    @staticmethod
    def move_right(x, y, game_field, position):
        i = int(y / 30)
        j = int(x / 30)
        if position == 1:
            game_field[i][j] = 0
            game_field[i - 1][j + 1] = 0
        elif position == 2:
            game_field[i][j + 1] = 0
            game_field[i - 1][j] = 0
            game_field[i - 2][j] = 0

    @staticmethod
    def can_turn(x, y, game_field, position):
        i = int(y / 30)
        j = int(x / 30)
        if position == 1:
            if i > 2 and game_field[i - 1][j] == 0 and game_field[i - 2][j] == 0:
                position = 2
        elif position == 2:
            if j < 9 and game_field[i][j] == 0 and game_field[i-1][j + 2] == 0:
                position = 1
        return position
