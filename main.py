
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivymd.uix.screen import MDScreen
from kivy.uix.floatlayout import FloatLayout

class MainCat(Image):
    def build(self):
        img = Image(source='cat.png', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        return img
class Background(Image):
    def build(self):
        img2 = Image(source='cats.png', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        return img2
class MainApp(App):
    def build(self):
        self.fl = FloatLayout()
        return MainCat
        return Background
        fl.add_widget(MainCat)

        return fl



        #main_layout = BoxLayout()
        #buttons = ["<", ">"]
        # for label in buttons:
        #     button = Button(
        #         text=label,
        #         pos_hint={"center_x": 0.5, "center_y": 0.5},
        #     )
        #     main_layout.add_widget(button)
        #     button.bind(on_press=self.on_button_press)


    # def on_touch_down(self, touch):
    #     ws = touch.x / self.size[0]
    #     hs = touch.y / self.size[1]
    #     aws = 1 - ws
    #     if ws > hs and aws > hs:
    #         cur_dir = (0, -1)  # Вниз
    #     elif ws > hs >= aws:
    #         cur_dir = (1, 0)  # Вправо
    #     elif ws <= hs < aws:
    #         cur_dir = (-1, 0)  # Влево
    #     else:
    #         cur_dir = (0, 1)  # Вверх
    #     self.cur_dir = cur_dir

    # def on_button_press(self,instance):
    #     button_text = instance.text
    #     print(button_text)



if __name__ == "__main__":
    app = MainApp()
    app.run()
