import sys
from Settings import *
from Player import Player


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

    # Fill background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(BG_COLOR)

    # test surface
    # test = pg.Surface((100, 100)).convert_alpha()
    # test.fill(RED_COLOR)
    # rotated_test = pg.transform.rotate(test, 100)

    # Blit everything to the screen
    screen.blit(background, (0, 0))

    # screen.blit(test, (100, 100))
    # screen.blit(rotated_test, (300, 300))
    pg.display.flip()

    # some cool player
    player = create_player(screen)

    # Display some text
    font = pg.font.Font(None, 36)
    text = font.render("Medieval Storm debug variable: " + str(player.base_rect.h), 1, WHITE_COLOR)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    pg.key.set_repeat(400, 270)

    # Event loop
    while True:
        screen.blit(background, (0, 0))

        if handle_input(player) == -1:
            break
        render_game_object(player)
        # screen.blit(player, player.pos)
        clock.tick(60)
        pg.display.flip()


def create_player(screen):
    player_object = pg.Surface((100, 100), pg.SRCALPHA)
    player_object.fill(PLAYER_COLOR)
    return Player(player_object, screen)


def render_game_object(gameObject):
    gameObject.screen.blit(gameObject.base_surface, gameObject.base_rect)


def handle_input(player):
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player.move((0, -1), 4)
    if keys[pg.K_s]:
        player.move((0, 1), 4)
    if keys[pg.K_a]:
        player.move((-1, 0), 4)
    if keys[pg.K_d]:
        player.move((1, 0), 4)

    events = pg.event.get()
    
    for event in events:
        if event.type == pg.QUIT:
            print('here')
            running = False
            return -1
        if event.type == pg.KEYDOWN:
            print("keydown")
            if event.key == pg.K_j:
                player.rotate(CAMERA_ROTATION_ANGLE)
            if event.key == pg.K_k:
                player.rotate(CAMERA_ROTATION_ANGLE)
    
    pg.event.pump()


if __name__ == '__main__': main()
