import pygame as pg

from constants import INDENT_LEFT, INDENT_TOP, \
    WIDTH_OF_PLAYGROUND, CELL_SIZE, TEXT_SIZE, \
    TEXT_SCORE_COLOR, TEXT_SCORE_SIGN_COLOR, NEW_RECORD_COLOR, DECO_TEXT_COLOR
from database import get_max_score_by_name


def draw_text(screen, score, level, name, next_figure_text_color):
    """Function to draw text"""
    text_x = INDENT_LEFT + WIDTH_OF_PLAYGROUND * CELL_SIZE + INDENT_LEFT
    
    def draw_line_of_text(text: str, color: tuple, y, font_size):
        font = pg.font.Font(None, font_size)
        text = font.render(text, True, color)
        screen.blit(text, (text_x, y))
    
    text_y_score = INDENT_TOP
    draw_line_of_text("Счёт:", TEXT_SCORE_SIGN_COLOR, text_y_score, 30)
    
    text_y_score_num = text_y_score + TEXT_SIZE
    draw_line_of_text(str(score), TEXT_SCORE_COLOR, text_y_score_num, 50)
    
    text_y_level = text_y_score_num + TEXT_SIZE + 20
    draw_line_of_text("Уровень:", TEXT_SCORE_SIGN_COLOR, text_y_level, 25)
    
    text_y_level_num = text_y_level + TEXT_SIZE
    draw_line_of_text(str(level), TEXT_SCORE_COLOR, text_y_level_num, 30)
    
    text_y_your_best = text_y_level_num + TEXT_SIZE + 20
    draw_line_of_text("Ваш лучший", TEXT_SCORE_SIGN_COLOR, text_y_your_best, 25)
    
    text_y_result = text_y_your_best + TEXT_SIZE
    draw_line_of_text("результат:", TEXT_SCORE_SIGN_COLOR, text_y_result, 25)
    
    text_y_result_num = text_y_result + TEXT_SIZE
    res = get_max_score_by_name(name)
    draw_line_of_text(str(max(res) if res else 0), NEW_RECORD_COLOR[0], text_y_result_num, 30)
    
    text_y_next = text_y_result_num + TEXT_SIZE + 20
    draw_line_of_text("Следующая", DECO_TEXT_COLOR[next_figure_text_color], text_y_next, 30)
    
    text_y_figure = text_y_next + TEXT_SIZE
    draw_line_of_text("фигура:", DECO_TEXT_COLOR[next_figure_text_color], text_y_figure, 30)
