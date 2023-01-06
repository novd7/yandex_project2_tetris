import pygame as pg
import sys

from constants import FPS, SIZE, TETRIS_LOGO_SIZE, START_SCREEN_BUTTONS, BUTTON_COLOR, BUTTON_TARGETED_COLOR, \
    BUTTON_TEXT_COLOR
from draw_buttons import draw_buttons

def terminate():  # Прерывание игры (через pg.QUIT или кнопкой "Выйти")
    pg.quit()
    sys.exit()


def start_screen():  # Стартовое окно
    pg.display.set_caption('Тетрис - Старт')
    screen = pg.display.set_mode(SIZE)
    clock = pg.time.Clock()

    tetris_logo = pg.transform.scale(pg.image.load('data/tetris_logo.png'), TETRIS_LOGO_SIZE)
    # Загружаем логотип "Тетриса"
    screen.blit(tetris_logo, (5, 75))  # Отображаем его на экране

    font = pg.font.Font(None, 40)  # Шрифт текста на кнопках

    draw_buttons(screen, BUTTON_COLOR, font, START_SCREEN_BUTTONS)

    while True:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                terminate()

            if event.type == pg.MOUSEMOTION:  # Выделение цветом кнопки, на которую наведён курсор
                if 125 <= event.pos[0] <= 355:  # Проверка позиции курсора по оси x
                    if 300 <= event.pos[1] <= 340:  # Проверки позиций курсора по оси y
                        draw_buttons(screen, BUTTON_TARGETED_COLOR, font, [START_SCREEN_BUTTONS[0]])
                    elif 370 <= event.pos[1] <= 410:
                        draw_buttons(screen, BUTTON_TARGETED_COLOR, font, [START_SCREEN_BUTTONS[1]])
                    elif 440 <= event.pos[1] <= 480:
                        draw_buttons(screen, BUTTON_TARGETED_COLOR, font, [START_SCREEN_BUTTONS[2]])

            if event.type == pg.MOUSEBUTTONDOWN:  # Действия, вызываемые нажатиями на кнопки
                if 125 <= event.pos[0] <= 355:  # Проверка позиции курсора по оси x
                    if 300 <= event.pos[1] <= 340:  # Проверки позиций курсора по оси y
                        return
                    elif 370 <= event.pos[1] <= 410:
                        # TODO: statistics call
                        pass
                    elif 440 <= event.pos[1] <= 480:
                        terminate()

        pg.display.flip()
        clock.tick(FPS)