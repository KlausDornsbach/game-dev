import pygame as pg
import math

vec2 = pg.math.Vector2

RES_2 = vec2(1350, 800)
RES = WIDTH, HEIGHT = vec2(1920, 1080)
CENTER = H_WIDTH, H_HEIGHT = RES_2 // 2

BG_COLOR = (20, 30, 46)
PLAYER_COLOR = (0, 0, 255)
WHITE_COLOR = (255, 255, 255)
RED_COLOR = (255, 0, 0)

CAMERA_ANGLE_DEGREES = 60
CAMERA_ROTATION_ANGLE = 45
ROTATION_TIME = 1000

# taking into consideration my pseudo perspective
SQUISH_FACTOR_Y = math.cos(math.radians(CAMERA_ANGLE_DEGREES))

# player stuff
PLAYER_BASE_SPEED = 2