from Settings import *
from GlobalVariables import object_id

class GameObject:
    # definitions of objects need a base rectangle, z axis rectangles, y and z components of the rects
    # will be squishified to take into consideration camera angle.
    def __init__(self, base_surface, screen, pos, type="", speed=1, hp=100, damage=50):
        global object_id
        self.id = object_id
        object_id += 1
        self.speed = speed
        self.base_surface = base_surface
        self.screen = screen
        self.base_rect = base_surface.get_rect(center = pos)
        self.original_surface = self.base_surface
        self.orientation = vec2(1, 0)
        self.type = type
        self.hp = hp
        self.damage = damage
        # squish on y axis
        self.scaleYByFactor(SQUISH_FACTOR_Y)


    def move(self, vec, speed_modifier = 1):
        self.base_rect = self.base_rect.move((vec[0]*speed_modifier, vec[1]*speed_modifier))


    def scaleYByFactor(self, factor):
        self.base_surface = pg.transform.scale(self.base_surface, (self.base_surface.get_width(), self.base_surface.get_height() * factor))


    def rotate(self, degrees):
        original_center = self.base_rect.center
        print('object orientation', self.orientation.as_polar()[1])
        print('object rotating: ', degrees + self.orientation.as_polar()[1])
        self.base_surface = pg.transform.rotate(self.original_surface, degrees + self.orientation.as_polar()[1])
        self.base_rect = self.base_surface.get_rect(center=original_center)
        self.orientation.rotate_ip(degrees)
        print('object orientation after', self.orientation.as_polar()[1])
        # self.orientation = self.orientation.x, int(self.orientation.y))
        # print(self.orientation)
        self.scaleYByFactor(SQUISH_FACTOR_Y)

