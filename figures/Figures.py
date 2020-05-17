import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600
BLUE = [0, 33, 88]
START_X = 165
START_Y = 75
WHITE = [255, 255, 255]

background = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


def spawn_new_figure(score, figures, figure, game_field, remove_line,score_text):
    TIMER = 0
    y = START_Y
    x = START_X
    score += 10
    figure = figures.pop()
    next_figure = figures[-1]
    view_score = score_text.render(score.__str__(), 1, WHITE)
    pygame.draw.rect(background, (0, 0, 0), (400, 100, 100, 100))
    background.blit(view_score, (400, 100))
    for j in range(2, 18):
        buffer_game_field = [row[:] for row in game_field]
        for i in range(10):
            remove_line[i] = game_field[i + 1][j]
        count_of_one = 0  # из-за частоты кадров успевает набрать 10 даже с 1 закрытым квадратом, поэтоому обнуляю
        for find_one in remove_line:
            if find_one == 1:
                count_of_one += 1

        if count_of_one == 10:
            for k in range(2, 18):
                for i in range(1, 12):
                    game_field[i][k] = buffer_game_field[i][k - 1]
            count_of_one = 0
            score += 100
            view_score = score_text.render(score.__str__(), 1, WHITE)
            pygame.draw.rect(background, (0, 0, 0), (400, 100, 100, 100))
            background.blit(view_score, (400, 100))
