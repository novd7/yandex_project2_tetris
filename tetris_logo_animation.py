import pygame as pg
from constants import TETRIS_LOGO_SIZE


def tetris_logo_animation(screen, iterations):  # Анимация логотипа игры
    '''Анимация логотипа тетриса'''
    tetris_logo = pg.transform.scale(pg.image.load(f'data/tetris_logo/tetris_logo_{iterations}.png'), TETRIS_LOGO_SIZE)
    # Загружаем логотип "Тетриса"
    screen.blit(tetris_logo, (5, 110))  # Отображаем его на экране