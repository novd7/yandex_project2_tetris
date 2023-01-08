import pygame as pg

from constants import FPS, BACK_GROUND_COLOR, STATISTICS_SCREEN_BUTTON, BUTTON_COLOR, BUTTON_TARGETED_COLOR, \
    DECO_TEXT_COLOR, TOP_10_SIGN_COLOR
from database import get_max_score_by_name
from draw_button import draw_button
from terminate import terminate


def statistics_screen(screen):
    '''Экран статистики'''
    
    def draw_line_of_text(text: str, color: tuple, x, y, font_size=40):
        font = pg.font.Font(None, font_size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
    
    screen.fill((0, 0, 0))
    pg.init()
    pg.display.set_caption('Тетрис - Статистика')
    clock = pg.time.Clock()
    
    button_font = pg.font.Font(None, 40)  # Шрифт текста на кнопке
    draw_button(screen, STATISTICS_SCREEN_BUTTON, BUTTON_COLOR, button_font)
    
    cycle_iterations = 0  # Подсчёт итераций цикла (для работы анимаций)
    deco_frame = 0
    deco_color = 0
    deco_font = pg.font.Font(None, 50)  # Декоративный текст сверху и снизу экрана
    
    draw_line_of_text("ТОП-10 игр по результату:", TOP_10_SIGN_COLOR, 20, 70, 50)
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
            draw_line_of_text(f"{i + 1}. {m[0]} - {m[1]}", col, 20, 90 + (i + 1) * 30)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            if event.type == pg.MOUSEMOTION:
                if 125 <= event.pos[0] <= 350 and 520 <= event.pos[1] <= 560:
                    draw_button(screen, STATISTICS_SCREEN_BUTTON, BUTTON_TARGETED_COLOR, button_font)
                else:
                    draw_button(screen, STATISTICS_SCREEN_BUTTON, BUTTON_COLOR, button_font)
            if event.type == pg.MOUSEBUTTONDOWN:
                if 125 <= event.pos[0] <= 350 and 520 <= event.pos[1] <= 560:
                    from start_screen import start_screen
                    start_screen()
        
        cycle_iterations += 1
        if cycle_iterations == 10:  # Кадр логотипа и цвет декораций меняется на каждой 10-ой итерации цикла
            cycle_iterations = 0
            
            if deco_frame == 0:
                deco_text = deco_font.render('× - ' * 9 + '×', True, BACK_GROUND_COLOR)
                screen.blit(deco_text, (12, 10))
                screen.blit(deco_text, (12, 580))
                deco_text = deco_font.render('- × ' * 9 + '-', True, DECO_TEXT_COLOR[deco_color])
                deco_frame = 1
            else:
                deco_text = deco_font.render('- × ' * 9 + '-', True, BACK_GROUND_COLOR)
                screen.blit(deco_text, (12, 10))
                screen.blit(deco_text, (12, 580))
                deco_text = deco_font.render('× - ' * 9 + '×', True, DECO_TEXT_COLOR[deco_color])
                deco_frame = 0
            screen.blit(deco_text, (12, 10))
            screen.blit(deco_text, (12, 580))
            
            deco_color += 1
            if deco_color > 2:
                deco_color = 0
        
        pg.display.flip()
        clock.tick(FPS)
