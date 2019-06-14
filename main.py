import pygame

from Entity import Rectangle, Circle
from Control import *
from Colission import *

static_dimensions = (640, 360)

pygame.init()

win = pygame.display.set_mode(static_dimensions)
pygame.display.set_caption('Test')

r = Rectangle(win, control_flag=False)
r.define_color((255,0,0))
r.insert_img('./img/nave_1.png',50,30)
r.define_geometry([30, 20])
r.define_position([10,10])
r.define_physics({'velocity':15, 'spawn':10, 'life':100, 'object':'enemy'})
r = CollisionAttributte(r)

control_rectangle = Control(r, {
	'static_1': Control.horizontal_sine_movement,
	'static_2': Control.spawn_down})

r.define_control(control_rectangle)

c = Circle(win, control_flag=True)
c.define_color((0,255,128))
c.insert_img('./img/nave_2.png',50,30)
c.define_geometry(10, 0)
c.define_position([40, 50])
c.define_physics({'velocity':5, 'shoot':4, 'life':100, 'object': 'ally'})
c = CollisionAttributte(c)

control_circle = Control(c, {
	pygame.K_LEFT:Control.move_left,
	pygame.K_RIGHT:Control.move_right,
	pygame.K_UP:Control.move_up,
	pygame.K_DOWN:Control.move_down,
	pygame.K_SPACE:Control.shoot_up})

c.define_control(control_circle)

global_entity_list = [r, c]
run = True
dt = 0
while run:
    win.fill((0,0,0))
    pygame.time.delay(20)
#    background = pygame.image.load("./img/background.jpg")
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys_pressed = pygame.key.get_pressed()

    for index, entity in enumerate(global_entity_list):
        entity.control.check_control(keys_pressed, dt, global_entity_list)
        entity.draw()

        Control.try_garbage_collector(index, global_entity_list, static_dimensions)
	
    for entity in global_entity_list:
        for other_entity in global_entity_list:
            if other_entity is not entity:
                if isinstance(entity, CollisionAttributte) and isinstance(other_entity, CollisionAttributte):
                    try:
                        entity.is_collided_with(other_entity, global_entity_list)
                    except:
                        pass


    pygame.display.update()
  #  win.blit(background,(0,0))
    dt += 1 
        

pygame.quit()
