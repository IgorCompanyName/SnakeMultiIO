import pygame as pg
from colors import *

class Snake:
    def __init__(self, start_pos: tuple[int, int], start_dir: tuple[int, int]):
        self.pos = start_pos
        self.dir = start_pos
    
    def step(self):
        self.pos += self.dir
    
    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, WHITE, self.pos + (16, 16))