import pygame as pg
from constants import BUTTON_TEXT_COLOR


def draw_button(screen, button, button_color, font):  # Функция для отрисовки кнопок
    pg.draw.rect(screen, button_color, button[1])
    button_text = font.render(button[0], True, BUTTON_TEXT_COLOR)
    button_text_x = button[1][0] + button[2][0]  # button_x + button_text_indent_x
    button_text_y = button[1][1] + button[2][1]  # button_y + button_text_indent_y
    screen.blit(button_text, (button_text_x, button_text_y))