from ursina import *


class Plant(Entity):
    def __init__(self, position=Vec3(0, 0, 0), scale=(1, 1, 1), model='cube', texture='white_cube', rotation=(0,0,0)):
        super().__init__(
            model=model,
            texture=texture,
            position=position,
            scale=scale,
            collider='mesh'
        )

