from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector


class character(Widget):
    pass


class MoveableImage(Image):

    def __init__(self, **kwargs):
        super(MoveableImage, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(None, self)
        if not self._keyboard:
            return
        self._keyboard.bind(on_key_down=self.on_keyboard_down)

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'right':
            Clock.schedule_interval(self.droite, 1.0 / 30.0)
            Clock.schedule_once(self.stop_droite, 0.1)
        elif keycode[1] == 'left':
            Clock.schedule_interval(self.gauche, 1.0 / 30.0)
            Clock.schedule_once(self.stop_gauche, 0.1)
        elif keycode[1] == 'up':
            Clock.schedule_interval(self.up, 1.0 / 30.0)
            Clock.schedule_once(self.stop_up, 0.1)
            Clock.schedule_once(self.down1, 0.2)
        else:
            return False
        return True

    def saut(self, keyboard):
        self.y -= 70

    def droite(self, keyboard):
        self.x += 12

    def stop_droite(self, dt):
        Clock.unschedule(self.droite)

    def gauche(self, keyboard):
        self.x -= 12

    def stop_gauche(self, dt):
        Clock.unschedule(self.gauche)

    def up(self, keyboard):
        self.y += 50

    def stop_up(self, dt):
        Clock.unschedule(self.up)

    def down1(self, keyboard):
        Clock.schedule_interval(self.down2, 1.0 / 30.0)
        Clock.schedule_once(self.stop_down, 0.1)

    def down2(self, keyboard):
        self.y -= 50

    def stop_down(self, dt):
        Clock.unschedule(self.down2)


class gameApp(App):
    def build(self):
        wimg = MoveableImage(source='images\cat.png')
        m = character()
        m.add_widget(wimg)
        return m


if __name__ == '__main__':
    gameApp().run()