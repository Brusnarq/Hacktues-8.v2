import ursina


class Option(ursina.Button):
    def __init__(self, button_text):
        super().__init__(
            color=ursina.color.gray,
            scale=0.25,
            text=button_text,
            text_origin=(-.5, 0)
        )


class MenuScreen(ursina.Entity):
    def __init__(self):
        global play_button
        play_button = Option('Play')
        if  play_button.on_click():
            ursina.destroy(self)
    

