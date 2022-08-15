import pygame as pg
import json

CFG = None
try:
    with open("config.json", "r") as config:
        CFG = json.loads(config.read())
except FileNotFoundError:
    print("You don't have config file yet! This is not allowed in current version, "
    "you have to create config.json yourself!")
    exit(0)

SIZE = WIDTH, HEIGHT = CFG['size']['width'], CFG['size']['height']
SCALING_FACTOR = SCALE_X, SCALE_Y = CFG['scale']['x'], CFG['scale']['y']
REAL_SIZE = REAL_WIDTH, REAL_HEIGHT = WIDTH * SCALE_X, HEIGHT * SCALE_Y
DIES_ON_BORDER = CFG['death_on_border']
FOOD_COLLECTABLE = CFG['food_is_collectable']
FOODS_AT_A_TIME = CFG['food_at_once']
DEBUG_MODE = CFG['debug_mode']
FRAMERATE = CFG['framerate']
GOD_MODE = CFG['god_mode']

def end_game():
    exit(0)
