import pygame as pg

from constants import WIDTH_OF_PLAYGROUND, \
    HEIGHT_OF_PLAYGROUND, INDENT_LEFT, INDENT_TOP, \
    CELL_SIZE, CELL_COLOR, MARKED_CELL_COLOR


class Board:
    # creating of the board
    def __init__(self, screen, width=WIDTH_OF_PLAYGROUND, height=HEIGHT_OF_PLAYGROUND):
        self.width = width
        self.height = height
        self.data = [["" for i in range(width)] for j in range(height)]
        self.coords_of_cubes_to_draw = []
        # coords of cubes (figures consist of them) to draw
        
        # default values
        self.left = INDENT_LEFT
        self.top = INDENT_TOP
        self.cell_size = CELL_SIZE
        self.screen = screen
    
    def render(self):
        screen = self.screen
        for coord_x, x in enumerate(range(self.left, self.width * self.cell_size + self.left, self.cell_size)):
            for coord_y, y in enumerate(range(self.top, self.height * self.cell_size + self.top, self.cell_size)):
                pg.draw.rect(
                    screen,
                    CELL_COLOR,
                    (x, y, self.cell_size, self.cell_size),
                    width=1
                )
                try:
                    if self.data[coord_y][coord_x]:
                        pg.draw.rect(
                            screen,
                            MARKED_CELL_COLOR,
                            (x + 1, y + 1, self.cell_size - 1, self.cell_size - 1)
                        )
                except IndexError:
                    continue
