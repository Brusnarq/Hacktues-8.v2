import ursina
from ursina.prefabs.first_person_controller import FirstPersonController

class Player(FirstPersonController):
    def __init__(self, position: ursina.Vec3):
        super().__init__(
            position = position,
            jump_height = 2.5,
            jump_duration = .4,
            origin_y = 1,
            collider = 'box',
            speed = 7
        )

