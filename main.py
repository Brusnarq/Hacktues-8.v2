import ursina
from menu_screen import MenuScreen
from player import Player

app = ursina.Ursina()

def update():
    if ursina.held_keys['escape']:
        menu = MenuScreen()

def main():
    player = Player(ursina.Vec3(0,1,0))
    app.run()


if __name__ == '__main__':
    main()
