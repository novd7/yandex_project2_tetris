import pygame as pg
import os
import sys
import sqlite3

import draw_figure
from board import Board
from constants import BACK_GROUND_COLOR, FPS, SIZE, INDENT_LEFT, WIDTH_OF_PLAYGROUND, CELL_SIZE, GAME_SCREEN_BUTTONS, \
    BUTTON_COLOR, BUTTON_TARGETED_COLOR
from constants import INITIAL_SPEED_OF_FIGURE_FALLING, \
    PROGRAM_NAME, DELTA_SPEED_FOR_LEVEL, SCORE_TO_SWITCH_LEVEL
from database import insert_score_in_database
from draw_button import draw_button
from draw_figure import draw_figure
from draw_text import draw_text
from get_random_figure import get_random_figure
from move_figure import move_figure
from remove_filled_rows import remove_filled_rows
from start_screen import start_screen
from turn_figure import turn_figure
from database import create_bd
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QWidget, QApplication
from get_name_from_dialog import GetName


def main():
    """Function of game process"""
    if not os.path.exists("data.sqlite"):
        create_bd()
    start_screen()
    
    app = QApplication(sys.argv)
    name = GetName()
    name = name.get_name()
    print("name =", name)
    pg.display.set_caption(PROGRAM_NAME)
    pg.display.set_caption('Тетрис')
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
    
    font = pg.font.Font(None, 27)  # Шрифт для кнопок "Пауза" и "Конец игры"
    mouse_pos = (0, 0)  # Изначальные кординаты курсора
    
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
            if event.type == pg.MOUSEMOTION:
                mouse_pos = event.pos  # Координаты курсора
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
        print(falling_counter % (1 / (INITIAL_SPEED_OF_FIGURE_FALLING + DELTA_SPEED_FOR_LEVEL * (level - 1))))
        if falling_counter % (round(1 / (INITIAL_SPEED_OF_FIGURE_FALLING + DELTA_SPEED_FOR_LEVEL * (level - 1)))) == 0:
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
        
        # Отрисовка кнопок "Пауза" и "Конец игры"
        if 345 <= mouse_pos[0] <= 465 and 540 <= mouse_pos[1] <= 570:  # Проверки позиции курсора
            draw_button(screen, GAME_SCREEN_BUTTONS[0], BUTTON_TARGETED_COLOR, font)
            draw_button(screen, GAME_SCREEN_BUTTONS[1], BUTTON_COLOR, font)
        elif 345 <= mouse_pos[0] <= 465 and 580 <= mouse_pos[1] <= 610:
            draw_button(screen, GAME_SCREEN_BUTTONS[1], BUTTON_TARGETED_COLOR, font)
            draw_button(screen, GAME_SCREEN_BUTTONS[0], BUTTON_COLOR, font)
        else:
            for button in GAME_SCREEN_BUTTONS:
                draw_button(screen, button, BUTTON_COLOR, font)
        
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
