import math
import re
from Entity import Rectangle
from Colission import *

class Control():
	def __init__(self, Entity, control_dict):
		self.controlled_entity = Entity
		self.control_dict = control_dict

	def check_control(self, keys_pressed=None, dt=0, entity_list=None):
		#if self.controlled_entity.control_flag:
		for key, action in self.control_dict.items():
			if not isinstance(key, str): 
				if keys_pressed[key]:
					action(self.controlled_entity, dt, entity_list)
		#else:
		#	for key, action in self.control_dict.items():
			elif re.match(r'static_\d+', key) is not None:
				action(self.controlled_entity, dt, entity_list)

	
	@staticmethod
	def move_left(entity, t, entity_list):
		entity.position[0] -= entity.physics['velocity']

	@staticmethod
	def move_right(entity, t, entity_list):
		entity.position[0] += entity.physics['velocity']

	@staticmethod
	def move_up(entity, t, entity_list):
		entity.position[1] -= entity.physics['velocity']

	@staticmethod
	def move_down(entity, t, entity_list):
		entity.position[1] += entity.physics['velocity']
	
	@staticmethod
	def shoot_up(entity, t, entity_list):
		if t%entity.physics['shoot'] == 0:
			bullet = Rectangle(entity.window_container, control_flag=False)
			bullet.define_color((0,255,45))
			bullet.insert_img('./img/bullet.png',10,10)
			bullet.define_geometry([100, 100])
			bullet.define_position([entity.position[0]+17, entity.position[1]-15])
			bullet.define_physics({'velocity':-5, 'object':'ally', 'life':1})
			bullet = CollisionAttributte(bullet)
			
			bullet_spawn = Control(bullet, {
				'static_1': Control.vertical_straight_movement
			})

			bullet.define_control(bullet_spawn)
			entity_list.append(bullet)

	@staticmethod
	def horizontal_sine_movement(entity, t, entity_list):
		entity.position[0] += int(entity.physics['velocity']*math.sin(t/21))

	@staticmethod
	def vertical_straight_movement(entity, t, entity_list):
		entity.position[1] += entity.physics['velocity']

	@staticmethod
	def spawn_down(entity, t, entity_list):
		if t%entity.physics['spawn'] == 0:
			spawn_entity = Rectangle(entity.window_container, control_flag=False)
			spawn_entity.define_color((255,100,0))
			spawn_entity.insert_img('./img/bullet_ovni.png',20,20)

			spawn_entity.define_geometry([10, 10])
			spawn_entity.define_position([entity.position[0], entity.position[1]])
			spawn_entity.define_physics({'velocity':1, 'object':'enemy', 'life':1})
			
			control_spawn = Control(spawn_entity, {
				'static_1': Control.vertical_straight_movement
			})

			spawn_entity.define_control(control_spawn)
			spawn_entity = CollisionAttributte(spawn_entity)
			entity_list.append(spawn_entity)
			# Balitas de la nave
#			print(spawn_entity)
	
	def try_garbage_collector(index, entity_list, display_dimensions):
		entity = entity_list[index]
		x = entity.position[0]
		y = entity.position[1]

		if (x < 0) or (x > display_dimensions[0]) or (y < 0) or (y > display_dimensions[1]):
			del entity_list[index]
