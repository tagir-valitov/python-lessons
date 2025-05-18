from apple import Apple
from snake import Snake
import pygame as pg
import sys

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

    snake = Snake(BLACK, app_resolution, sc)
    apple = Apple(RED, app_resolution, sc)

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
                if snake.check_lose():
                    print('Вы проиграли')
                    font = pg.font.Font(None, 74)
                    text = font.render("Вы проиграли", True, BLACK)
                    sc.blit(text, (0, 0))
                    pg.time.wait(10000)
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
        