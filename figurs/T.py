from random import randint
import pygame as pg
all_sprites = []

class T(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.orientations = {
            1: ['oxo',
                'xxx'],
            2: ['oxo',
                'oxx',
                'oxo'],
            3: ['xxx',
                'oxo'],
            4: ['oxo',
                'xxo',
                'oxo']
        }
        self.current_orientation = randint(1, 4)
        self.current_img = self.orientations[self.current_orientation]
        
        self.size = 20
        self.image = pg.Surface((self.size, self.size))
        self.image.fill("blue")
        self.all_cubes = []
        for koeff_y in range(len(self.current_img)):
            for koeff_x in range(len(self.current_img[koeff_y])):
                if self.current_img[koeff_y][koeff_x] == "x":
                    cur_x = x + self.size * (koeff_x - 1)
                    cur_y = y + self.size * koeff_y
                    self.all_cubes.append(
                        pg.Rect(
                            cur_x,
                            cur_y,
                            self.size,
                            self.size
                        )
                    )
    
    def update(self, *keys):
        if not pg.sprite.spritecollideany(self, platforms):
            self.rect = self.rect.move(0, 1)
            return
        if keys:
            keys = keys[0]
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.rect = self.rect.move(-1, 0)
            elif keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.rect = self.rect.move(1, 0)

T(0, 0)