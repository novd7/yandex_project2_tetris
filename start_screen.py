import sys

import pygame as pg

from constants import FPS, SIZE, TETRIS_LOGO_SIZE, START_SCREEN_BUTTONS, BUTTON_COLOR, BUTTON_TARGETED_COLOR, \
    DECO_TEXT_COLOR
from draw_button import draw_button
from tetris_logo_animation import tetris_logo_animation


def terminate():  # Прерывание игры (через pg.QUIT или кнопкой "Выйти")
    pg.quit()
    sys.exit()


def start_screen():  # Стартовое окно
    pg.display.set_caption('Тетрис - Старт')
    screen = pg.display.set_mode(SIZE)
    clock = pg.time.Clock()

    cycle_iterations = 0  # Подсчёт итераций цикла (для работы анимаций)
    logo_frame = 1  # Номер кадра логотипа
    deco_frame = 0

    font = pg.font.Font(None, 40)  # Шрифт текста на кнопках

    for button in START_SCREEN_BUTTONS:  # Отрисовка кнопок
        draw_button(screen, button, BUTTON_COLOR, font)

    deco_font = pg.font.Font(None, 50)  # Декоративный текст сверху и снизу экрана


    while True:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                terminate()

            if event.type == pg.MOUSEMOTION:  # Выделение цветом кнопки, на которую наведён курсор
                if 125 <= event.pos[0] <= 355 and 300 <= event.pos[1] <= 340:  # Проверки позиции курсора
                    draw_button(screen, START_SCREEN_BUTTONS[0], BUTTON_TARGETED_COLOR, font)
                elif 125 <= event.pos[0] <= 355 and 370 <= event.pos[1] <= 410:
                    draw_button(screen, START_SCREEN_BUTTONS[1], BUTTON_TARGETED_COLOR, font)
                elif 125 <= event.pos[0] <= 355 and 440 <= event.pos[1] <= 480:
                    draw_button(screen, START_SCREEN_BUTTONS[2], BUTTON_TARGETED_COLOR, font)
                else:
                    for button in START_SCREEN_BUTTONS:
                        draw_button(screen, button, BUTTON_COLOR, font)

            if event.type == pg.MOUSEBUTTONDOWN:  # Действия, вызываемые нажатиями на кнопки
                if 125 <= event.pos[0] <= 355:  # Проверка позиции курсора по оси x
                    if 300 <= event.pos[1] <= 340:  # Проверки позиций курсора по оси y
                        return
                    elif 370 <= event.pos[1] <= 410:
                        # TODO: statistics call
                        pass
                    elif 440 <= event.pos[1] <= 480:
                        terminate()

        cycle_iterations += 1
        if cycle_iterations == 10:  # Кадр логотипа и цвет декораций меняется на каждой 5-ой итерации цикла
            cycle_iterations = 0
            tetris_logo_animation(screen, logo_frame)
            deco_text = deco_font.render('- × - × - × - × - × - × - × - × - × -', True, DECO_TEXT_COLOR[deco_frame])
            screen.blit(deco_text, (12, 10))
            screen.blit(deco_text, (12, 580))

            deco_frame += 1
            if deco_frame > 2:
                deco_frame = 0
            logo_frame += 1
            if logo_frame > 15:
                logo_frame = 1

        pg.display.flip()
        clock.tick(FPS)