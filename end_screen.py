import pygame as pg

from constants import FPS, SIZE, BACK_GROUND_COLOR, END_SCREEN_BUTTONS, BUTTON_COLOR, \
    BUTTON_TARGETED_COLOR, DECO_TEXT_COLOR, TEXT_SCORE_COLOR, TEXT_SCORE_SIGN_COLOR, NEW_RECORD_COLOR
from draw_button import draw_button
from logo_animation import logo_animation
from main import main
from start_screen import start_screen
from particle_system import all_sprites, create_particles
from terminate import terminate


def end_screen(score, max_score):
    '''Конечное окно'''
    pg.init()
    pg.display.set_caption('Тетрис - Игра окончена')
    screen = pg.display.set_mode(SIZE)
    clock = pg.time.Clock()
    
    cycle_iterations = 0  # Подсчёты итераций цикла (для работы анимаций)
    logo_frame = 1  # Номер кадра логотипа
    
    score_sign_font = pg.font.Font(None, 30)  # Шрифт надписи "Счёт:"
    
    if len(str(score)) == 1:  # Положение счётчика очков
        score_pos = (235, 350)
    elif len(str(score)) == 2:
        score_pos = (225, 350)
    elif len(str(score)) == 3:
        score_pos = (215, 350)
    else:
        score_pos = (205, 350)
    score_num_font = pg.font.Font(None, 50)  # Шрифт cчётчика

    max_score = max_score if type(max_score) == int else max_score[0]  # Максимальный счёт
    new_record_font = pg.font.Font(None, 50)  # Шрифт надписи "Новый рекорд!"
    new_record_color = 0
    
    deco_frame = 0
    deco_color = 0
    deco_font = pg.font.Font(None, 50)  # Декоративный текст сверху и снизу экрана
    
    button_font = pg.font.Font(None, 35)  # Шрифт текста на кнопках
    
    for button in END_SCREEN_BUTTONS:  # Отрисовка кнопок
        draw_button(screen, button, BUTTON_COLOR, button_font)

    mouse_pos = (0, 0)  # Позиция курсора

    particles_been_played = False  # Частицы ещё не проигрывались
    while True:
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                terminate()
            
            if event.type == pg.MOUSEMOTION:  # Выделение цветом кнопки, на которую наведён курсор
                mouse_pos = event.pos
            
            if event.type == pg.MOUSEBUTTONDOWN:  # Действия, вызываемые нажатиями на кнопки
                if 520 <= event.pos[1] <= 560:  # Проверка позиции курсора по оси x
                    if 30 <= event.pos[0] <= 230:  # Проверки позиций курсора по оси y
                        main()
                    elif 250 <= event.pos[0] <= 450:
                        start_screen()

        screen.fill(BACK_GROUND_COLOR)  # Заливка экрана чёрным для дальнейшей отрисовки объектов
        logo_animation(screen, logo_frame, 'game_over')  # Надпись "GAME OVER"

        if 30 <= mouse_pos[0] <= 230 and 520 <= mouse_pos[1] <= 560:  # Проверки позиции курсора
            draw_button(screen, END_SCREEN_BUTTONS[0], BUTTON_TARGETED_COLOR, button_font)  # и отрисовка кнопок
            draw_button(screen, END_SCREEN_BUTTONS[1], BUTTON_COLOR, button_font)
        elif 250 <= mouse_pos[0] <= 450 and 520 <= mouse_pos[1] <= 560:
            draw_button(screen, END_SCREEN_BUTTONS[0], BUTTON_COLOR, button_font)
            draw_button(screen, END_SCREEN_BUTTONS[1], BUTTON_TARGETED_COLOR, button_font)
        else:
            for button in END_SCREEN_BUTTONS:
                draw_button(screen, button, BUTTON_COLOR, button_font)

        score_sign = score_sign_font.render('Счёт:', True, TEXT_SCORE_SIGN_COLOR)  # Надпись "Счёт:"
        screen.blit(score_sign, (220, 320))
        score_num = score_num_font.render(str(score), True, TEXT_SCORE_COLOR)  # Счёт
        screen.blit(score_num, score_pos)

        if deco_frame == 0:  # Декорации
            deco_text = deco_font.render('- × ' * 9 + '-', True, DECO_TEXT_COLOR[deco_color])
        else:
            deco_text = deco_font.render('× - ' * 9 + '×', True, DECO_TEXT_COLOR[deco_color])
        screen.blit(deco_text, (12, 10))
        screen.blit(deco_text, (12, 580))

        if score > max_score:  # Если новый рекорд...

            if not particles_been_played:
                create_particles((237, 445))
                particles_been_played = True
            all_sprites.update()
            all_sprites.draw(screen)
            pg.display.flip()

            new_record = new_record_font.render('Новый рекорд!', True, NEW_RECORD_COLOR[new_record_color])
            screen.blit(new_record, (110, 420))

        cycle_iterations += 1
        if cycle_iterations == 10:  # Кадр логотипа, цвет и положение декораций меняется на каждой 10-ой итерации цикла

            if deco_frame == 0:
                deco_frame = 1
            else:
                deco_frame = 0
            if new_record_color == 0:
                new_record_color = 1
            else:
                new_record_color = 0

            deco_color += 1
            if deco_color > 2:
                deco_color = 0
            logo_frame += 1
            if logo_frame > 15:
                logo_frame = 1
            cycle_iterations = 0

        pg.display.flip()
        clock.tick(FPS)
