from GameObject import GameObject

class Enemy(GameObject):
    def __init__(self, object, screen, pos, base_speed = 1):
        super().__init__(object, screen, pos, base_speed)