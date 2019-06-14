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

## Estructura
![](https://github.com/luislve17/AOP-Space-Game/blob/master/img/uml_structure.jpeg)


## Documentación

> **Collision.py**
* class AbstractDecorator(Entity): Clase de envoltura destinada a la generación de un aspecto genérico. Funcionará como padre al aplicar decoradores como la colisión.

* class CollisionAttributte(AbstractDecorator): Clase de aspecto _'colisión'_, que permite manipular las _hitbox_ de las entidades, revisando si existen colisión entre estas. La función central a considerar es la siguiente:

```py
def is_collided_with(self, entity, entity_list): # Usando un par de entidades
  collision_bool = self.border.colliderect(entity.border)
        if collision_bool: # Se revisa si ocurrio colision
            if self.physics['object'] != entity.physics['object']: # Y si son entidades enemigas
                for e in entity_list:
                    if e is self or e is entity:
                        current_life = e.physics['life']
                        e.physics['life'] = current_life - 1 if current_life >= 0 else 0 # Se aplica el daño
                        if e is entity:
                            del e.physics["object"] # O se borra de memoria
```



> **Control.py:** Este apartado permite definir la cinemática de las entidades, ya sea aquellas controladas por el usuario, como los de patrones predefinidos. A destacar:

```py
...
  def check_control(self, keys_pressed=None, dt=0, entity_list=None):
		    for key, action in self.control_dict.items(): # Del diccionario de controles definido
			        if not isinstance(key, str): # Si el elemento fue un 'key stroke'
				           if keys_pressed[key]: # Indexar la tecla presionada
					              action(self.controlled_entity, dt, entity_list) # Y aplicar la accion pertinente
			        elif re.match(r'static_\d+', key) is not None: # Si no, se verifica que el elemento se ligo a una accion 'static_\d'
                   action(self.controlled_entity, dt, entity_list) # Y se aplica la accion estatica
...
```

> **Entity.py:** Aquí se definen las características y métodos genéricos de las entidades a utilizar, basándonos en la estructura mostrada en el gráfico UML previo.

> **main.py:** Archivo contenedor del _loop_ de juego principal. Aquí se generan las entidades estática y dinámicamente, en función a los personajes principales (protagonista y enemigo) y los proyectiles y esbirros generados durante la ejecución del juego. Cabe resaltar el uso de un _garbage collector_ para aumentar la eficiencia de ejecución del juego. Se muestra el loop principal a continuación

```py
...
while run:
    win.fill((0,0,0))
    pygame.time.delay(20)
        
    for event in pygame.event.get(): # Manejo de salida de la ventana
        if event.type == pygame.QUIT:
            run = False

    keys_pressed = pygame.key.get_pressed() # Manejo de eventos _key stroke_

    for index, entity in enumerate(global_entity_list): # Iteracion sobre entidades presentes en la lista de entidades
        entity.control.check_control(keys_pressed, dt, global_entity_list)
        entity.draw()

        Control.try_garbage_collector(index, global_entity_list, static_dimensions) # Recoleccion de entidades no presentes en pantalla
	
    for entity in global_entity_list:
        for other_entity in global_entity_list:
            if other_entity is not entity: # Para entidades diferentes
                if isinstance(entity, CollisionAttributte) and isinstance(other_entity, CollisionAttributte):
                    try:
                        entity.is_collided_with(other_entity, global_entity_list) # Control de colision
                    except:
                        pass


    pygame.display.update() # Actualizacion de display

dt += 1 # Control de tiempo
...
```
