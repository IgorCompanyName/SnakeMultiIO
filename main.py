import pygame as pg
from snake import Snake
from colors import *
from constants import *
from food import *
from random import randint

pg.init()

# Multiplayer
# TODO: Remove all client-side snake operations and variables
# TODO: Move them to server-side, so that clients are only able to input and see stuff, not modify anything
# TODO: Server must have constant tick rate of 10 or something

screen = pg.display.set_mode(REAL_SIZE)
internal_screen = pg.Surface(SIZE)
Running = True
timer = pg.time.Clock()

snake = Snake((int(WIDTH / 2), int(HEIGHT / 2)), (0, 0))
foods = [Food.generate() for _ in range(FOODS_AT_A_TIME)]

def update():
    internal_screen.fill(BLACK)
    snake.step(foods)
    snake.draw(internal_screen)
    for food in foods:
        food.draw(internal_screen)

def main():
    global Running

    while Running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Running = False
            if event.type == pg.KEYDOWN or event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    snake.change_dir((-1, 0))
                elif event.key == pg.K_RIGHT:
                    snake.change_dir((1, 0))
                elif event.key == pg.K_UP:
                    snake.change_dir((0, -1))
                elif event.key == pg.K_DOWN:
                    snake.change_dir((0, 1))
                if DEBUG_MODE:
                    if event.key == pg.K_t:
                        snake.add_size()
        update()

        screen.blit(pg.transform.scale(internal_screen, screen.get_rect().size), (0, 0))
        pg.display.update()

        timer.tick(FRAMERATE)

if __name__ == "__main__":
    main()
else:
    raise RuntimeError("You cannot run this inside another file!")