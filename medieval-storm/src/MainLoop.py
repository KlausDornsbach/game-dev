VERSION = "0.1"

try:
    from Settings import *
    import sys
    import os
    import time
    import random
    import math
    from Player import Player
    from Enemy import Enemy
except ImportError as err:
    print(f"couldn't load module. {err}")
    sys.exit(2)


KEYBOARD_CHECK = pg.event.custom_type()

def main():
    # Initialise screen
    pg.init()
    screen = pg.display.set_mode(RES_2)
    pg.display.set_caption('Basic Pygame program')

    clock = pg.time.Clock()

    # Fill background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(BG_COLOR)

    # some cool player
    player_pos = CENTER
    player_pos[1] += 200
    player = create_player(screen, player_pos)

    # some random enemy
    world_objects = []
    enemy = create_enemy(screen, (200, 200))

    world_objects.append(enemy)

    # Display some text
    font = pg.font.Font(None, 50)
    text = font.render("Medieval Storm", 1, WHITE_COLOR)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # pg.key.set_repeat(400, 270)

    # this will set a timer to check on keyboard events, so we get every x ms, making it less shaky
    pg.time.set_timer(KEYBOARD_CHECK, 150)

    # Event loop
    while 1:
        screen.blit(background, (0, 0))

        if handle_input(player, world_objects) == -1:
            break
    
        for o in world_objects:
            if is_on_screen(screen, o):
                blit_game_object(o)

        blit_game_object(player)
        
        clock.tick(60)
        pg.display.flip()


def create_player(screen, pos):
    player_object = pg.Surface((100, 100), pg.SRCALPHA)
    player_object.fill(PLAYER_COLOR)
    return Player(player_object, screen, pos, PLAYER_BASE_SPEED)


def create_enemy(screen, pos):
    player_object = pg.Surface((100, 100), pg.SRCALPHA)
    player_object.fill(RED_COLOR)
    return Enemy(player_object, screen, pos)


def is_on_screen(screen, object):
    if not screen.get_rect().colliderect(object.base_rect):
        return False
    return True


def blit_game_object(object):
    object.screen.blit(object.base_surface, object.base_rect)


def handle_input(player, world_objects):
    keys = pg.key.get_pressed()

    # player rotation on move
    # if keys[pg.K_w] or keys[pg.K_a] or keys[pg.K_s] or keys[pg.K_d]:
    #     player.rotate_player(keys)

    for o in world_objects:
        if keys[pg.K_w]:
            pass
            # player.move((0, -1), 4)
        if keys[pg.K_s]:
            pass
            # player.move((0, 1), 4)
        if keys[pg.K_a]:
            pass
            # player.move((-1, 0), 4)
        if keys[pg.K_d]:
            pass
            # player.move((1, 0), 4)

    if pg.event.peek(pg.QUIT):
        return -1
    
    # keyboard events
    if pg.event.peek(KEYBOARD_CHECK):
        player.rotate_player(pg.event.get())
    
    events = pg.event.get()
    for e in events:
        if e.type == pg.KEYDOWN or e.type == pg.KEYUP:
            player.rotate_player(e.type, e.key)
            pass
    
    # if event.type == pg.KEYDOWN:
    #     if event.key == pg.K_j:
    #         pass
    #         # player.rotate(CAMERA_ROTATION_ANGLE)
    #     if event.key == pg.K_k:
    #         pass
    #         # player.rotate(CAMERA_ROTATION_ANGLE)

    # player.rotate_player(pressed_keys)

    # for event in events:
    #     if event.type == pg.QUIT:
    #         return -1


def load_png(name):
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


if __name__ == '__main__': main()