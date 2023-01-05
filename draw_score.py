import pygame as pg

from constants import INDENT_LEFT, INDENT_TOP, WIDTH_OF_PLAYGROUND, CELL_SIZE


def draw_score(screen, score):
    font = pg.font.Font(None, 50)
    text1 = font.render("Счёт:", True, (100, 255, 100))
    text1_x = INDENT_LEFT + WIDTH_OF_PLAYGROUND * CELL_SIZE + INDENT_LEFT
    text1_y = INDENT_TOP
    screen.blit(text1, (text1_x, text1_y))
    text2 = font.render(str(score), True, (100, 255, 100))
    text2_x = INDENT_LEFT + WIDTH_OF_PLAYGROUND * CELL_SIZE + INDENT_LEFT
    text2_y = INDENT_TOP + text1.get_height()
    screen.blit(text2, (text2_x, text2_y))
    
