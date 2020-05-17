import random
import time
import pygame
from figures import Rectangle
from figures import IFigure, OFigure, JFigure, LFigure, TFigure, SFigure, ZFigure

WIN_WIDTH = 580
WIN_HEIGHT = 600
BACKGROUND_COLOR = [0, 0, 0]
GAME_NAME = "Tetris"
FPS = 60
TIMER = 1
START_X = 165
START_Y = 75
START = True
RESTART = True
WHITE = [255, 255, 255]
BLUE = [0, 33, 88]
SPEED = 30
position = 1
game_over = 0
pygame.init()
background = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(GAME_NAME)
background.fill(BACKGROUND_COLOR)

pygame.mixer.music.load('src/Tetris - Theme (musicpro.me).mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

score_text = pygame.font.SysFont('arial', 36)
game_over_format = pygame.font.SysFont('arial', 54)
start_format = pygame.font.SysFont('arial', 54)
restart_format = pygame.font.SysFont('arial', 46)
pygame.draw.rect(background, BLUE, (385, 510, 150, 70))

your_score = score_text.render('Your score', 1, WHITE)
background.blit(your_score, (400, 50))
start_text = start_format.render('Start', 1, WHITE)
background.blit(start_text, (410, 510))

pygame.display.update()

game_field = [[0 for y in range(12)] for x in range(19)]
remove_line = []
line_full = 0
score = 0
figures = []
for j in range(10000):
    figures.append(random.randint(1, 7))
figure = figures[0]
next_figure = figures[-1]
figure_checked = [0, 0, 0, 0]
timing = time.time()
view_score = score_text.render(score.__str__(), 1, WHITE)
pygame.draw.rect(background, (0, 0, 0), (400, 100, 100, 100))
background.blit(view_score, (450, 100))
for i in range(0, 570, 30):
    for j in range(0, 360, 30):
        if i == 0 or i == 540 or j == 0 or j == 330:
            Rectangle.draw_rectangle_gray(j + 15, i + 15)
            game_field[int(i / 30)][int(j / 30)] = 1

x = START_X
y = START_Y

while True:
    clock.tick(FPS)
    if TIMER == 0 and (int(time.time() - timing)) % 20 == 0:
        if SPEED <= 3:
            SPEED = 3
        SPEED -= 1
    for i in range(30, 540, 30):
        for j in range(30, 320, 30):
            if game_field[int(i / 30)][int(j / 30)] == 0:
                Rectangle.draw_rectangle_background(j, i)
            # после сдвига цвет у фигур останется тем же
            elif game_field[int(i / 30)][int(j / 30)] == 2:
                Rectangle.draw_rectangle_blue(j + 15, i + 15)
            elif game_field[int(i / 30)][int(j / 30)] == 3:
                Rectangle.draw_rectangle_yellow(j + 15, i + 15)
            elif game_field[int(i / 30)][int(j / 30)] == 4:
                Rectangle.draw_rectangle_purple(j + 15, i + 15)
            elif game_field[int(i / 30)][int(j / 30)] == 5:
                Rectangle.draw_rectangle_red(j + 15, i + 15)
            elif game_field[int(i / 30)][int(j / 30)] == 6:
                Rectangle.draw_rectangle_orange(j + 15, i + 15)
            elif game_field[int(i / 30)][int(j / 30)] == 7:
                Rectangle.draw_rectangle_green(j + 15, i + 15)
            elif game_field[int(i / 30)][int(j / 30)] == 8:
                Rectangle.draw_rectangle_light_blue(j + 15, i + 15)
    pygame.draw.rect(background, (200, 200, 200), (390, 200, 150, 200), 1)
    pygame.draw.rect(background, BACKGROUND_COLOR, (391, 201, 148, 198))
    if figure == 1:
        IFigure.IFigure.draw_figure(x, y, game_field, position)
    elif figure == 2:
        OFigure.OFigure.draw_figure(x, y, game_field)
    elif figure == 3:
        TFigure.TFigure.draw_figure(x, y, game_field, position)
    elif figure == 4:
        JFigure.JFigure.draw_figure(x, y, game_field, position)
    elif figure == 5:
        LFigure.LFigure.draw_figure(x, y, game_field, position)
    elif figure == 6:
        SFigure.SFigure.draw_figure(x, y, game_field, position)
    elif figure == 7:
        ZFigure.ZFigure.draw_figure(x, y, game_field, position)
    if next_figure == 1:
        IFigure.IFigure.draw_if_next(405, 270)
    elif next_figure == 2:
        OFigure.OFigure.draw_if_next(430, 270)
    elif next_figure == 3:
        TFigure.TFigure.draw_if_next(430, 270)
    elif next_figure == 4:
        JFigure.JFigure.draw_if_next(405, 270)
    elif next_figure == 5:
        LFigure.LFigure.draw_if_next(405, 270)
    elif next_figure == 6:
        SFigure.SFigure.draw_if_next(405, 270)
    elif next_figure == 7:
        ZFigure.ZFigure.draw_if_next(405, 270)
    pygame.display.update()
    while START:
        for k in pygame.event.get():
            if k.type == pygame.MOUSEBUTTONDOWN:
                if k.button == 1:
                    if 385 <= k.pos[0] <= 635 and 510 <= k.pos[1] <= 580:
                        START = False
            if k.type == pygame.QUIT:
                exit()

    for k in pygame.event.get():
        if k.type == pygame.QUIT:
            exit()
        elif k.type == pygame.KEYDOWN:
            i = int(y / 30)
            j = int(x / 30)
            if k.key == pygame.K_SPACE:
                if figure == 1:
                    if IFigure.IFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                        while IFigure.IFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                            IFigure.IFigure.remove_previous_position(x, y, game_field, position)
                            y += 30
                elif figure == 2:
                    if OFigure.OFigure.check_under(x, y + 30, game_field) == [0, 0, 0, 0]:
                        while OFigure.OFigure.check_under(x, y + 30, game_field) == [0, 0, 0, 0]:
                            OFigure.OFigure.remove_previous_position(x, y, game_field)
                            y += 30
                elif figure == 3:
                    if TFigure.TFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                        while TFigure.TFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                            TFigure.TFigure.remove_previous_position(x, y, game_field, position)
                            y += 30
                elif figure == 4:
                    if JFigure.JFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                        while JFigure.JFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                            JFigure.JFigure.remove_previous_position(x, y, game_field, position)
                            y += 30
                elif figure == 5:
                    if LFigure.LFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                        while LFigure.LFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                            LFigure.LFigure.remove_previous_position(x, y, game_field, position)
                            y += 30
                elif figure == 6:
                    if SFigure.SFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                        while SFigure.SFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                            SFigure.SFigure.remove_previous_position(x, y, game_field, position)
                            y += 30
                elif figure == 7:
                    if ZFigure.ZFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                        while ZFigure.ZFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                            ZFigure.ZFigure.remove_previous_position(x, y, game_field, position)
                            y += 30
            elif k.key == pygame.K_LEFT:
                # сдвиг фигуры влево
                if figure == 1:
                    if game_field[i][j - 1] == 0:
                        IFigure.IFigure.move_left(x, y, game_field, position)
                        x -= 30
                elif figure == 2:
                    if game_field[i][j - 1] == 0 and game_field[i - 1][j - 1] == 0:
                        OFigure.OFigure.move_left(x, y, game_field)
                        x -= 30
                elif figure == 3:
                    if position == 1:
                        if game_field[i][j - 1] == 0 and game_field[i - 1][j] == 0:
                            TFigure.TFigure.move_left(x, y, game_field, position)
                            x -= 30
                    elif position == 2:
                        if game_field[i][j] == 0 and game_field[i - 1][j - 1] == 0 and game_field[i - 2][j] == 0:
                            TFigure.TFigure.move_left(x, y, game_field, position)
                            x -= 30
                    elif position == 3:
                        if game_field[i][j] == 0 and game_field[i - 1][j - 1] == 0:
                            TFigure.TFigure.move_left(x, y, game_field, position)
                            x -= 30
                    elif position == 4:
                        if game_field[i][j] == 0 and game_field[i - 1][j] == 0 and game_field[i - 2][j] == 0:
                            TFigure.TFigure.move_left(x, y, game_field, position)
                            x -= 30
                elif figure == 4:
                    if position == 1:
                        if game_field[i][j - 1] == 0 and game_field[i - 1][j - 1] == 0:
                            JFigure.JFigure.move_left(x, y, game_field, position)
                            x -= 30
                    elif position == 2:
                        if game_field[i][j - 1] == 0 and game_field[i - 1][j] == 0 and game_field[i - 2][j] == 0:
                            JFigure.JFigure.move_left(x, y, game_field, position)
                            x -= 30
                    elif position == 3:
                        if game_field[i - 1][j - 1] == 0 and game_field[i][j + 1] == 0:
                            JFigure.JFigure.move_left(x, y, game_field, position)
                            x -= 30
                    elif position == 4:
                        if game_field[i][j - 1] == 0 and game_field[i - 1][j - 1] == 0 \
                                and game_field[i - 2][j - 1] == 0:
                            JFigure.JFigure.move_left(x, y, game_field, position)
                            x -= 30
                elif figure == 5:
                    if position == 1:
                        if game_field[i][j - 1] == 0 and game_field[i - 1][j + 1] == 0:
                            LFigure.LFigure.move_left(x, y, game_field, position)
                            x -= 30
                    elif position == 2:
                        if game_field[i][j] == 0 and game_field[i - 1][j] == 0 and game_field[i - 2][j - 1] == 0:
                            LFigure.LFigure.move_left(x, y, game_field, position)
                            x -= 30
                    elif position == 3:
                        if game_field[i][j - 1] == 0 and game_field[i - 1][j - 1] == 0:
                            LFigure.LFigure.move_left(x, y, game_field, position)
                            x -= 30
                    elif position == 4:
                        if game_field[i][j - 1] == 0 and game_field[i - 1][j - 1] == 0 \
                                and game_field[i - 2][j - 1] == 0:
                            LFigure.LFigure.move_left(x, y, game_field, position)
                            x -= 30
                elif figure == 6:
                    if position == 1:
                        if game_field[i][j - 1] == 0 and game_field[i - 1][j] == 0:
                            SFigure.SFigure.move_left(x, y, game_field, position)
                            x -= 30
                    elif position == 2:
                        if game_field[i][j] == 0 and game_field[i - 1][j - 1] == 0 and game_field[i - 2][j - 1] == 0:
                            SFigure.SFigure.move_left(x, y, game_field, position)
                            x -= 30
                elif figure == 7:
                    if position == 1:
                        if game_field[i][j] == 0 and game_field[i - 1][j - 1] == 0:
                            ZFigure.ZFigure.move_left(x, y, game_field, position)
                            x -= 30
                    elif position == 2:
                        if game_field[i][j - 1] == 0 and game_field[i - 1][j - 1] == 0 and game_field[i - 2][j] == 0:
                            ZFigure.ZFigure.move_left(x, y, game_field, position)
                            x -= 30
            elif k.key == pygame.K_RIGHT:
                # сдвиг фигуры вправо
                if figure == 1:
                    if position == 1:
                        if game_field[i][j + 4] == 0:
                            IFigure.IFigure.move_right(x, y, game_field, position)
                            x += 30
                    elif position == 2:
                        if game_field[i][j + 1] == 0 and game_field[i - 1][j + 1] == 0 \
                                and game_field[i - 2][j + 1] == 0 and game_field[i - 3][j + 1] == 0:
                            IFigure.IFigure.move_right(x, y, game_field, position)
                            x += 30
                elif figure == 2:
                    if game_field[i][j + 2] == 0 and game_field[i - 1][j + 2] == 0:
                        OFigure.OFigure.move_right(x, y, game_field)
                        x += 30
                elif figure == 3:
                    if position == 1:
                        if game_field[i][j + 3] == 0 and game_field[i - 1][j + 2] == 0:
                            TFigure.TFigure.move_right(x, y, game_field, position)
                            x += 30
                    elif position == 2:
                        if game_field[i][j + 2] == 0 and game_field[i - 1][j + 2] == 0 \
                                and game_field[i - 2][j + 2] == 0:
                            TFigure.TFigure.move_right(x, y, game_field, position)
                            x += 30
                    elif position == 3:
                        if game_field[i][j + 2] == 0 and game_field[i - 1][j + 3] == 0:
                            TFigure.TFigure.move_right(x, y, game_field, position)
                            x += 30
                    elif position == 4:
                        if game_field[i][j + 2] == 0 and game_field[i - 1][j + 3] == 0 \
                                and game_field[i - 2][j + 2] == 0:
                            TFigure.TFigure.move_right(x, y, game_field, position)
                            x += 30
                elif figure == 4:
                    if position == 1:
                        if game_field[i][j + 3] == 0 and game_field[i - 1][j + 1] == 0:
                            JFigure.JFigure.move_right(x, y, game_field, position)
                            x += 30
                    elif position == 2:
                        if game_field[i][j + 2] == 0 and game_field[i - 1][j + 2] == 0 \
                                and game_field[i - 2][j + 2] == 0:
                            JFigure.JFigure.move_right(x, y, game_field, position)
                            x += 30
                    elif position == 3:
                        if game_field[i][j + 3] == 0 and game_field[i - 1][j + 3] == 0:
                            JFigure.JFigure.move_right(x, y, game_field, position)
                            x += 30
                    elif position == 4:
                        if game_field[i][j + 1] == 0 and game_field[i - 1][j + 1] == 0 \
                                and game_field[i - 2][j + 2] == 0:
                            JFigure.JFigure.move_right(x, y, game_field, position)
                            x += 30
                elif figure == 5:
                    if position == 1:
                        if game_field[i][j + 3] == 0 and game_field[i - 1][j + 3] == 0:
                            LFigure.LFigure.move_right(x, y, game_field, position)
                            x += 30
                    elif position == 2:
                        if game_field[i][j + 2] == 0 and game_field[i - 1][j + 2] == 0 \
                                and game_field[i - 2][j + 2] == 0:
                            LFigure.LFigure.move_right(x, y, game_field, position)
                            x += 30
                    elif position == 3:
                        if game_field[i][j + 1] == 0 and game_field[i - 1][j + 3] == 0:
                            LFigure.LFigure.move_right(x, y, game_field, position)
                            x += 30
                    elif position == 4:
                        if game_field[i][j + 2] == 0 and game_field[i - 1][j + 1] == 0 \
                                and game_field[i - 2][j + 1] == 0:
                            LFigure.LFigure.move_right(x, y, game_field, position)
                            x += 30
                elif figure == 6:
                    if position == 1:
                        if game_field[i][j + 2] == 0 and game_field[i - 1][j + 3] == 0:
                            SFigure.SFigure.move_right(x, y, game_field, position)
                            x += 30
                    elif position == 2:
                        if game_field[i][j + 2] == 0 and game_field[i - 1][j + 2] == 0 \
                                and game_field[i - 2][j + 1] == 0:
                            print(123)
                            SFigure.SFigure.move_right(x, y, game_field, position)
                            x += 30
                elif figure == 7:
                    if position == 1:
                        if game_field[i][j + 3] == 0 and game_field[i - 1][j + 2] == 0:
                            ZFigure.ZFigure.move_right(x, y, game_field, position)
                            x += 30
                    if position == 2:
                        if game_field[i][j + 1] == 0 and game_field[i - 1][j + 2] == 0 \
                                and game_field[i - 2][j + 2] == 0:
                            ZFigure.ZFigure.move_right(x, y, game_field, position)
                            x += 30
            elif k.key == pygame.K_UP:
                if figure == 1:
                    IFigure.IFigure.remove_previous_position(x, y, game_field, position)
                    position = IFigure.IFigure.can_turn(x, y, game_field, position)
                elif figure == 3:
                    TFigure.TFigure.remove_previous_position(x, y, game_field, position)
                    position = TFigure.TFigure.can_turn(x, y, game_field, position)
                elif figure == 4:
                    JFigure.JFigure.remove_previous_position(x, y, game_field, position)
                    position = JFigure.JFigure.can_turn(x, y, game_field, position)
                elif figure == 5:
                    LFigure.LFigure.remove_previous_position(x, y, game_field, position)
                    position = LFigure.LFigure.can_turn(x, y, game_field, position)
                elif figure == 6:
                    SFigure.SFigure.remove_previous_position(x, y, game_field, position)
                    position = SFigure.SFigure.can_turn(x, y, game_field, position)
                elif figure == 7:
                    ZFigure.ZFigure.remove_previous_position(x, y, game_field, position)
                    position = ZFigure.ZFigure.can_turn(x, y, game_field, position)
            elif k.key == pygame.K_DOWN:
                if figure == 1:
                    if IFigure.IFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                        IFigure.IFigure.remove_previous_position(x, y, game_field, position)
                        y += 30
                elif figure == 2:
                    if OFigure.OFigure.check_under(x, y + 30, game_field) == [0, 0, 0, 0]:
                        OFigure.OFigure.remove_previous_position(x, y, game_field)
                        y += 30
                elif figure == 3:
                    if TFigure.TFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                        TFigure.TFigure.remove_previous_position(x, y, game_field, position)
                        y += 30
                elif figure == 4:
                    if JFigure.JFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                        JFigure.JFigure.remove_previous_position(x, y, game_field, position)
                        y += 30
                elif figure == 5:
                    if LFigure.LFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                        LFigure.LFigure.remove_previous_position(x, y, game_field, position)
                        y += 30
                elif figure == 6:
                    if SFigure.SFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                        SFigure.SFigure.remove_previous_position(x, y, game_field, position)
                        y += 30
                elif figure == 7:
                    if ZFigure.ZFigure.check_under(x, y + 30, game_field, position) == [0, 0, 0, 0]:
                        ZFigure.ZFigure.remove_previous_position(x, y, game_field, position)
                        y += 30
    if game_field[2][5] != 0 and game_field[3][5] != 0 and game_field[2][5] != game_field[3][5]:
        game_over = 1
    elif game_field[2][6] != 0 and game_field[3][6] != 0 and game_field[2][6] != game_field[3][6]:
        game_over = 1
    elif game_field[2][7] != 0 and game_field[3][7] != 0 and game_field[2][7] != game_field[3][7]:
        game_over = 1
    elif game_field[2][8] != 0 and game_field[3][8] != 0 and game_field[2][8] != game_field[3][8]:
        game_over = 1
    if game_over != 0:
        game_over_text = game_over_format.render('GAME OVER', 1, WHITE)
        background.blit(game_over_text, (70, 200))
        pygame.draw.rect(background, BACKGROUND_COLOR, (400, 50, 150, 50))
        your_score = score_text.render('Final score', 1, WHITE)
        background.blit(your_score, (400, 50))
        pygame.draw.rect(background, BLUE, (385, 510, 150, 70))
        restart_text = restart_format.render('Restart?', 1, WHITE)
        background.blit(restart_text, (390, 515))
        pygame.display.update()
        figures = []
        SPEED = 30
        game_over = 0
        for i in range(10000):
            figures.append(random.randint(1, 7))
        position = 1
        figure = figures[0]
        next_figure = figures[-1]
        RESTART = True
        while RESTART:
            for k in pygame.event.get():
                if k.type == pygame.MOUSEBUTTONDOWN:
                    if k.button == 1:
                        if 385 <= k.pos[0] <= 635 and 510 <= k.pos[1] <= 580:
                            RESTART = False
                            for j in range(30, 320, 30):
                                for i in range(30, 540, 30):
                                    game_field[int(i / 30)][int(j / 30)] = 0
                            pygame.draw.rect(background, (0, 0, 0), (44, 44, 290, 510))
                            pygame.draw.rect(background, BLUE, (385, 510, 150, 70))
                            start_text = start_format.render('Start', 1, WHITE)
                            pygame.draw.rect(background, (0, 0, 0), (400, 100, 100, 100))
                            score = 0
                            view_score = score_text.render(score.__str__(), 1, WHITE)
                            background.blit(view_score, (450, 100))
                            background.blit(start_text, (410, 510))
                            pygame.draw.rect(background, BACKGROUND_COLOR, (400, 50, 150, 50))
                            your_score = score_text.render('Your score', 1, WHITE)
                            background.blit(your_score, (400, 50))
                elif k.type == pygame.QUIT:
                    exit()
    if figure == 1:
        if IFigure.IFigure.check_under(x, y, game_field, position) == [0, 0, 0, 0]:
            TIMER += 1
            figure_checked = IFigure.IFigure.check_under(x, y, game_field, position)
            if TIMER == SPEED:
                IFigure.IFigure.remove_previous_position(x, y, game_field, position)
                y += 30
                TIMER = 0
    elif figure == 2:
        if OFigure.OFigure.check_under(x, y, game_field) == [0, 0, 0, 0]:
            TIMER += 1
            figure_checked = OFigure.OFigure.check_under(x, y, game_field)
            if TIMER == SPEED:
                OFigure.OFigure.remove_previous_position(x, y, game_field)
                y += 30
                TIMER = 0
    elif figure == 3:
        if TFigure.TFigure.check_under(x, y, game_field, position) == [0, 0, 0, 0]:
            TIMER += 1
            figure_checked = TFigure.TFigure.check_under(x, y, game_field, position)
            if TIMER == SPEED:
                TFigure.TFigure.remove_previous_position(x, y, game_field, position)
                y += 30
                TIMER = 0
    elif figure == 4:
        if JFigure.JFigure.check_under(x, y, game_field, position) == [0, 0, 0, 0]:
            TIMER += 1
            figure_checked = JFigure.JFigure.check_under(x, y, game_field, position)
            if TIMER == SPEED:
                JFigure.JFigure.remove_previous_position(x, y, game_field, position)
                y += 30
                TIMER = 0
    elif figure == 5:
        if LFigure.LFigure.check_under(x, y, game_field, position) == [0, 0, 0, 0]:
            TIMER += 1
            figure_checked = LFigure.LFigure.check_under(x, y, game_field, position)
            if TIMER == SPEED:
                LFigure.LFigure.remove_previous_position(x, y, game_field, position)
                y += 30
                TIMER = 0
    elif figure == 6:
        if SFigure.SFigure.check_under(x, y, game_field, position) == [0, 0, 0, 0]:
            TIMER += 1
            figure_checked = SFigure.SFigure.check_under(x, y, game_field, position)
            if TIMER == SPEED:
                SFigure.SFigure.remove_previous_position(x, y, game_field, position)
                y += 30
                TIMER = 0
    elif figure == 7:
        if ZFigure.ZFigure.check_under(x, y, game_field, position) == [0, 0, 0, 0]:
            TIMER += 1
            figure_checked = ZFigure.ZFigure.check_under(x, y, game_field, position)
            if TIMER == SPEED:
                ZFigure.ZFigure.remove_previous_position(x, y, game_field, position)
                y += 30
                TIMER = 0
    if figure_checked != [0, 0, 0, 0]:
        TIMER = 0
        y = START_Y
        x = START_X
        score += 10
        position = 1
        figure = next_figure
        if not figures:
            for i in range(1000):
                figures.append(random.randint(1, 7))
        next_figure = figures.pop()
        view_score = score_text.render(score.__str__(), 1, WHITE)
        pygame.draw.rect(background, (0, 0, 0), (400, 100, 150, 100))
        background.blit(view_score, (450, 100))
        for i in range(2, game_field.__len__() - 1):
            remove_line = game_field[i]
            for j in range(1, 11):
                if remove_line[j] != 0:
                    line_full += 1
            if line_full == 10:
                del game_field[i]
                game_field.insert(0, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
                game_field[1] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
                score += 100
                view_score = score_text.render(score.__str__(), 1, WHITE)
                pygame.draw.rect(background, (0, 0, 0), (400, 100, 150, 100))
                background.blit(view_score, (450, 100))
            line_full = 0
