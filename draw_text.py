import pygame as pg

from constants import INDENT_LEFT, INDENT_TOP, \
    WIDTH_OF_PLAYGROUND, CELL_SIZE, TEXT_SCORE_SIZE, \
    TEXT_SCORE_COLOR, TEXT_NEXT_SIZE, TEXT_NEXT_COLOR


def draw_text(screen, score):
    font = pg.font.Font(None, 50)
    
    text1 = font.render("Счёт:", True, TEXT_SCORE_COLOR)
    text1_x = INDENT_LEFT + WIDTH_OF_PLAYGROUND * CELL_SIZE + INDENT_LEFT
    text1_y = INDENT_TOP
    screen.blit(text1, (text1_x, text1_y))
    
    text2 = font.render(str(score), True, TEXT_SCORE_COLOR)
    text2_x = text1_x
    text2_y = text1_y + TEXT_SCORE_SIZE
    screen.blit(text2, (text2_x, text2_y))
    
    font3 = pg.font.Font(None, 30)
    
    text3 = font3.render("Следующая", True, TEXT_NEXT_COLOR)
    text3_x = text1_x
    text3_y = text2_y + TEXT_SCORE_SIZE + INDENT_TOP + INDENT_TOP
    screen.blit(text3, (text3_x, text3_y))
    
    text4 = font3.render("фигура:", True, TEXT_NEXT_COLOR)
    text4_x = text1_x
    text4_y = text3_y + TEXT_NEXT_SIZE
    screen.blit(text4, (text4_x, text4_y))