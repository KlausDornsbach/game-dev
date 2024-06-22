import math
import Settings
from GameObject import GameObject

class Player(GameObject):
    def __init__(self, object, screen, base_speed = 1):
        super().__init__(object, screen, base_speed)
        
    
