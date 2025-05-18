import random
import pygame as pg

class Apple:
    def __init__(self, color, app_resolution, sc):
        self.sc = sc
        self.app_resolution = app_resolution
        self.surface = pg.Surface((20, 20))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.random_pos()

    def random_pos(self):
        self.rect.x = random.randrange(0, self.app_resolution[0], 20)
        self.rect.y = random.randrange(0, self.app_resolution[1], 20)

    def get_rect(self):
        return self.rect

    def blit(self):
        self.sc.blit(self.surface, self.rect)