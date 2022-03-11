import ursina
from menu_screen import MenuScreen
from player import Player
from ursina.prefabs.first_person_controller import *

app = ursina.Ursina()


def update():
    pass


def main():
    # EditorCamera()
    terrain = ursina.Entity(model=ursina.Terrain(heightmap='assets/maps/map3.png', skip=36),
                            scale=(200, 60, 200), texture='assets/maps/map3.png', collider='mesh')
    #Sky()
    Sky(texture='assets/textures/sky.png')

    player = Player(ursina.Vec3(0, 70, 0))
    app.run()


if __name__ == '__main__':
    main()
