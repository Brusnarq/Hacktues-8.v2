from ursina import *
from fuel_tank import FuelTank
from player import Player, win


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
        collider = 'mesh',
    )

    player = Player(position = ( 0, 20, 0 ))
    fuel = FuelTank()
    # if win == 1:

    app.run()
    