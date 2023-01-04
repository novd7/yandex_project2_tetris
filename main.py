import pygame as pg

import draw_figure
from board import Board
from get_random_figure import get_random_figure
from draw_figure import draw_figure
from constants import BACK_GROUND_COLOR, FPS, SIZE


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
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            # if event.type == pg.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         board.get_click(event.pos)
            if event.type == pg.K_UP:
                # TODO: turn the figure
                pass
            if event.type == pg.K_DOWN:
                # TODO: go down
                pass
            if event.type == pg.K_LEFT:
                # TODO: go left
                pass
            if event.type == pg.K_RALT:
                # TODO: go right
                pass
            # TODO: go right
            
        screen.fill(BACK_GROUND_COLOR)
        board.render()
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
