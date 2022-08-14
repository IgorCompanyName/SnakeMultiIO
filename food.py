import pygame as pg
from colors import *
from constants import *
from random import randint

class Food:
    def __init__(self, pos: tuple[int, int]):
        self.pos = pos
        self.eaten = False
    
    def draw(self, screen: pg.Surface):
        if not self.eaten:
            screen.set_at(self.pos, FOOD_COLOR)

    def regenerate(self):
        self.eaten = False
        self.pos = (randint(0, WIDTH - 1), randint(0, HEIGHT - 1))

    @staticmethod
    def generate():
        return Food((randint(0, WIDTH - 1), randint(0, HEIGHT - 1)))