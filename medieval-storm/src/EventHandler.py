from Settings import *


thirds_lerp_curve = [34, 56, 71, 81, 87, 91, 94, 96, 97, 99, 100]

KEYBOARD_CHECK_EVENT = pg.event.custom_type()
CAMERA_ROTATION_DELAY_OVER = pg.event.custom_type()
CAMERA_ROTATION_EVENT = pg.event.custom_type()
PLAYER_ATTACK_EVENT = pg.event.custom_type()
DELETE_OBJECT_EVENT = pg.event.custom_type()

can_rotate_camera = True

class EventHandler: 
    def __init__(self, utils):
        self.utils = utils

    # Event transitions (actions that require multiple frames will use thigns on thjis area)
    def lerp_transition(self, event, objects):
        dic = event.__dict__
        index = dic['index']
        curve = dic['curve']

        if index == len(curve):
            return 
        
        if event.type == CAMERA_ROTATION_EVENT:
            # print('cam rotate frame ', index)
            total_degrees = dic['degrees']
            if index != 0:
                rotate_porcentage = curve[index] - curve[index - 1]
            else:
                rotate_porcentage = curve[index]

            frame_degrees_rotate = total_degrees * (rotate_porcentage / 100)

            for o in objects:
                print('degrees to rotate in this frame', frame_degrees_rotate)
                self.rotate_on_pivot(o, PLAYER_POS, round(frame_degrees_rotate, 2))

            index += 1

            new_event = self.create_camera_rotation_event(total_degrees, index)
            pg.event.post(new_event)

    # event creators
    def create_camera_rotation_event(self, degrees, index=0):
        properties = dict()
        properties['degrees'] = degrees
        properties['index'] = index
        properties['curve'] = thirds_lerp_curve
        return pg.event.Event(CAMERA_ROTATION_EVENT, properties)
    

    def create_keyboard_timer(self):
        # this will set a timer to check on keyboard events, so we get every x ms, making it less shaky
        pg.time.set_timer(KEYBOARD_CHECK_EVENT, PLAYER_KEYBOARD_CHECK_DELAY, loops=1)


    def create_player_attack_event(self, attack_hitbox, world_objects):
        dic = dict()
        dic['hitbox'] = attack_hitbox
        dic['world_objects'] = world_objects
        event = pg.event.Event(PLAYER_ATTACK_EVENT, dic)
        pg.event.post(event)


    def handle_player_attack_event(self, player, attack_event):
        attack = attack_event.__dict__['hitbox']
        world_objects = attack_event.__dict__['world_objects']

        player.play_attack_sound()
        objects_collided = attack.base_rect.collideobjectsall(world_objects, key=lambda x: x.base_rect)
        enemies_collided = list(filter(lambda o: o.id != attack.id and o.type=='enemy', objects_collided))
        for enemy in enemies_collided:
            enemy.hp -= player.damage
            enemy.get_hit(player.orientation)
            if enemy.hp <= 0:
                enemy.die()
                world_objects.remove(enemy)
                del enemy
            

    def handle_object_deletion_event(self, delete_event, world_objects):
        to_delete_object = delete_event.__dict__['object']
        world_objects.remove(to_delete_object)
        del to_delete_object


    # event transitions
    def lerp_transition(self, event, objects):
        dic = event.__dict__
        index = dic['index']
        curve = dic['curve']

        if index == len(curve):
            return
        
        if event.type == CAMERA_ROTATION_EVENT:
            # print('cam rotate frame ', index)
            total_degrees = dic['degrees']
            if index != 0:
                rotate_porcentage = curve[index] - curve[index - 1]
            else:
                rotate_porcentage = curve[index]

            frame_degrees_rotate = total_degrees * (rotate_porcentage / 100)

            for o in objects:
                # print('degrees to rotate in this frame', frame_degrees_rotate)
                self.utils.rotate_on_pivot(o, PLAYER_POS, round(frame_degrees_rotate, 2))

            index += 1

            new_event = self.create_camera_rotation_event(total_degrees, index)
            pg.event.post(new_event)


    def handle_input(self, player, world_objects):
        events = pg.event.get()
        keys = pg.key.get_pressed()

        global can_rotate_camera
        
        # player object rotation
        # sum vec stored out for also using in movement

        for event in events:
            # if event.type == KEYBOARD_CHECK:
            #     print(event.__dict__['test'])
            sum_vec = VEC0
            if event.type == pg.QUIT:
                return -1
            
            if event.type == PLAYER_ATTACK_EVENT:
                self.handle_player_attack_event(player, event)

            if event.type == CAMERA_ROTATION_DELAY_OVER:
                can_rotate_camera = True

            if event.type == CAMERA_ROTATION_EVENT:
                self.lerp_transition(event, world_objects)
            
            if event.type == KEYBOARD_CHECK_EVENT:
                pg.time.set_timer(KEYBOARD_CHECK_EVENT, PLAYER_KEYBOARD_CHECK_DELAY, loops=1)

                # print(can_rotate, keys[pg.K_j])

                if can_rotate_camera and keys[pg.K_j]:
                    rotation_event = self.create_camera_rotation_event(-CAMERA_ROTATION_ANGLE)
                    player.rotate(-CAMERA_ROTATION_ANGLE)
                    pg.event.post(rotation_event)
                    can_rotate_camera = False
                    pg.time.set_timer(CAMERA_ROTATION_DELAY_OVER, ROTATION_DELAY, loops=1)

                if can_rotate_camera and keys[pg.K_k]:
                    rotation_event = self.create_camera_rotation_event(CAMERA_ROTATION_ANGLE)
                    player.rotate(CAMERA_ROTATION_ANGLE)
                    pg.event.post(rotation_event)
                    can_rotate_camera = False
                    pg.time.set_timer(CAMERA_ROTATION_DELAY_OVER, ROTATION_DELAY, loops=1)

                if keys[pg.K_w]:
                    sum_vec = self.utils.vector_add(sum_vec, vec2(0, -1))

                if keys[pg.K_a]:
                    sum_vec = self.utils.vector_add(sum_vec, vec2(-1, 0))

                if keys[pg.K_s]:
                    sum_vec = self.utils.vector_add(sum_vec, vec2(0, 1))

                if keys[pg.K_d]:
                    sum_vec = self.utils.vector_add(sum_vec, vec2(1, 0))
                
                if keys[pg.K_SPACE]:
                    attack_hitbox = player.attack()
                    world_objects.append(attack_hitbox)
                    self.create_player_attack_event(attack_hitbox, world_objects)

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
                

    
