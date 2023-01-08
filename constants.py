"""File where all constants are situated"""

PROGRAM_NAME = "Тетрис"
SIZE = WIDTH, HEIGHT = 475, 625
FPS = 50
BACK_GROUND_COLOR = (0, 0, 0)
INITIAL_SPEED_OF_FIGURE_FALLING = 0.05
DELTA_SPEED_FOR_LEVEL = 0.025
SCORE_TO_SWITCH_LEVEL = 50

WIDTH_OF_PLAYGROUND = 13
HEIGHT_OF_PLAYGROUND = 24
INDENT_LEFT = 10
INDENT_TOP = 10
CELL_SIZE = 25
CELL_COLOR = (30, 30, 30)
MARKED_CELL_COLOR = (0, 140, 255)

TEXT_SCORE_SIZE = 24
TEXT_SCORE_COLOR = (100, 255, 100)
TEXT_SIZE = 20
TEXT_SCORE_SIGN_COLOR = (66, 170, 66)
TEXT_NEXT_SIZE = 10
TEXT_NEXT_COLOR = (178, 102, 255)

TETRIS_LOGO_SIZE = (464, 98)  # Размер логотипа игры
START_SCREEN_BUTTONS = (('Играть', (125, 300, 225, 40), (70, 5)),  # (button_text, button_rect, text_indents)
                        ('Статистика', (125, 370, 225, 40), (40, 5)),
                        ('Выйти', (125, 440, 225, 40), (72, 5)))
BUTTON_COLOR = (66, 170, 66)  # (150, 150, 150)  # Цвет кнопки
BUTTON_TARGETED_COLOR = (100, 255, 100)  # Цвет кнопки, на которую наведён курсор
BUTTON_TEXT_COLOR = (0, 0, 0)  # Цвет текста на кнопках
DECO_TEXT_COLOR = ((98, 0, 196), (136, 17, 255), (178, 102, 255))  # Цвета декораций

GAME_SCREEN_BUTTONS = (('Пауза', (345, 540, 120, 30), (35, 4)),  # (button_text, button_rect, text_indents)
                       ('Конец игры', (345, 580, 120, 30), (8, 4)))

GAME_OVER_SIZE = (309, 215)  # Размер надписи "GAME OVER"
END_SCREEN_BUTTONS = (('Новая игра', (30, 520, 200, 40), (35, 7)),  # (button_text, button_rect, text_indents)
                      ('В главное меню', (250, 520, 200, 40), (4, 7)))
NEW_RECORD_COLOR = ((255, 187, 0), (255, 231, 166))

STATISTICS_SCREEN_BUTTON = ('Назад', (125, 520, 225, 40), (72, 5))  # (button_text, button_rect, text_indents)
TOP_10_SIGN_COLOR = (0, 140, 255)