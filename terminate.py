import pygame as pg
import sys


def terminate():
    '''Прерывание игры (через pg.QUIT или кнопкой "Выйти")'''
    pg.quit()
    sys.exit()