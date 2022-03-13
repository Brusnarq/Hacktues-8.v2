from numpy import full
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import *
from hotbar import Hotbar
from item_position import item_pos_to_coords
from items_in_slots import SlotPngRender
from grisho import Grisho
from plant_generation import flower_type_to_png, generate_flowers

hot_bar_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
all_2d_flowers = ['assets/textures/toxic_flower.png',
                  'assets/textures/strawberry_flower.png', 'assets/textures/purple_flower.png']
hotbar = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
item_position_in_hotbar = 1
items_needed_to_fill = 0
full = 0
made_change = 0
win = 0


class Fuel(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(.00885, .032),
            position=Vec2(-.739 + items_needed_to_fill * .00885, .3727),
            color=color.lime
        )


class CurrentItemSlot(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(.138, .124),
            position=Vec2(item_pos_to_coords(
                item_position_in_hotbar)+0.004, -.471),
            texture='assets/textures/hotbar_overlay.png',
        )


class Player(Entity):
    def __init__(self, **kwargs):
        self.controller = FirstPersonController(**kwargs)
        super().__init__(parent=self.controller)
        self.cursor = Entity(
            parent=camera.ui,
            model='sphere',
            color=color.white,
            scale=.010,
            rotation_z=45
        )

        self.toxic_flower = Entity(
            parent=self.controller.camera_pivot,
            scale=.31,
            position=Vec3(.90, -.59, 1.5),
            rotation=Vec3(20, 6, 0),
            model='assets/plant objects/plant 1/plant_1',
            texture='assets/plant objects/plant 1/plant_1',
            visible=False
        )

        self.purple_flower = Entity(
            parent=self.controller.camera_pivot,
            scale=.3,
            position=Vec3(1, -.9, 1.5),
            rotation=Vec3(-25, 115, 20),
            model='assets/plant objects/plant 2/plant_2',
            texture='assets/plant objects/plant 2/plant_2',
            visible=False
        )

        self.strawberry_flower = Entity(
            parent=self.controller.camera_pivot,
            scale=.278,
            position=Vec3(.91, -.45, 1.5),
            rotation=Vec3(20, 6, 0),
            model='assets/plant objects/plant 3/plant_3_v2',
            texture='assets/plant objects/plant 3/plant_3_v2',
            visible=False
        )

        self.all_3d_flowers = [self.toxic_flower,
                               self.strawberry_flower, self.purple_flower]
        self.current_3d_item = 0
        self.hotbar_render = Hotbar()
        self.current_item_slot = CurrentItemSlot()
        self.txt = Text(text=f'{self.controller.position}', x=-.88, y=.5)
        self.png_list = []
        self.grisho = Grisho()
        self.flower_list = generate_flowers(5)

    def switch_item(self):
        for i, v in enumerate(self.all_3d_flowers):
            if i == self.current_3d_item:
                v.visible = True
            else:
                v.visible = False

    def input(self, key):
        global item_position_in_hotbar
        global items_needed_to_fill

        if key == 'e':
            for flower in self.flower_list:
                if (flower.position.x - 1.2) <= self.controller.x <= (flower.position.x + 1.2) and (flower.position.z - 1.2) <= self.controller.z <= (flower.position.z + 1.2):
                    self.finding_slot_in_hotbar(flower_type_to_png(flower))
                    self.current_3d_item = all_2d_flowers.index(
                        hotbar[item_position_in_hotbar - 1])
                    if made_change:
                        pickup_sound = Audio('assets/sounds/pickup.wav', volume=0.5)
                        pickup_sound.play()
                        self.flower_list.pop(self.flower_list.index(flower))
                        destroy(flower)
                        self.switch_item()

        if key == 'q':
            if (self.grisho.x - 3) <= self.controller.x <= (self.grisho.x + 3) and (self.grisho.z - 3) <= self.controller.z <= (self.grisho.z + 3):
                drop_sound = Audio('assets/sounds/drop.wav', volume=0.5)
                drop_sound.play()
                for i in range(len(hotbar)):
                    if hotbar[i - 1] != '0':
                        items_needed_to_fill += 1
                        destroy(self.png_list[0])
                        self.png_list.pop(0)
                        hotbar[i - 1] = '0'
                        fill = Fuel()
                destroy(self.hotbar_render)
                destroy(self.current_item_slot)
                self.hotbar_render = Hotbar()
                self.current_item_slot = CurrentItemSlot()
                self.png_list = []
                self.all_3d_flowers[self.current_3d_item].visible = False

        if key in hot_bar_keys:
            item_position_in_hotbar = int(key)

            if hotbar[int(key) - 1] == '0':
                self.strawberry_flower.visible = False
                self.purple_flower.visible = False
                self.toxic_flower.visible = False
            else:
                self.current_3d_item = all_2d_flowers.index(
                    hotbar[int(key) - 1])
                self.switch_item()

            destroy(self.current_item_slot)
            self.current_item_slot = CurrentItemSlot()

        if key == 'scroll down':
            item_position_in_hotbar = (
                item_position_in_hotbar + 1) % (len(hotbar) + 1)

            if item_position_in_hotbar == 0:
                item_position_in_hotbar = 1

            if hotbar[item_position_in_hotbar - 1] == '0':
                self.strawberry_flower.visible = False
                self.purple_flower.visible = False
                self.toxic_flower.visible = False
            else:
                self.current_3d_item = all_2d_flowers.index(
                    hotbar[item_position_in_hotbar - 1])
                self.switch_item()

            destroy(self.current_item_slot)
            self.current_item_slot = CurrentItemSlot()

        if key == 'scroll up':
            item_position_in_hotbar = (
                item_position_in_hotbar - 1) % (len(hotbar) + 1)

            if item_position_in_hotbar == 0:
                item_position_in_hotbar = 9

            if hotbar[item_position_in_hotbar - 1] == '0':
                self.strawberry_flower.visible = False
                self.purple_flower.visible = False
                self.toxic_flower.visible = False
            else:
                self.current_3d_item = all_2d_flowers.index(
                    hotbar[item_position_in_hotbar - 1])
                self.switch_item()

            destroy(self.current_item_slot)
            self.current_item_slot = CurrentItemSlot()

    def update(self):
        global win

        self.controller.camera_pivot.y = 2 - held_keys['left control']
        if self.controller.position.y < 5:
            self.controller.position = Vec3(-56, 12, -66)
        self.txt.text = f'x: {int(self.controller.position.x)} y: {self.controller.position.y} z: {int(self.controller.position.z)}'
        if items_needed_to_fill >= 20:
            win = 1

    def finding_slot_in_hotbar(self, current_2d_flower):
        global item_position_in_hotbar
        global hotbar
        global made_change
        global full

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
            text = Text(text='All of your space is full',
                        position=Vec2(-0.14, -.400), color=color.white)
            destroy(text, delay=2.5)
        elif not made_change:
            text = Text(text='Your hand is full',
                        position=Vec2(-0.1, -.400), color=color.white)
            destroy(text, delay=2.5)

    def hotbar_item(self, current_2d_flower):
        scale_ = None

        if current_2d_flower == 'assets/textures/toxic_flower.png':
            scale_ = (.24, .13)

        if current_2d_flower == 'assets/textures/strawberry_flower.png':
            scale_ = (.142, .072)

        if current_2d_flower == 'assets/textures/purple_flower.png':
            scale_ = (.16, .087)

        self.png = SlotPngRender(
            scale_, current_2d_flower, item_position_in_hotbar)
        self.png_list.append(self.png)
