from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.lang import Builder


class Login(Screen):
    pass


class Gerenciador(ScreenManager):
    pass


class Rabi3(Image):
    vel = 0
    ac = -1000

    def update(self, move, collided):
        # Ground logic
        if self.vel > 0 and collided:
            onGround = False
        elif self.vel <= 0 and collided:
            onGround = True
        else:
            onGround = False
        # move logic
        if self.x < 640:
            self.x += 2
            self.source = 'images/kotk1.png'
        elif self.x > 50:
            self.x -= 2
            self.source = 'images/kotk2.png'
        else:
            print('hi')


class Jellyfish(Image):
    vel = 0
    ac = -1000

    def update(self, jump, move, collided):
        # jump and Ground logic
        if self.vel > 0 and collided:
            onGround = False
        elif self.vel <= 0 and collided:
            onGround = True
        else:
            onGround = False
        if onGround and jump:
            self.vel = 900
            self.y += self.vel * 1 / 30
            onGround = False
        elif onGround:
            self.vel = 0
        else:
            self.vel += self.ac * 1 / 70
            self.y += self.vel * 1 / 70
        # move logic
        if move == 'right':
            self.x += 3
            self.source = 'p6.png'
        elif move == 'left':
            self.x -= 3
            self.source = 'p6l.png'
        else:
            move = ''


class Land(Image):
    px = NumericProperty(0)
    py = NumericProperty(0)


class Gamee(Screen):
    Lands = []
    jump = False
    move = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.drawtela)

    def collision(self):
        px = self.jellyfish.x
        py = self.jellyfish.y
        for block in self.Lands:
            if block.x <= px + self.jellyfish.width / 1.6 < block.x + block.width:
                if block.y <= py < block.y + block.width:
                    return True
        return False

    def update(self, *args):
        collided = self.collision()
        self.jellyfish.update(self.jump, self.move, collided)
        self.rabi3.update(self.move, collided)
        self.jump = False

    def start_game(self):
        if self.jump == False:
            self.jump = True

    def move_left(self):
        if self.move == 'right' or self.move == '':
            self.move = 'left'
        else:
            self.move = ''

    def move_right(self):
        if self.move == 'left' or self.move == '':
            self.move = 'right'
        else:
            self.move = ''

    def drawtela(self, *args):
        self.jellyfish = Jellyfish()
        self.add_widget(self.jellyfish)
        self.rabi3 = Rabi3()
        self.add_widget(self.rabi3)
        for i in range(-1, 20):
            self.Lands.append(Land(px=i))
            self.add_widget(self.Lands[-1])
        for i in range(10, 16):
            self.Lands.append(Land(px=i, py=8))
            self.add_widget(self.Lands[-1])
        for i in range(-1, 5):
            self.Lands.append(Land(px=i, py=16))
            self.add_widget(self.Lands[-1])
        for i in range(5, 11):
            self.Lands.append(Land(px=i, py=35))
            self.add_widget(self.Lands[-1])
        Clock.schedule_interval(self.update, 1 / 60)


class MainApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')


if __name__ == "__main__":
    MainApp().run()
