import sys

import pygame as pg


def terminate():
    '''Прерывание игры (через pg.QUIT или кнопкой "Выйти")'''
    pg.quit()
    sys.exit()
