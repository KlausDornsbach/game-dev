VERSION = "0.1"

try:
    from Settings import *
    import sys
    import os
    import time
    import random
    import math
    from EventHandler import EventHandler
    from Player import Player
    from Enemy import Enemy
    from Utils import Utils

except ImportError as err:
    print(f"couldn't load module. {err}")
    sys.exit(2)


def main():
    utils = Utils()

    # Initialise screen
    pg.init()
    screen = pg.display.set_mode(RES)
    pg.display.set_caption('Basic Pygame program')

    clock = pg.time.Clock()

    # Fill background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(BG_COLOR)

    # some cool player
    player = utils.create_player(screen, PLAYER_POS)

    # some random enemy
    world_objects = []
    enemy = utils.create_enemy(screen, (200, 200))

    world_objects.append(enemy)

    # Display some text
    font = pg.font.Font(None, 50)
    text = font.render("Medieval Storm", 1, WHITE_COLOR)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # pg.key.set_repeat(400, 270)

    # this little guy also handles input
    event_handler = EventHandler(utils)
    event_handler.create_keyboard_timer()

    # Event loop
    while 1:
        screen.blit(background, (0, 0))

        if event_handler.handle_input(player, world_objects) == -1:
            break
    
        for o in world_objects:
            if utils.is_on_screen(screen, o):
                utils.blit_game_object(o)

        utils.blit_game_object(player)
        
        clock.tick(CLOCK_TICK)
        pg.display.flip()

if __name__ == '__main__': main()