import pygame as pg
from figurs.T import T
# from add_borders import AddBorders

SIZE = WIDTH, HEIGHT = 750, 500
FPS = 50

pg.init()
screen = pg.display.set_mode(SIZE)
all_sprites = pg.sprite.Group()
player = pg.sprite.Group()
borders = pg.sprite.Group()
current = pg.sprite.Group()


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, player)
        self.orientation = "vertical"
        self.size = (20, 100)
        self.image = pg.Surface(self.size)
        self.image.fill("blue")
        
        self.rect = pg.Rect(x, y, *self.size)

    def update(self, *keys):
        if not pg.sprite.spritecollideany(self, borders):
            self.rect = self.rect.move(0, 1)
            return
        if keys:
            keys = keys[0]
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.rect = self.rect.move(-1, 0)
            elif keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.rect = self.rect.move(1, 0)


class AddBorders(pg.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites, borders)
        self.image = pg.Surface((abs(x1 - x2), abs(y1 - y2)))
        self.image.fill("gray")
        self.rect = pg.Rect(x1, y1, x2, y2)


def main():
    # global all_sprites, player, borders, current
    running = True
    clock = pg.time.Clock()
    AddBorders(0, HEIGHT, WIDTH, HEIGHT + 1)

    player = None
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 3:
                    if not player:
                        player = T(*event.pos)
                    # else:
                    #     player.rect.x, player.rect.y = event.pos
                # if event.button == 1:
                #     pass

        screen.fill('black')
        all_sprites.draw(screen)
        keys = pg.key.get_pressed()
        all_sprites.update(keys)
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
    pg.quit()
