from ursina import *
from hot_bar import HotBar, CurrentItem


if __name__ == '__main__':
    app = Ursina()
    hotbar = HotBar()
    item = CurrentItem()
    app.run()
    