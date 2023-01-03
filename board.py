import pygame as pg


class Board:
    # creating of the board
    def __init__(self, screen, width=13, height=24):
        self.width = width
        self.height = height
        self.board = [["" for i in range(width)] for j in range(height)]
        self.coords_of_cubes_to_draw = []
        # coords of cubes (figures consist of them) to draw
        
        # default values
        self.left = 10
        self.top = 10
        self.cell_size = 25
        self.screen = screen
    
    # settings of the front view
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
    
    def render(self):
        screen = self.screen
        for coord_x, x in enumerate(range(self.left, self.width * self.cell_size + self.left, self.cell_size)):
            for coord_y, y in enumerate(range(self.top, self.height * self.cell_size + self.top, self.cell_size)):
                pg.draw.rect(
                    screen,
                    'white',
                    (x, y, self.cell_size, self.cell_size),
                    width=1
                )
    
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
    
    def get_cell(self, mouse_pos):
        mx, my = mouse_pos
        if mx <= self.left or mx >= self.width * self.cell_size + self.left or \
            my <= self.top or my >= self.height * self.cell_size + self.top:
            return
        
        column = (mx - self.left) // self.cell_size
        row = (my - self.top) // self.cell_size
        return row, column
    
    def on_click(self, cell):
        try:
            print("board.py:50", cell, self.board[cell[0]][cell[1]])
        except TypeError:
            print("board.py:52 You're out of board")
            
    