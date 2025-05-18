import pygame as pg

class Snake:
    def __init__(self, color, app_resolution, sc):
        self.sc = sc
        self.color = color
        self.app_resolution = app_resolution
        self.surface_list = []
        surface = pg.Surface((20, 20))
        surface.fill(self.color)
        self.surface_list.append((surface, surface.get_rect()))
        self.direction = 'r'

    def blit(self):
        for surface, rect in self.surface_list:
            self.sc.blit(surface, rect)

    def update_direction(self, keydown_key):
        if keydown_key == 100 and self.direction != 'l':
            self.direction = 'r'
        if keydown_key == 97 and self.direction != 'r':
            self.direction = 'l'
        if keydown_key == 115 and self.direction != 'u':
            self.direction = 'd'
        if keydown_key == 119 and self.direction != 'd':
            self.direction = 'u'

    def get_head(self):
        return self.surface_list[0]

    def get_head_rect(self):
        return self.surface_list[0][1]

    def update_head_rect(self, rect):
        head, head_rect = self.get_head()
        self.surface_list[0] = (head, rect)

    def update_rect(self, index, rect):
        head, head_rect = self.get_head()
        self.surface_list[index] = (head, rect)

    def adjust_border(self):
        _, head_rect = self.get_head()

        if head_rect.x > self.app_resolution[0]:
            head_rect.x = 0
        if head_rect.x < 0:
            head_rect.x = self.app_resolution[0]
        if head_rect.y > self.app_resolution[1]:
            head_rect.y = 0
        if head_rect.y < 0:
            head_rect.y = self.app_resolution[1]

        self.update_head_rect(head_rect)

    def move(self):
        _, head_rect = self.get_head()

        prev_rect = head_rect

        for j in range(1, len(self.surface_list)):
            _, rect = self.surface_list[j]
            self.update_rect(j, prev_rect)
            prev_rect = rect

        if self.direction == 'r':
            head_rect = head_rect.move(20, 0)
        if self.direction == 'l':
            head_rect = head_rect.move(-20, 0)
        if self.direction == 'd':
            head_rect = head_rect.move(0, 20)
        if self.direction == 'u':
            head_rect = head_rect.move(0, -20)

        self.update_head_rect(head_rect)

    def add_surface(self):
        surface = pg.Surface((20, 20))
        surface.fill(self.color)
        rect = self.surface_list[-1][1]

        if self.direction == 'r':
            rect = rect.move(-20, 0)
        if self.direction == 'l':
            rect = rect.move(20, 0)
        if self.direction == 'd':
            rect = rect.move(0, -20)
        if self.direction == 'u':
            rect = rect.move(0, 20)

        self.surface_list.append((surface, rect))


    def check_lose(self):
        head_rect = self.get_head_rect()
        for j in range(1, len(self.surface_list)):
            _, rect = self.surface_list[j]
            if head_rect == rect:
                return True
        return False