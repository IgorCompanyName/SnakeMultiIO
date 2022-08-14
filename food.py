import pygame as pg
from colors import *
from constants import *

class Food:
    def __init__(self, pos: tuple[int, int]):
        self.pos = pos
        self.eaten = False
    
    def draw(self, screen: pg.Surface):
        if not self.eaten:
            screen.set_at(self.pos, FOOD_COLOR)
