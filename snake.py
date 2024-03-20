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
        self.surface_list.append(surface)
        self.pos = surface.get_rect()

    def blit(self):
        for surface in self.surface_list:
            sc.blit(surface, surface.get_rect())


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


def random_pos(rect):
    rect.x = random.randrange(0, app_resolution[0], 20)
    rect.y = random.randrange(0, app_resolution[1], 20)


if __name__ == '__main__':
    pg.font.init()
    sc = pg.display.set_mode(app_resolution)
    pg.time.set_timer(TIMER_EVENT, 160)
    sc.fill(GREY)
    snake = Snake()
    snake.blit()
    pg.display.update()
    direction = 'r'
    apple = Apple()
    apple.blit()

    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            if i.type == pg.KEYDOWN:
                print(i)
                if i.dict['key'] == 100:
                    direction = 'r'
                if i.dict['key'] == 97:
                    direction = 'l'
                if i.dict['key'] == 115:
                    direction = 'd'
                if i.dict['key'] == 119:
                    direction = 'u'
            if i.type == TIMER_EVENT:
                if snake.pos.x > app_resolution[0]:
                    snake.pos.x = 0
                if snake.pos.x < 0:
                    snake.pos.x = app_resolution[0]
                if snake.pos.y > app_resolution[1]:
                    snake.pos.y = 0
                if snake.pos.y < 0:
                    snake.pos.y = app_resolution[1]

                if direction == 'r':
                    snake.pos.move(20, 0)
                if direction == 'l':
                    snake.pos = snake.pos.move(-20, 0)
                if direction == 'd':
                    snake.pos = snake.pos.move(0, 20)
                if direction == 'u':
                    snake.pos = snake.pos.move(0, -20)

                sc.fill(GREY)

                if snake.pos == apple.get_rect():
                    apple.random_pos()

                apple.blit()
                snake.blit()

        pg.display.update()
        pg.time.delay(20)
        