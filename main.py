from ursina import *
from hot_bar import HotBar
from player import Player


def input(key):
    if key == 'escape':
        quit()


if __name__ == '__main__':
    app = Ursina()

    ground = Entity(
        model = 'plane',
        scale = 20,
        texture = 'white_cube',
        texture_scale = ( 20, 20, 20 ),
        collider = 'mesh'
    )

    hotbar = HotBar()
    player = Player(position = ( 0, 10, 0 ))

    app.run()
    