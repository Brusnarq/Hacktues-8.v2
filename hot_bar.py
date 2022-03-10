from ursina import *


itemposittion = 5


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
    
    if itemposittion >= 5:
        return (itemposittion - 5) * .055
    else:
        return (5 - itemposittion) * -.055


class Item(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = ( .055, .055 ),                                                                                   
            position =  Vec2( ItemPosToHotBar(), -.465 ),
            texture = 'white_cube',
            color = color.green,                                  
        )    
