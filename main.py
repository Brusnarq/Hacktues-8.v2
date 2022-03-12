from ursina import *
from ursina.prefabs.first_person_controller import *
from ursina.shaders import lit_with_shadows_shader
from menu_screen import MenuScreen
from player import Player
from plant import Plant
import random

window.vsync = False
app = Ursina()
player = Player(Vec3(-56, 12, -66))
txt = Text(text=f'{player.position}', x=-.88, y=.5)


def update():
    if player.position.y < 5:
        player.position = Vec3(-56, 12, -66)
    txt.text = f'x: {int(player.position.x)} y: {player.position.y} z: {int(player.position.z)}'


def get_plant_type(plant_model):
    if plant_model == 'assets/plant objects/plant 1/plant_1':
        plant_type = 'toxic_flower'
    elif plant_model == 'assets/plant objects/plant 2/plant_2':
        plant_type = 'purple_flower'
    elif plant_model == 'assets/plant objects/plant 3/plant_3_v2':
        plant_type = 'strawberry_flower'
    elif plant_model == 'assets/trees/tree 1/tree1_v2':
        plant_type = 'tree'
    else:
        plant_type = 'mushroom'

    return plant_type


def generate_plants(num):
    flower_list = ['assets/plant objects/plant 1/plant_1',
                   'assets/plant objects/plant 2/plant_2',
                   'assets/plant objects/plant 3/plant_3_v2']
    tree_list = ['assets/trees/tree 1/tree1_v2',
                 'assets/trees/mushroom/mushroom']

    for i in range(num):
        # generation area 1
        random_model = random.choice(flower_list)
        random_texture = random_model
        area1 = []
        area1.append(Plant(position=Vec3(random.uniform(82, 98), random.uniform(9.2, 9.29), random.uniform(86, 98)),
                           scale=(.3, .3, .3),
                           model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), type=get_plant_type(random_model)))
        # generation area 2
        random_model = random.choice(flower_list)
        random_texture = random_model
        area2 = []
        area2.append(Plant(position=Vec3(random.uniform(61, 72), random.uniform(9.2, 9.29), random.uniform(24, 50)),
                           scale=(.3, .3, .3),
                           model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), type=get_plant_type(random_model)))
        # generation area 3
        random_model = random.choice(flower_list)
        random_texture = random_model
        area3 = []
        area3.append(Plant(position=Vec3(random.uniform(-61, -79), random.uniform(9.08, 9.17), random.uniform(40, 50)),
                           scale=(.3, .3, .3),
                           model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), type=get_plant_type(random_model)))
        # generation area 4
        random_model = random.choice(flower_list)
        random_texture = random_model
        area4 = []
        area4.append(Plant(position=Vec3(random.uniform(-2, -11), random.uniform(9.07, 9.3), random.uniform(46, 60)),
                           scale=(.3, .3, .3),
                           model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), type=get_plant_type(random_model)))

    random_model = random.choice(tree_list)
    random_texture = random_model
    area1.append(Plant(position=Vec3(random.uniform(82, 98), random.uniform(9.2, 9.29), random.uniform(86, 98)),
                       scale=(3, 3, 3),
                       model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), type=get_plant_type(random_model))
                 )
    random_model = random.choice(tree_list)
    random_texture = random_model
    area2.append(Plant(position=Vec3(random.uniform(61, 72), random.uniform(9.2, 9.29), random.uniform(24, 50)),
                       scale=(3, 3, 3),
                       model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), type=get_plant_type(random_model))
                 )
    random_model = random.choice(tree_list)
    random_texture = random_model
    area3.append(Plant(position=Vec3(random.uniform(-61, -79), random.uniform(9.08, 9.17), random.uniform(40, 50)),
                       scale=(3, 3, 3),
                       model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), type=get_plant_type(random_model))
                 )
    random_model = random.choice(tree_list)
    random_texture = random_model
    area4.append(Plant(position=Vec3(random.uniform(-2, -11), random.uniform(9.07, 9.3), random.uniform(46, 60)),
                       scale=(3, 3, 3),
                       model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), type=get_plant_type(random_model))
                 )


def generate_level():
    terrain = Entity(model=Terrain(heightmap='assets/maps/map3.png', skip=36),
                     scale=(200, 60, 200), texture='assets/maps/map3.png', collider='mesh')
    generate_plants(2)
    Sky(texture='assets/textures/sky.png')
    PointLight(position=Vec3(0, 100, 0))
    PointLight(position=Vec3(100, 100, 100))
    PointLight(position=Vec3(0, 100, 100))
    PointLight(position=Vec3(100, 100, 0))
    PointLight(position=Vec3(50, 100, 50))
    PointLight(position=Vec3(0, 100, 50))
    PointLight(position=Vec3(50, 100, 0))
  

def main():
    generate_level()
    app.run()


if __name__ == '__main__':
    main()
