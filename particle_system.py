import pygame
from random import choice
from constants import WIDTH, HEIGHT, GRAVITY

all_sprites = pygame.sprite.Group()
screen_rect = (0, 0, WIDTH, HEIGHT)


class Particle(pygame.sprite.Sprite):
    '''Класс частиц'''
    shiny = [pygame.image.load("data/shiny.png")]
    for scale in (10, 20, 30):
        shiny.append(pygame.transform.scale(shiny[0], (scale, scale)))
    del shiny[0]

    def __init__(self, pos, delta_x, delta_y):
        super().__init__(all_sprites)
        self.image = choice(self.shiny)
        self.rect = self.image.get_rect()

        self.v = [delta_x, delta_y]  # Скорость частицы
        self.rect.x, self.rect.y = pos  # Координаты частицы

        self.gravity = GRAVITY

    def update(self):
        self.v[1] += self.gravity  # Движение под действием гравитации
        self.rect.x += self.v[0]  # Движение под действием скорости
        self.rect.y += self.v[1]
        if not self.rect.colliderect(screen_rect):  # Если частица ушла за экран - уничтожаем
            self.kill()


def create_particles(position):
    '''Создание частиц'''
    particle_count = 80  # Кол-во частиц
    values_of_v = range(-30, 30)  # Возможные скорости
    for _ in range(particle_count):
        Particle(position, choice(values_of_v), choice(values_of_v))