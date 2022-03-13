from ursina import *


class FuelTank(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = ( 0.3, 0.1 ),
            position = Vec2( -.7, .4 ),
            texture = 'assets/Fuel_tank.png',
        )
