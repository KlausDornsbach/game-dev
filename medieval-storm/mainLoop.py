import sys
from settings import *


# def Game():
#     def __init__(self):
#         self.screen = pg.display.set_mode(RES)
#         self.clock = pg.time.Clock()
#         self.time = 0
#         self.delta_time = 0.01
    
#     def update(self):
#         pg.display.set_caption


def main():
    # Initialise screen
    pg.init()
    screen = pg.display.set_mode((1350, 800))
    pg.display.set_caption('Basic Pygame program')

    clock = pg.time.Clock()
    player = pg.Surface((100, 100))

    # Fill background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pg.font.Font(None, 36)
    text = font.render("Medieval Storm", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pg.display.flip()

    # some cool object
    surf = pg.Surface((100, 100))
    surf.convert()
    surf.fill((140, 140, 140))
    background.blit(surf, (100, 100))

    # Event loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.blit(background, (0, 0))
        pg.display.flip()


if __name__ == '__main__': main()
