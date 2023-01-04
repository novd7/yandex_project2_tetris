import pygame as pg

import draw_figure
from board import Board
from constants import BACK_GROUND_COLOR, FPS, SIZE, SPEED_OF_FIGURE_FALLING
from draw_figure import draw_figure
from get_random_figure import get_random_figure
from move_figure import move_figure


def main():
    pg.display.set_caption('Тетрис')
    screen = pg.display.set_mode(SIZE)
    
    clock = pg.time.Clock()
    running = True
    board = Board(screen=screen)
    current_figures = get_random_figure()
    current_figure_position_in_list = 0
    result_of_drawing = draw_figure(current_figures, current_figure_position_in_list, 0, 3, board)
    if not result_of_drawing:
        # TODO: the end of the game
        pass
    # We will fall a figure not every iteration of loop
    falling_counter = 0
    last_keys = None
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            # if event.type == pg.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         board.get_click(event.pos)
        # print(34)
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            # TODO: turn the figure
            pass
        if keys[pg.K_DOWN]:
            if last_keys != str(keys):
                move_figure(board=board, direction='down')
        if keys[pg.K_LEFT]:
            if last_keys != str(keys):
                move_figure(board=board, direction='left')
        if keys[pg.K_RIGHT]:
            if last_keys != str(keys):
                move_figure(board=board, direction='right')
        if falling_counter % (1 / SPEED_OF_FIGURE_FALLING) == 0:
            move_figure(board=board, direction='down')
        last_keys = str(keys)
        falling_counter += 1
        screen.fill(BACK_GROUND_COLOR)
        board.render()
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
