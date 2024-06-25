from Settings import *
from Player import Player
from Enemy import Enemy
from EventHandler import *

thirds_lerp_curve = [34, 56, 71, 81, 87, 91, 94, 96, 97, 99, 100]

#### UTIL FUNCTIONS ####
class Utils:
    def create_player(self, screen, pos):
        player_object = pg.Surface(PLAYER_DIMENSIONS, pg.SRCALPHA)
        player_object.fill(PLAYER_COLOR)
        return Player(player_object, screen, pos, PLAYER_BASE_SPEED)


    def create_enemy(self, screen, pos):
        player_object = pg.Surface((100, 100), pg.SRCALPHA)
        player_object.fill(RED_COLOR)
        return Enemy(player_object, screen, pos)


    def create_camera_rotation_event(self, degrees, index=0):
        properties = dict()
        properties['degrees'] = degrees
        properties['index'] = index
        properties['curve'] = thirds_lerp_curve
        return pg.event.Event(CAMERA_ROTATION_EVENT, properties)


    def is_on_screen(self, screen, object):
        if not screen.get_rect().colliderect(object.base_rect):
            return False
        return True


    def blit_game_object(self, object):
        object.screen.blit(object.base_surface, object.base_rect)


    def rotate_on_pivot(self, object, pivot, degrees):
        original_pivot = vec2(pivot)
        print('center of the base rect, and pivot (player)', object.base_rect.center, pivot)
        obj_center = object.base_rect.center
        pivot_vector = self.vector_sub(vec2(obj_center), original_pivot)
        print('pivot vector', pivot_vector)
        
        object.rotate(degrees)

        pivot_vector = pivot_vector.rotate(degrees)
        print('pivot after', pivot_vector)
        pivot_vector = self.vector_add(original_pivot, pivot_vector)
        
        object.base_rect = object.base_surface.get_rect(center=pivot_vector)
        print(object.base_rect.center)


    def vector_add(self, v1, v2):
        return vec2(v1.x + v2.x, v1.y + v2.y)


    def vector_sub(self, v1, v2):
        return vec2(v1.x - v2.x, v1.y - v2.y)


    def load_png(self, name):
        """ Load image and return image object"""
        fullname = os.path.join("data", name)
        try:
            image = pg.image.load(fullname)
            if image.get_alpha is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except FileNotFoundError:
            print(f"Cannot load image: {fullname}")
            raise SystemExit
        return image, image.get_rect()
