from ursina import *


class HotBar(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = ( 0.5, .055 ),                                                                                   
            position =  Vec2( 0, -.465 ),                                      
            texture = 'white_cube',                                     
            texture_scale = ( 9, 1 ),                                      
            color = color.red                                         
        )
