from Entity import *

class AbstractDecorator(Entity):
    def __init__(self, wrapping_entity):
        if wrapping_entity is not None:
            self.__dict__.update(wrapping_entity.__dict__)
		

class CollisionAttributte(AbstractDecorator):
    def __init__(self, wrapping_entity):
        super().__init__(wrapping_entity)

    def is_collided_with(self, entity, entity_list):
        collision_bool = self.border.colliderect(entity.border)
        if collision_bool:
            if self.physics['object'] != entity.physics['object']:
                for e in entity_list:
                    if e is self or e is entity:
                        current_life = e.physics['life']
                        e.physics['life'] = current_life - 1 if current_life >= 0 else 0
                        if e is entity:
                            del e.physics["object"]




