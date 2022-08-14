import pygame as pg
from colors import *
from constants import *

class Snake:
    def __init__(self, start_pos: tuple[int, int], start_dir: tuple[int, int]):
        self.pos = start_pos
        self.dir = start_dir
    
    def step(self):
        self.pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
        if not DIES_ON_BORDER:
            if self.pos[0] > WIDTH:
                self.pos = (0, self.pos[1])
            elif self.pos[0] < 0:
                self.pos = (WIDTH, self.pos[1])
            if self.pos[1] > HEIGHT:
                self.pos = (self.pos[0], 0)
            elif self.pos[1] < 0:
                self.pos = (self.pos[0], HEIGHT)
        else:
            if 0 > self.pos[0] > WIDTH or 0 > self.pos[1] > HEIGHT:
                exit(0)
    
    def change_dir(self, n_dir: tuple[int, int]):
        self.dir = n_dir

    def draw(self, screen: pg.Surface):
        screen.set_at(self.pos, WHITE)