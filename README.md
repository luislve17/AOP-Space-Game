# AOP-Space-Game
Juego de naves clásico, implementado aplicando el paradigma Aspect Oriented Programming

## Información
* Asignatura: Tópicos de Software I
* Docente: Ing. Miguel Arrunátegui
* Integrantes:
  * Nelson Sanabio Maldonado
  * Luis Vasquez Espinoza
  
## Contenido
* **AOP_game.mdj:** Archivo de StarUML que documenta la distribución de clases del proyecto
* **Colission.py:** Programa de implementación del decorador destinado a controlar colisiones
* **Control.py:** Programa de definición de controles de entidades del juego
* **Entity.py:** Archivo de estructuración de entidades
* **main.py:** Contenedor del loop principal del juego

## Documentación

> Collision.py
* class AbstractDecorator(Entity): Clase de envoltura destinada a la generación de un aspecto genérico. Funcionará como padre al aplicar decoradores como la colisión.

* class CollisionAttributte(AbstractDecorator): Clase de aspecto _'colisión'_, que permite manipular las _hitbox_ de las entidades, revisando si existen colisión entre estas. La función central a considerar es la siguiente:

```py
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
```



> Control.py

> Entity.py

> main.py
