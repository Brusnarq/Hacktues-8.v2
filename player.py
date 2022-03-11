from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


hot_bar_keys = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
all_items = [ 'assets/3d flowers/toxic_flower.png', 'assets/3d flowers/strawberry_flower.png', 'assets/3d flowers/purple_flower.png' ]
hotbar = [ 'assets/3d flowers/strawberry_flower.png', 'assets/3d flowers/toxic_flower.png', 'assets/3d flowers/strawberry_flower.png', 'assets/3d flowers/purple_flower.png', 'assets/3d flowers/toxic_flower.png', 'assets/3d flowers/toxic_flower.png', 'assets/3d flowers/toxic_flower.png', 'assets/3d flowers/strawberry_flower.png', 'assets/3d flowers/toxic_flower.png' ]
itemposition = 0

def ItemPosToHotBar():

    if itemposition >= 5:
        return (itemposition - 5) * .055
    else:
        return (5 - itemposition) * -.055


class CurrentItemSlot(Entity):
    
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = ( .055, .055 ),
            position =  Vec2( ItemPosToHotBar(), -.465 ),
            texture = 'assets/3d flowers/plant_1',
            color = color.rgb(166, 110, 167),
        )

item_pos = CurrentItemSlot()


class Player(Entity):
    
    def __init__(self, **kwargs):
        self.controller = FirstPersonController(**kwargs)
        super().__init__(parent = self.controller)

        self.toxic_flower = Entity(
            parent = self.controller.camera_pivot,
            scale = .3,
            position = Vec3( .88, -.5, 1.5 ),
            rotation = Vec3( 20, 6, 0 ),
            model = 'assets/3d flowers/plant_1',
            texture = ('assets/3d flowers/plant_1'),
            visible = False
        )

        self.purple_flower = Entity(
            parent = self.controller.camera_pivot,
            scale = .3,
            position = Vec3( .87, -.45, 1.5 ),
            rotation = Vec3( 20, -3, 0 ),
            model = 'assets/3d flowers/plant_2',
            texture = ('assets/3d flowers/plant_2'),
            visible = False
        )

        self.strawberry_flower = Entity(
            parent = self.controller.camera_pivot,
            scale = .28,
            position = Vec3( .87, -.45, 1.5 ),
            rotation = Vec3( 20, 6, 0 ),
            model = 'assets/3d flowers/plant_3',
            texture = ('assets/3d flowers/plant_3'),
            visible = False
        )

        self.items = [self.toxic_flower, self.strawberry_flower, self.purple_flower]
        self.current_item = 0

    def SwitchItems(self):
       
        for i, v in enumerate(self.items):
            if i == self.current_item:
                v.visible = True
            else:
                v.visible = False


    def input(self, key):
        global itemposition
        global item_pos

        if key in hot_bar_keys:
            itemposition = int(key)
            self.current_item = all_items.index(hotbar[int(key) - 1])
            destroy(item_pos)
            item_pos = CurrentItemSlot()
            self.SwitchItems()

        if key == 'scroll up':
            itemposition = (itemposition + 1) % (len(hotbar) + 1)
            if itemposition == 0:
                itemposition = 1
            self.current_item = all_items.index(hotbar[itemposition - 1])
            destroy(item_pos)
            item_pos = CurrentItemSlot()
            self.SwitchItems()
        
        if key == 'scroll down':
            itemposition = (itemposition - 1) % (len(hotbar) + 1)
            if itemposition == 0:
                itemposition = 9
            self.current_item = all_items.index(hotbar[itemposition - 1])
            destroy(item_pos)
            item_pos = CurrentItemSlot()
            self.SwitchItems()


    def update(self):
        self.controller.camera_pivot.y = 2 - held_keys['left control']
