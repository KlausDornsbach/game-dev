import math
from Settings import *
from GameObject import GameObject

class Player(GameObject):
    def __init__(self, object, screen, pos, base_speed = 1):
        super().__init__(object, screen, pos, base_speed)
        
    
    def move(self, keys):
        pass
    

    def rotate_player(self, vec):
        self.rotate(self.orientation.angle_to(vec))

    # def rotate_player(self, keys):
    #     if keys[pg.K_w] and keys[pg.K_d] and self.orientation != 45:
    #         self.rotate(45 - self.orientation)
    #         print("1")
    #         return
    #     elif keys[pg.K_w] and keys[pg.K_a] and self.orientation != 135:
    #         self.rotate(135 - self.orientation)
    #         return
    #     elif keys[pg.K_s] and keys[pg.K_a] and self.orientation != 225:
    #         # print('orientation before' + str(self.orientation))
    #         self.rotate(225 - self.orientation)
    #         # print('orientation after' + str(self.orientation))
    #         return
    #     elif keys[pg.K_s] and keys[pg.K_d] and self.orientation != 315:
    #         self.rotate(315 - self.orientation)
    #         return
    #     elif keys[pg.K_w] and self.orientation != 90:
    #         print("2")
    #         self.rotate(90 - self.orientation)
    #     elif keys[pg.K_s] and self.orientation != 270:
    #         self.rotate(270 - self.orientation)
    #     elif keys[pg.K_a] and self.orientation != 180:
    #         self.rotate(180 - self.orientation)
    #     elif keys[pg.K_d] and self.orientation != 0:
    #         self.rotate(0 - self.orientation)
    
    # def rotate_player(self, events):
    #     keydown_events = list(filter(lambda ev: ev.type == pg.KEYDOWN, events))
    #     events = list(map(lambda ev: ev.key, keydown_events))
    #     print(events)


    #     sum_vec = vec2()

    #     if pg.K_w in events and pg.K_d in events and self.orientation != 45:
    #         self.rotate(90 - self.orientation)
    #         pg.event.pump()
    #         return
    #     elif pg.K_w in events and pg.K_a in events and self.orientation != 135:
    #         self.rotate(135 - self.orientation)
    #         pg.event.pump()
    #         return
    #     elif pg.K_s in events and pg.K_a in events and self.orientation != 225:
    #         self.rotate(225 - self.orientation)
    #         pg.event.pump()
    #         return
    #     elif pg.K_s in events and pg.K_d in events and self.orientation != 315:
    #         self.rotate(315 - self.orientation)
    #         pg.event.pump()
    #         return
    #     if pg.K_w in events and self.orientation != 90:
    #         self.rotate(90 - self.orientation)
    #     elif pg.K_s in events and self.orientation != 270:
    #         self.rotate(270 - self.orientation)
    #     elif pg.K_a in events and self.orientation != 180:
    #         self.rotate(180 - self.orientation)
    #     elif pg.K_d in events and self.orientation != 0:
    #         self.rotate(0 - self.orientation)