from GameObject import GameObject

class Enemy(GameObject):
    def __init__(self, object, screen, pos, base_speed = 1):
        super().__init__(object, screen, pos, 'enemy', base_speed)

    
    def get_hit(self, hit_direction):
        self.move(hit_direction, 5)


    def die():
        pass
