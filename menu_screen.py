import ursina


class Option(ursina.Button):
    def __init__(self, button_text):
        super().__init__(
            color=ursina.color.gray,
            scale=0.25,
            text=button_text,
            text_origin=(0, 0)
        )

    def on_click(self):
        pass

class MenuScreen(ursina.Entity):
    def __init__(self):
        super().__init__(
           parent = ursina.camera.ui 
        )
        global play_button
        play_button = Option('Play')
        
