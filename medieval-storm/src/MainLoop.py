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

can_rotate_camera = True


KEYBOARD_CHECK = pg.event.custom_type()
CAMERA_ROTATION_DELAY_OVER = pg.event.custom_type()

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
    player = create_player(screen, PLAYER_POS)

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
    pg.time.set_timer(KEYBOARD_CHECK, PLAYER_KEYBOARD_CHECK_DELAY, loops=1)

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


def handle_input(player, world_objects):
    events = pg.event.get()
    keys = pg.key.get_pressed()

    global can_rotate_camera
    
    # player object rotation
    # sum vec stored out for also using in movement

    for event in events:
        sum_vec = VEC0
        if event.type == pg.QUIT:
            return -1
        
        if event.type == CAMERA_ROTATION_DELAY_OVER:
            can_rotate_camera = True
        
        if event.type == KEYBOARD_CHECK:
            pg.time.set_timer(KEYBOARD_CHECK, PLAYER_KEYBOARD_CHECK_DELAY, loops=1)

            # print(can_rotate, keys[pg.K_j])

            if can_rotate_camera and keys[pg.K_j]:
                print('rotate ->')
                for o in world_objects:
                    rotate_on_pivot(o, PLAYER_POS, -45)
                
                can_rotate_camera = False
                pg.time.set_timer(CAMERA_ROTATION_DELAY_OVER, ROTATION_DELAY, loops=1)


            if can_rotate_camera and keys[pg.K_k]:
                for o in world_objects:
                    rotate_on_pivot(o, PLAYER_POS, 45)

                can_rotate_camera = False
                pg.time.set_timer(CAMERA_ROTATION_DELAY_OVER, ROTATION_DELAY, loops=1)


            if keys[pg.K_w]:
                sum_vec = vector_add(sum_vec, vec2(0, -1))

            if keys[pg.K_a]:
                sum_vec = vector_add(sum_vec, vec2(-1, 0))

            if keys[pg.K_s]:
                sum_vec = vector_add(sum_vec, vec2(0, 1))

            if keys[pg.K_d]:
                sum_vec = vector_add(sum_vec, vec2(1, 0))

            if sum_vec == VEC0:
                continue

            # print('here')
            
            sum_vec.normalize_ip()
            player.rotate_player(sum_vec)
            
            # world object movement and rotation
            for o in world_objects:
                # print('move world')
                o.move(-sum_vec, player.speed)
            # print('about to rotate')
        

            



#### UTIL FUNCTIONS ####

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


def rotate_on_pivot(object, pivot, degrees):
    original_pivot = vec2(pivot)
    print(object.base_rect.center, pivot)
    obj_center = object.base_rect.center
    pivot_vector = vector_sub(vec2(obj_center), original_pivot)
    print(pivot_vector)
    
    object.rotate(degrees)

    pivot_vector = pivot_vector.rotate(degrees)
    print('pivot after', pivot_vector)
    pivot_vector = vector_add(original_pivot, pivot_vector)
    
    object.base_rect = object.base_surface.get_rect(center=pivot_vector)
    print(object.base_rect.center)


def vector_add(v1, v2):
    return vec2(v1.x + v2.x, v1.y + v2.y)


def vector_sub(v1, v2):
    return vec2(v1.x - v2.x, v1.y - v2.y)


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