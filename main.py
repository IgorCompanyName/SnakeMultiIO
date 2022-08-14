import pygame as pg
from snake import Snake

pg.init()
SIZE = WIDTH, HEIGHT = 800, 600

screen = pg.display.set_mode(SIZE)
Running = True
timer = pg.time.Clock()

snake = Snake((0, 0), 1, 1)

def update():
    snake.step()
    snake.draw(screen)

def main():
    while Running:
        for event in pg.event.get():
            if event == pg.QUIT:
                Running = False
        update()
        pg.display.update()
        timer.tick(5)

if __name__ == "__main__":
    main()
else:
    raise RuntimeError("You cannot run this inside another file!")