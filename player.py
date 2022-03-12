from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Player(FirstPersonController):
    def __init__(self, position: Vec3):
        super().__init__(
            position=position,
            jump_height=3,
            jump_duration=.7,
            origin_y=1,
            collider='sphere',
            speed=20,
            gravity=0.3
        )
