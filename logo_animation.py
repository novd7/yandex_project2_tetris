import pygame as pg
from constants import TETRIS_LOGO_SIZE, GAME_OVER_SIZE


def logo_animation(screen, iterations, logo_type):
    '''Анимация логотипов'''
    logo = pg.transform.scale(pg.image.load(f'data/{logo_type}/{logo_type}_{iterations}.png'),
                                     eval(f'{logo_type}_SIZE'.upper()))  # Загружаем логотип
    if logo_type == 'tetris_logo':  # Отображаем его на экране
        screen.blit(logo, (5, 110))
    else:
        screen.blit(logo, (90, 70))