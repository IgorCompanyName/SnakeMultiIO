import pygame as pg
from colors import *
from constants import *
from food import Food

def pos_equal(p1: tuple[int, int], p2: tuple[int, int]):
    return p1[0] == p2[0] and p1[1] == p2[1]

class Snake:
    def __init__(self, start_pos: tuple[int, int], start_dir: tuple[int, int]):
        self.pos = start_pos
        self.dir = start_dir
        self.size = 1
        self.history = [self.pos]
    
    def step(self, foods: list[Food]):
        self.pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
        for food in foods:
            if pos_equal(food.pos, self.pos) and not food.eaten:
                food.eaten = True
                self.add_size()
        for i in range(1, len(self.history)):
            pos = self.history[i]
            if pos_equal(self.pos, pos):
                end_game()
        if not DIES_ON_BORDER:
            if self.pos[0] >= WIDTH:
                self.pos = (0, self.pos[1])
            elif self.pos[0] < 0:
                self.pos = (WIDTH - 1, self.pos[1])
            if self.pos[1] >= HEIGHT:
                self.pos = (self.pos[0], 0)
            elif self.pos[1] < 0:
                self.pos = (self.pos[0], HEIGHT - 1)
        else:
            if self.pos[0] >= WIDTH or self.pos[0] < 0 or \
            self.pos[1] >= HEIGHT or self.pos[1] < 0:
                end_game()

        tmp = self.history.copy()
        self.history[0] = self.pos
        for i in range(1, len(self.history)):
            self.history[i] = tmp[i - 1]
    
    def add_size(self):
        self.size += 1
        self.history.append(self.pos)

    def change_dir(self, n_dir: tuple[int, int]):
        if self.size <= 2 or (self.dir[0] != -n_dir[0] and self.dir[1] != -n_dir[1]):
            self.dir = n_dir

    def draw(self, screen: pg.Surface):
        for pos in self.history:
            screen.set_at(pos, WHITE)