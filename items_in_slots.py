from ursina import *
from item_position import item_pos_to_coords


class SlotPngRender(Entity):
    def __init__(self, scale_, current_2d_flower, item_position_in_hotbar):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = scale_,
            position =  Vec2( item_pos_to_coords(item_position_in_hotbar), -.465 ),
            texture = current_2d_flower
        )