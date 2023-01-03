import pygame as pg

from board import Board
from get_random_figure import get_random_figure

FPS = 50
SIZE = WIDTH, HEIGHT = 450, 625


def main():
    pg.display.set_caption('Тетрис')
    screen = pg.display.set_mode(SIZE)
    
    clock = pg.time.Clock()
    running = True
    board = Board(screen=screen)
    current_figures = get_random_figure()
    current_figure_position_in_list = 1
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.get_click(event.pos)
        
        screen.fill('black')
        board.render()
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
