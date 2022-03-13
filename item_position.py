from ursina import *

def item_pos_to_coords(item_position_in_hotbar):

    if item_position_in_hotbar > 5:
        return (item_position_in_hotbar - 5) * .056
    else:
        return (5 - item_position_in_hotbar) * -.056