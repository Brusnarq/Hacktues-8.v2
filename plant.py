from ursina import *


class Plant(Entity):
    def __init__(self, position=Vec3(0, 0, 0), scale=(1, 1, 1), model='cube', texture='white_cube', rotation=(0,0,0), ptype='tree'): # possible types  are:
        self.ptype=ptype
        super().__init__(                                                                                                           # tree, mushroom, purple_flower, 
            model=model,                                                                                                            # strawberry_flower, toxic_flower
            texture=texture,
            position=position,
            scale=scale,
            rotation=rotation,
            collider='mesh',
        )