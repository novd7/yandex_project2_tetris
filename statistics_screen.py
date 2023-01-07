import sys

import pygame
import pygame as pg

from constants import FPS, SIZE, TETRIS_LOGO_SIZE, START_SCREEN_BUTTONS, BUTTON_COLOR, BUTTON_TARGETED_COLOR, \
    DECO_TEXT_COLOR
from database import get_max_score_by_name


def terminate():  # Прерывание игры (через pg.QUIT или кнопкой "Выйти")
    pg.quit()
    sys.exit()


def statistics_screen(screen):
    def draw_line_of_text(text: str, color: tuple, x, y):
        font = pg.font.Font(None, 30)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
    screen.fill((0, 0, 0))
    pg.init()
    pg.display.set_caption('Статистика')
    clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
            draw_line_of_text("ТОП 10 игр по результату:", (255, 255, 255), 100, 10)
            data = get_max_score_by_name()
            for i in range(10):
                if len(data) == 0:
                    break
                else:
                    if i == 0:
                        col = (255, 215, 0)
                    elif i == 1:
                        col = (192, 192, 192)
                    elif i == 2:
                        col = (205, 127, 50)
                    else:
                        col = (255, 255, 255)
                    m = max(data, key=lambda x: x[1])
                    data.remove(m)
                    draw_line_of_text(f"{i + 1}. {m[0]} - {m[1]}", col, 10, 10 + (i + 1) * 20)
                

            # if event.type == pg.MOUSEMOTION:  # Выделение цветом кнопки, на которую наведён курсор
            #     if 125 <= event.pos[0] <= 355 and 300 <= event.pos[1] <= 340:  # Проверки позиции курсора
            #         draw_button(screen, START_SCREEN_BUTTONS[0], BUTTON_TARGETED_COLOR, font)
            #     elif 125 <= event.pos[0] <= 355 and 370 <= event.pos[1] <= 410:
            #         draw_button(screen, START_SCREEN_BUTTONS[1], BUTTON_TARGETED_COLOR, font)
            #     elif 125 <= event.pos[0] <= 355 and 440 <= event.pos[1] <= 480:
            #         draw_button(screen, START_SCREEN_BUTTONS[2], BUTTON_TARGETED_COLOR, font)
            #     else:
            #         for button in START_SCREEN_BUTTONS:
            #             draw_button(screen, button, BUTTON_COLOR, font)

            

        pg.display.flip()
        clock.tick(FPS)