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

TIMER_EVENT = pg.USEREVENT + 1

if __name__ == '__main__':
    pg.font.init()
    sc = pg.display.set_mode(app_resolution)
    pg.time.set_timer(TIMER_EVENT, 100)  # 1 second = 1000 milliseconds
    sc.fill(GREY)
    snake = pg.Surface((20, 20))
    snake.fill(BLACK)
    position = snake.get_rect()
    sc.blit(snake, position)
    pg.display.update()
    direction = 'r'

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
                if position.x > app_resolution[0]:
                    position.x = 0
                if position.x < 0:
                    position.x = app_resolution[0]
                if position.y > app_resolution[1]:
                    position.y = 0
                if position.y < 0:
                    position.y = app_resolution[1]

                if direction == 'r':
                    position = position.move(20, 0)
                if direction == 'l':
                    position = position.move(-20, 0)
                if direction == 'd':
                    position = position.move(0, 20)
                if direction == 'u':
                    position = position.move(0, -20)

                sc.fill(GREY)
                sc.blit(snake, position)

        pg.display.update()
        pg.time.delay(20)
        