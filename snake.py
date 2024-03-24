import random
import pygame as pg
import sys

# 1. Сделать поле
# 2. Сделать змейку
# 3. Движение
#   3.1. Новая поверхность змейки появляется со противоположной движению стороне
#   3.2. В следующем кадре голова змейки перемещается по направлению движения
#   3.3. В следующем кадре хвост перемещается на место предыдущей поверхности
# 4. Добавить яблоки
# 5. Логика победы/поражения
# 6. Размеры змейки


class Snake:
    def __init__(self):
        self.surface_list = []
        surface = pg.Surface((20, 20))
        surface.fill(BLACK)
        self.surface_list.append((surface, surface.get_rect()))
        self.direction = 'r'

    def blit(self):
        for surface, rect in self.surface_list:
            sc.blit(surface, rect)

    def update_direction(self, keydown_key):
        if keydown_key == 100:
            self.direction = 'r'
        if keydown_key == 97:
            self.direction = 'l'
        if keydown_key == 115:
            self.direction = 'd'
        if keydown_key == 119:
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

        if head_rect.x > app_resolution[0]:
            head_rect.x = 0
        if head_rect.x < 0:
            head_rect.x = app_resolution[0]
        if head_rect.y > app_resolution[1]:
            head_rect.y = 0
        if head_rect.y < 0:
            head_rect.y = app_resolution[1]

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
        surface.fill(BLACK)
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


class Apple:
    def __init__(self):
        self.surface = pg.Surface((20, 20))
        self.surface.fill(RED)
        self.rect = self.surface.get_rect()
        self.random_pos()

    def random_pos(self):
        self.rect.x = random.randrange(0, app_resolution[0], 20)
        self.rect.y = random.randrange(0, app_resolution[1], 20)

    def get_rect(self):
        return self.rect

    def blit(self):
        sc.blit(self.surface, self.rect)


app_resolution = (600, 400)

WHITE = (255, 255, 255)
GREY = (150, 150, 150)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

TIMER_EVENT = pg.USEREVENT + 1


if __name__ == '__main__':
    pg.font.init()
    sc = pg.display.set_mode(app_resolution)
    pg.time.set_timer(TIMER_EVENT, 160)
    sc.fill(GREY)

    snake = Snake()
    apple = Apple()

    snake.blit()
    apple.blit()

    pg.display.update()

    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            if i.type == pg.KEYDOWN:
                key = i.dict['key']
                snake.update_direction(key)
            if i.type == TIMER_EVENT:
                sc.fill(GREY)

                snake.adjust_border()
                snake.move()

                if snake.get_head_rect() == apple.get_rect():
                    apple.random_pos()
                    snake.add_surface()

                apple.blit()
                snake.blit()

        pg.display.flip()
        pg.time.delay(20)
        