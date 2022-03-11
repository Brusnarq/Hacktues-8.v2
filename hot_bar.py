from ursina import *


itemposition = 7
hotbar = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]


class HotBar(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = ( .5, .055 ),
            position =  Vec2( 0, -.465 ),
            texture = 'white_cube',
            texture_scale = ( 9, 1 ),
            color = color.red
        )


def ItemPosToHotBar():

    if itemposition >= 5:
        return (itemposition - 5) * .055
    else:
        return (5 - itemposition) * -.055


class CurrentItem(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = ( .055, .055 ),
            position =  Vec2( ItemPosToHotBar(), -.465 ),
            texture = load_texture("assets/Xbox.png"),
            color = color.green,
        )

    hotbar[itemposition - 1] = 1