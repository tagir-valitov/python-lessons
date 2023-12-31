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

    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            if i.type == pg.KEYDOWN:
                print(i)
            if i.type == TIMER_EVENT:
                position = position.move(20, 0)
                sc.fill(GREY)
                sc.blit(snake, position)

        pg.display.update()
        pg.time.delay(20)
        