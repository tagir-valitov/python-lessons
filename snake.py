import random
import pygame as pg
import sys

# 1. Сделать поле
# 2. Сделать змейку
# 3. Движение
# 4. Добавить яблоки
# 5. Логика победы/поражения
# 6. Размеры змейки


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
    pg.time.set_timer(TIMER_EVENT, 160)  # 1 second = 1000 milliseconds
    sc.fill(GREY)
    snake = pg.Surface((20, 20))
    snake.fill(BLACK)
    snake_pos = snake.get_rect()
    sc.blit(snake, snake_pos)
    pg.display.update()
    direction = 'r'
    apple = pg.Surface((20, 20))
    apple.fill(RED)
    apple_pos = apple.get_rect()
    random_pos(apple_pos)
    sc.blit(apple, apple_pos)

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
                if snake_pos.x > app_resolution[0]:
                    snake_pos.x = 0
                if snake_pos.x < 0:
                    snake_pos.x = app_resolution[0]
                if snake_pos.y > app_resolution[1]:
                    snake_pos.y = 0
                if snake_pos.y < 0:
                    snake_pos.y = app_resolution[1]

                if direction == 'r':
                    snake_pos = snake_pos.move(20, 0)
                if direction == 'l':
                    snake_pos = snake_pos.move(-20, 0)
                if direction == 'd':
                    snake_pos = snake_pos.move(0, 20)
                if direction == 'u':
                    snake_pos = snake_pos.move(0, -20)

                if snake_pos == apple_pos:
                    random_pos(apple_pos)

                sc.fill(GREY)
                sc.blit(snake, snake_pos)
                sc.blit(apple, apple_pos)

        pg.display.update()
        pg.time.delay(20)
        