from Settings import *
from GameObject import GameObject

class Player(GameObject):
    def __init__(self, object, screen, pos, speed = 1):
        super().__init__(object, screen, pos, 'player', speed)
        

    def rotate_player(self, vec):
        self.rotate(self.orientation.angle_to(vec))


    def attack(self):
        attack_hitbox = pg.Surface(BASIC_ATTACK_HITBOX_DIMENSIONS, pg.SRCALPHA)
        attack_hitbox.fill(GREEN_COLOR)
        attack_hitbox_center = vec2(self.base_rect.center) + (self.orientation * 3)

        attack = GameObject(attack_hitbox, self.screen, attack_hitbox_center)
        return attack
    

    def play_attack_sound(self):
        pass
