import pygame as pg


class AddBorders(pg.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites, borders)
        self.image = pg.Surface((abs(x1 - x2), abs(y1 - y2)))
        self.image.fill("gray")
        self.rect = pg.Rect(x, y, 50, 10)