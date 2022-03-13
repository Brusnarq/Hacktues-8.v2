import tkinter
from tkinter import ttk
import PIL.Image
import PIL.ImageTk
from ursina import *
from ursina.prefabs.first_person_controller import *
from player import Player, win
from plant import Plant
from plant_generation import generate_trees
from hotbar import Hotbar
from fuel_tank import FuelTank
import random
# from menu_screen import MenuScreen
# from ursina.shaders import lit_with_shadows_shader

window.vsync = False
app = Ursina()
player = Player(position=Vec3(-56, 12, -66),
                jump_height=2.5,
                jump_duration=.6,
                origin_y=1,
                collider='sphere',
                speed=14,
                gravity=0.5)
fuel = FuelTank()
hotbar = Hotbar()


def generate_level():
    terrain = Entity(model=Terrain(heightmap='assets/maps/map3.png', skip=36),
                     scale=(200, 60, 200), texture='assets/maps/map3.png', collider='mesh')
    generate_trees(2)
    #grigor = Entity(position=Vec3(0, 15, 0), model='assets/grisho/grisho', texture='assets/grisho/grisho', scale=(1, 1, 1), collider='mesh')
    rocket = Entity(model='assets/rocket/rocket_v2', texture='assets/rocket/rocket_v2',
                    position=Vec3(0, 20, 0), collider='mesh', scale=(1, 1, 1))
    Sky(texture='assets/textures/sky.png')
    PointLight(position=Vec3(0, 100, 0))
    PointLight(position=Vec3(100, 100, 100))
    PointLight(position=Vec3(0, 100, 100))
    PointLight(position=Vec3(100, 100, 0))
    PointLight(position=Vec3(50, 100, 50))
    PointLight(position=Vec3(0, 100, 50))
    PointLight(position=Vec3(50, 100, 0))


def main():
    # EditorCamera()
    generate_level()
    app.run()


if __name__ == '__main__':
    launcher = tkinter.Tk()
    launcher.geometry('350x165')
    launcher.wm_title("Last Chance Launcher")
    launcher.iconbitmap('assets/textures/icon.ico')
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="black", background="white")
    logo_img = PIL.Image.open('assets/textures/logo.png')
    logo = PIL.ImageTk.PhotoImage(logo_img)
    logo_label = ttk.Label(image=logo, style='BW.TLabel').pack()
    play = ttk.Button(text='Play', command=main).pack()
    quit = ttk.Button(text='Quit', command=launcher.destroy).pack()
    launcher.mainloop()
