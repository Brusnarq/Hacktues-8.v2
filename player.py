from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


hot_bar_keys = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
all_2d_flowers = [ 'assets/textures/toxic_flower.png', 'assets/textures/strawberry_flower.png', 'assets/textures/purple_flower.png' ]
hotbar = [ '0', '0', '0', '0', '0', '0', '0', '0', '0' ]
item_position_in_hotbar = 1


def item_pos_to_coords():
    if item_position_in_hotbar > 5:
        return (item_position_in_hotbar - 5) * .056
    else:
        return (5 - item_position_in_hotbar) * -.056


class CurrentItemSlot(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = ( .138, .124 ),
            position =  Vec2( item_pos_to_coords() + 0.004, -.471 ),
            texture = 'assets/textures/hotbar_overlay.png',
        )


class Player(Entity):
    def __init__(self, **kwargs):
        self.controller = FirstPersonController(**kwargs)
        super().__init__(parent = self.controller)
        self.cursor = Entity(
            parent = camera.ui,
            model = 'sphere',
            color = color.white, 
            scale = .010, 
            rotation_z = 45
        ) 
        self.toxic_flower = Entity(
            parent = self.controller.camera_pivot,
            scale = .31,
            position = Vec3( .90, -.59, 1.5 ),
            rotation = Vec3( 20, 6, 0 ),
            model = 'assets/plant objects/plant 1/ plant_1',
            texture = 'assets/plant objects/plant 1/ plant_1',
            visible = False
        )
        self.purple_flower = Entity(
            parent = self.controller.camera_pivot,
            scale = .3,
            position = Vec3( 1, -.9, 1.5 ),
            rotation = Vec3( -25, 115, 20 ),
            model = 'assets/plant objects/plant 2/ plant_2',
            texture = 'assets/plant objects/plant 2/ plant_2',
            visible = False
        )
        self.strawberry_flower = Entity(
            parent = self.controller.camera_pivot,
            scale = .278,
            position = Vec3( .91, -.45, 1.5 ),
            rotation = Vec3( 20, 6, 0 ),
            model = 'assets/plant objects/plant 3/ plant_3_v2',
            texture = 'assets/plant objects/plant 3/ plant_3_v2',
            visible = False
        )
        self.all_3d_flowers = [self.toxic_flower, self.strawberry_flower, self.purple_flower]
        self.current_3d_item = 0
        self.current_item_slot = CurrentItemSlot()


    def switch_item(self):
        for i, v in enumerate(self.all_3d_flowers):
            if i == self.current_3d_item:
                v.visible = True
            else:
                v.visible = False


    def input(self, key):
        global item_position_in_hotbar
        if key == 'e':
            self.find_hotbar_slot(random.choice(all_2d_flowers))
            self.current_3d_item = all_2d_flowers.index(hotbar[item_position_in_hotbar - 1])
            self.switch_item()

        if key in hot_bar_keys:
            item_position_in_hotbar = int(key)

            if hotbar[int(key) - 1] == '0':
                self.strawberry_flower.visible = False
                self.purple_flower.visible = False
                self.toxic_flower.visible = False 
            else:
                self.current_3d_item = all_2d_flowers.index(hotbar[int(key) - 1])
                self.switch_item()

            destroy(self.current_item_slot)
            self.current_item_slot = CurrentItemSlot()

        if key == 'scroll down':
            item_position_in_hotbar = (item_position_in_hotbar + 1) % (len(hotbar) + 1)
            
            if item_position_in_hotbar == 0:
                item_position_in_hotbar = 1
                
            if hotbar[item_position_in_hotbar - 1] == '0':
                self.strawberry_flower.visible = False
                self.purple_flower.visible = False
                self.toxic_flower.visible = False 
            else:
                self.current_3d_item = all_2d_flowers.index(hotbar[item_position_in_hotbar - 1])
                self.switch_item()
            
            destroy(self.current_item_slot)
            self.current_item_slot = CurrentItemSlot()
        
        if key == 'scroll up':
            item_position_in_hotbar = (item_position_in_hotbar - 1) % (len(hotbar) + 1)
            
            if item_position_in_hotbar == 0:
                item_position_in_hotbar = 9
            
            if hotbar[item_position_in_hotbar - 1] == '0':
                self.strawberry_flower.visible = False
                self.purple_flower.visible = False
                self.toxic_flower.visible = False 
            else:
                self.current_3d_item = all_2d_flowers.index(hotbar[item_position_in_hotbar - 1])
                self.switch_item()
            
            destroy(self.current_item_slot)
            self.current_item_slot = CurrentItemSlot()

        
    def find_hotbar_slot(self, current_2d_flower):
        global item_position_in_hotbar
        global hotbar
    
        if hotbar[item_position_in_hotbar - 1] == '0':
            hotbar[item_position_in_hotbar - 1] = current_2d_flower
            self.hotbar_item(current_2d_flower)
            made_change = 1
        else:
            made_change = 0
            
        for i in hotbar:

            if i == '0':
                full = 0
                break
            if i != '0':
                full = 1
        
        if full == 1 and not made_change:        
            text = Text( text = 'All of your space is full', position = Vec2( -0.14, -.400 ), color = color.white )
            destroy(text, delay = 2)
        elif not made_change:
            text = Text( text = 'Your hand is full', position = Vec2( -0.1, -.400 ), color = color.white )
            destroy(text, delay = 2)
        

    def hotbar_item(self, current_2d_flower):
        
        if current_2d_flower == 'assets/textures/toxic_flower.png':
            scale_ = ( .24, .13 )
        
        if current_2d_flower == 'assets/textures/strawberry_flower.png':
            scale_ = ( .142, .072 )
        
        if current_2d_flower == 'assets/textures/purple_flower.png':
            scale_ = ( .16, .087 )

        self.png = Entity(
                parent = camera.ui,
                model = 'quad',
                scale = scale_,
                position =  Vec2(item_pos_to_coords(), -.465),
                texture = current_2d_flower,
            )