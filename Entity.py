import pygame

class Entity:
	def __init__(self, window_ref, control_flag=False):
		self.control_flag = control_flag # Indica si el jugador tiene control sobre esta entidad
		self.available_shapes = ['circle', 'rect']
		self.window_container = window_ref
		self.attached_image = None
		self.font = pygame.font.Font(None,20)
		self.border = None
	
	def define_physics(self, physics):
		self.physics = physics
	
	def define_color(self, rgb_tuple):
		if len(rgb_tuple) != 3:

			raise ValueError("Bad rgb_tuple argument: {}. Shape needed: 3".format(len(rgb_tuple)))
	
		self.color = rgb_tuple
	
	def define_position(self, position_list = [0,0]):
		if len(position_list) != 2:
			raise ValueError("Bad position_list argument: {}. Shape needed: 2".format(len(position_list)))
		self.position = position_list

	def define_control(self, control_obj):
		self.control = control_obj

	def draw(self):
		if self.attached_image is None:
			if isinstance(self, Rectangle):
				self.border = pygame.draw.rect(self.window_container, self.color, self.position+self.geometry)

			if isinstance(self, Circle):
				self.border = pygame.draw.circle(self.window_container, self.color, self.position, self.radius, self.tickness)
		else:
			self.window_container.blit(self.attached_image, self.position)
			try:
				self.txt = self.font.render("Vida : {}%".format(self.physics["life"]),0,self.color)
				self.window_container.blit(self.txt,(self.position[0],self.position[1]+35))
			except:
				pass

		if self.attached_image is not None:
			self.border = pygame.draw.rect(self.window_container, (0,0,0,0), self.position + self.attached_image.get_rect()[2:], 1)

	def insert_img(self, image_path,sx,sy):
		self.attached_image = pygame.image.load(image_path)
		self.attached_image = pygame.transform.scale(self.attached_image,(sx,sy))


class Rectangle(Entity):
	def __init__(self, window_ref, control_flag=False):
		super().__init__(window_ref, control_flag)

	def define_geometry(self, dimensions_list):
		if len(dimensions_list) != 2:
			raise ValueError("Bad dimensions_list argument: {}. Shape needed: 2".format(len(dimensions_list)))

		self.geometry = dimensions_list
	
	"""
	def draw(self):
		print("???????????????????")
		if self.attached_image is None:
			self.border = pygame.draw.rect(self.window_container, self.color, self.position+self.geometry)
		else:
			self.window_container.blit(self.attached_image, self.position)
			self.txt = self.font.render("Vida : {}%".format(self.physics["life"]),0,(255,0,0))
			self.window_container.blit(self.txt,(0,0))
	"""

	def print_info(self):
		print({'control':self.control, 'color': self.color, 'geometry':self.geometry, 'position':self.position})


class Circle(Entity):
	def __init__(self, window_ref, control_flag=False):
		super().__init__(window_ref, control_flag)

	def define_geometry(self, radius, tickness=1):
		self.radius = radius
		self.tickness = tickness
	
	"""
	def draw(self):
		print("???????????????????")
		if self.attached_image is None:
			self.border = pygame.draw.circle(self.window_container, self.color, self.position, self.radius, self.tickness)
		else:
			self.window_container.blit(self.attached_image, self.position)
			self.txt = self.font.render("Vida : {}%".format(self.physics["life"]),0,(0, 255, 0))
			self.window_container.blit(self.txt,(0,345))
	"""

	def print_info(self):
		print({'control':self.control, 'color': self.color, 'radius':self.radius, 'position':self.position, 'tickness': self.tickness})


if __name__ == "__main__":
	r = Rectangle(None, True)
	r.define_color((255,0,0))
	r.define_geometry((30, 20))
	r.define_position((20,20))
	r.print_info()
