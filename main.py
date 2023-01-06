import pygame as pg

import draw_figure
from board import Board
from constants import BACK_GROUND_COLOR, FPS, SIZE, INITIAL_SPEED_OF_FIGURE_FALLING, \
    INDENT_LEFT, WIDTH_OF_PLAYGROUND, CELL_SIZE, PROGRAM_NAME, DELTA_SPEED_FOR_LEVEL, SCORE_TO_SWITCH_LEVEL
from database import insert_score_in_database
from draw_figure import draw_figure
from draw_text import draw_text
from get_random_figure import get_random_figure
from move_figure import move_figure
from remove_filled_rows import remove_filled_rows
from turn_figure import turn_figure


def main(name='Vladimir'):
    """Function of game process"""
    pg.display.set_caption(PROGRAM_NAME)
    screen = pg.display.set_mode(SIZE)
    score = 0
    level = score // SCORE_TO_SWITCH_LEVEL + 1
    clock = pg.time.Clock()
    running = True
    board = Board(screen=screen)
    current_figures = get_random_figure()
    next_figure = get_random_figure()
    next_figure_board = Board(screen=screen)
    next_figure_board.width = 4
    next_figure_board.height = 4
    next_figure_board.left = INDENT_LEFT + WIDTH_OF_PLAYGROUND * CELL_SIZE + INDENT_LEFT
    next_figure_board.top = 255
    next_figure_board.data = [[j if j == "x" else "" for j in i] for i in next_figure[0]]
    
    current_figure_position_in_list = 0
    result_of_drawing = draw_figure(current_figures, current_figure_position_in_list, 0, 5, board)
    print("result_of_drawing", result_of_drawing)
    if result_of_drawing == False:
        # TODO: the end of the game
        insert_score_in_database(name, score)
        print("main.py:26 the game is over")
        return
    # We will fall a figure not every iteration of loop
    falling_counter = 0
    last_keys = None
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                print(board.data)
                break
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            if last_keys != str(keys):
                current_figure_position_in_list = turn_figure(
                    cur_figure=current_figures,
                    pos_in_list=current_figure_position_in_list,
                    board=board
                )
        if keys[pg.K_DOWN]:
            move_figure(board=board, direction='down')
        if keys[pg.K_LEFT]:
            if last_keys != str(keys):
                move_figure(board=board, direction='left')
        if keys[pg.K_RIGHT]:
            if last_keys != str(keys):
                move_figure(board=board, direction='right')
        if falling_counter % (1 / (INITIAL_SPEED_OF_FIGURE_FALLING + DELTA_SPEED_FOR_LEVEL * (level - 1))) <= 0.2:
            move_figure(board=board, direction='down')
        
        last_keys = str(keys)
        should_draw_new_figure = True
        for i in board.data:
            for j in i:
                if j == "@":
                    should_draw_new_figure = False
                    break
            if not should_draw_new_figure:
                break
        if should_draw_new_figure:
            score += 1
            level = score // SCORE_TO_SWITCH_LEVEL + 1
            current_figures = next_figure
            next_figure = get_random_figure()
            next_figure_board.data = [[j if j == "x" else "" for j in i] for i in next_figure[0]]
            current_figure_position_in_list = 0
            result_of_drawing = draw_figure(current_figures, current_figure_position_in_list, 0, 5, board)
            if result_of_drawing == False:
                score -= 1
                # TODO: the end of the game
                insert_score_in_database(name, score)
                print("main.py:26 the game is over")
                return
        score += remove_filled_rows(board=board)
        level = score // SCORE_TO_SWITCH_LEVEL + 1
        falling_counter += 1
        screen.fill(BACK_GROUND_COLOR)
        board.render()
        next_figure_board.render()
        draw_text(screen, score, level, name)
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
