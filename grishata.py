from ursina import *

class Grisho(Entity):
    def __init__(self):
        super().__init__(
            scale = .5,
            position = ( 3, 1, 3),
            model = 'assets/grishata/grisho_v2',
            texture = 'assets/grishata/grisho_v2',
            collider = 'mesh'
        )
