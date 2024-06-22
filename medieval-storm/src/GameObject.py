from Settings import *

class GameObject:
    # definitions of objects need a base rectangle, z axis rectangles, y and z components of the rects
    # will be squishified to take into consideration camera angle.
    def __init__(self, base_surface, screen, base_speed):
        self.base_speed = base_speed
        self.base_surface = base_surface
        self.screen = screen
        self.base_rect = base_surface.get_rect()
        self.original_surface = self.base_surface
        self.object_orientation = 0
        # squish on y axis
        self.scaleYByFactor(SQUISH_FACTOR_Y)


    def move(self, vec, modifier = 1):
        self.base_rect = self.base_rect.move((vec[0]*modifier*self.base_speed, vec[1]*modifier*self.base_speed))


    def scaleYByFactor(self, factor):
        self.base_surface = pg.transform.scale(self.base_surface, (self.base_surface.get_width(), self.base_surface.get_height() * factor))


    def rotate(self, degrees):
        original_center = self.base_rect.center
        self.base_surface = pg.transform.rotate(self.original_surface, degrees + self.object_orientation)
        self.base_rect = self.base_surface.get_rect(center=original_center)
        self.object_orientation += degrees
        self.scaleYByFactor(SQUISH_FACTOR_Y)