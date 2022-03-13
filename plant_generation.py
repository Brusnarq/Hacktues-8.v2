from ursina import *
from plant import Plant
import random


def get_plant_type(plant_model):
    if plant_model == 'assets/plant objects/plant 1/plant_1':
        plant_type = 'toxic_flower'
    elif plant_model == 'assets/plant objects/plant 2/plant_2':
        plant_type = 'purple_flower'
    elif plant_model == 'assets/plant objects/plant 3/plant_3_v2':
        plant_type = 'strawberry_flower'
    elif plant_model == 'assets/trees/tree 1/tree1_v3':
        plant_type = 'tree'
    else:
        plant_type = 'mushroom'

    return plant_type

def flower_type_to_png(plant: Plant):
    if plant.ptype == 'strawberry_flower':
        return 'assets/textures/strawberry_flower.png'
    if plant.ptype == 'toxic_flower':
        return 'assets/textures/toxic_flower.png'
    if plant.ptype == 'purple_flower':
        return 'assets/textures/purple_flower.png'

def generate_flowers(num):
    flower_texture_list = ['assets/plant objects/plant 1/plant_1',
                   'assets/plant objects/plant 2/plant_2',
                   'assets/plant objects/plant 3/plant_3_v2']
    flower_list = []
    for i in range(num):
        # generation area 1
        random_model = random.choice(flower_texture_list)
        random_texture = random_model
        plant = Plant(position=Vec3(random.uniform(82, 97), random.uniform(9.2, 9.29), random.uniform(86, 98)),
                      scale=(.3, .3, .3),
                      model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), ptype=get_plant_type(random_model))
        flower_list.append(plant)

        # generation area 2
        random_model = random.choice(flower_texture_list)
        random_texture = random_model
        plant = Plant(position=Vec3(random.uniform(61, 72), random.uniform(9.2, 9.29), random.uniform(24, 50)),
                      scale=(.3, .3, .3),
                      model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), ptype=get_plant_type(random_model))
        flower_list.append(plant)

        # generation area 3
        random_model = random.choice(flower_texture_list)
        random_texture = random_model
        plant = Plant(position=Vec3(random.uniform(-61, -79), random.uniform(9.08, 9.17), random.uniform(40, 50)),
                      scale=(.3, .3, .3),
                      model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), ptype=get_plant_type(random_model))
        flower_list.append(plant)

        # generation area 4
        random_model = random.choice(flower_texture_list)
        random_texture = random_model
        plant = Plant(position=Vec3(random.uniform(-2, -11), random.uniform(9.07, 9.3), random.uniform(46, 60)),
                      scale=(.3, .3, .3),
                      model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), ptype=get_plant_type(random_model))
        flower_list.append(plant)
    
    return flower_list

def generate_trees(num):
    tree_texture_list = ['assets/trees/tree 1/tree1_v3',
                 'assets/trees/mushroom/mushroom_v3']
    tree_list = []
    for i in range(num):
        random_model = random.choice(tree_texture_list)
        random_texture = random_model
        tree_list.append(Plant(position=Vec3(random.uniform(82, 87), random.uniform(9.2, 9.29), random.uniform(86, 98)),
                                scale=(3, 3, 3),
                                model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), ptype=get_plant_type(random_model))
                          )
        random_model = random.choice(tree_texture_list)
        random_texture = random_model
        tree_list.append(Plant(position=Vec3(random.uniform(61, 72), random.uniform(9.2, 9.29), random.uniform(24, 50)),
                                scale=(3, 3, 3),
                                model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), ptype=get_plant_type(random_model))
                          )
        random_model = random.choice(tree_texture_list)
        random_texture = random_model
        tree_list.append(Plant(position=Vec3(random.uniform(-61, -79), random.uniform(9.08, 9.17), random.uniform(40, 50)),
                                scale=(3, 3, 3),
                                model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), ptype=get_plant_type(random_model))
                          )
        random_model = random.choice(tree_texture_list)
        random_texture = random_model
        tree_list.append(Plant(position=Vec3(random.uniform(-2, -11), random.uniform(9.07, 9.3), random.uniform(46, 60)),
                                scale=(3, 3, 3),
                                model=random_model, texture=random_texture, rotation=Vec3(0, random.uniform(0, 10), 0), ptype=get_plant_type(random_model))
                          )
        