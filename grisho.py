from ursina import *

class Grisho(Entity):
    def __init__(self):
        super().__init__(
            scale = 1,
            position = (12,16.36,-18),
            model = 'assets/grisho/grisho_v2',
            texture = 'assets/grisho/grisho_v2',
            collider = 'mesh'
        )