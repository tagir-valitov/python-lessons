import pygame as pg
import sys

# 1. Создать приложение
# 2. Расчертить поле
#                           1 | 2 | 3
#                           ---------
#                           4 | 5 | 6
#                           ---------
#                           7 | 8 | 9
# 3. Написать функции которые будут изображать крестик и нолик
# 4. Отслеживание кликов мышки
# 5. Условие выйгрыша и проигрыша


def draw_circle(sc, center):
    pg.draw.circle(sc, WHITE, center, 50, 10)
        

def draw_x(sc, center):
    x = center[0]
    y = center[1]
    pg.draw.line(sc, WHITE, (x-50, y-50), (x+50, y+50), 10)
    pg.draw.line(sc, WHITE, (x+50, y-50), (x-50,y+50 ), 10)


def get_cell(pos):
    if pos[0] < 200 and pos[1] < 200:
        return 1
    if 400 > pos[0] >= 200 > pos[1]:
        return 2
    if 400 <= pos[0] < 600 and pos[1] < 200:
        return 3
    if pos[0] < 200 <= pos[1] < 400:
        return 4
    if 200 <= pos[0] < 400 and 200 <= pos[1] < 400:
        return 5
    if 600 > pos[0] >= 400 > pos[1] >= 200:
        return 6
    if pos[0] < 200 and 400 <= pos[1] < 600:
        return 7
    if 200 <= pos[0] < 400 <= pos[1] < 600:
        return 8
    if 400 <= pos[0] < 600 and 400 <= pos[1] < 600:
        return 9


def get_center(cell):
    match cell:
        case 1:
            return 100, 100
        case 2:
            return 300, 100
        case 3:
            return 500, 100
        case 4:
            return 100, 300
        case 5:
            return 300, 300
        case 6:
            return 500, 300
        case 7:
            return 100, 500
        case 8:
            return 300, 500
        case 9:
            return 500, 500


def draw_tic_tac_toe(is_x, center, sc):
    if is_x:
        draw_x(sc, center)
        return False
    else:
        draw_circle(sc, center)
        return True


def check_win(x):
    return (((1 in x and 2 in x and 3 in x) or (4 in x and 5 in x and 6 in x) or (7 in x and 8 in x and 9 in x)) or
            ((1 in x and 4 in x and 7 in x) or (2 in x and 5 in x and 8 in x) or (3 in x and 6 in x and 9 in x)) or
            (1 in x and 5 in x and 9 in x) or (7 in x and 5 in x and 3 in x))


def check_game(x, o):
    if check_win(x):
        return "x"
    if check_win(o):
        return "o"
    if len(x) + len(o) == 9:
        return 'd'
    return ""


def is_empty(cell, x, o):
    return not (cell in x or cell in o)


def restart_game(sc):
    sc.fill(GREY)
    pg.draw.line(sc, WHITE, (200, 0), (200, 600), 10)
    pg.draw.line(sc, WHITE, (0, 200), (600, 200), 10)
    pg.draw.line(sc, WHITE, (400, 0), (400, 600), 10)
    pg.draw.line(sc, WHITE, (0, 400), (600, 400), 10)


x = []
o = []
app_resolution = (600, 600)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
BLACK = (0, 0, 0)
is_x = True
if __name__ == '__main__':
    pg.font.init()
    sc = pg.display.set_mode(app_resolution)
    restart_game(sc)

    pg.display.update()
    while 1:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            if i.type == pg.KEYDOWN:
                x.clear()
                o.clear()
                is_x = True
                restart_game(sc)
            if i.type == pg.MOUSEBUTTONDOWN:
                if i.button == 1:
                    cell = get_cell(i.pos)
                    if is_empty(cell, x, o):
                        if is_x:
                            x.append(cell)
                        else:
                            o.append(cell)
                        center = get_center(cell)
                        is_x = draw_tic_tac_toe(is_x, center, sc)
                        result = check_game(x, o)
                        font = pg.font.Font(None, 72)
                        match result:
                            case "x":
                                text = font.render("Победили крестики", True, BLACK)
                                sc.blit(text, (55, 170))
                            case 'o':
                                text = font.render("Победили нолики", True, BLACK)
                                sc.blit(text, (75, 170))
                            case 'd':
                                text = font.render("Ничья", True, BLACK)
                                sc.blit(text, (230, 170))
        pg.display.update()
        pg.time.delay(20)
        