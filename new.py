import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock

class Box(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = None, None
        self.width = 50
        self.height = 50

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.remove_widget(self)
            return True

class TenekeKutuKulesiApp(App):
    def build(self):
        # set the window size
        Window.size = (300, 600)
        self.box_size = 50
        self.box_speed = 1
        self.boxes = []
        self.score = 0
        self.score_label = Button(text=f"Score: {self.score}", pos=(0, Window.height - 50), size_hint=(None, None), width=100, height=50)

        # add the score label to the screen
        self.root = Widget()
        self.root.add_widget(self.score_label)

        # start adding boxes
        self.add_boxes()

        # set up a game loop to update the boxes
        self.game_loop = Clock.schedule_interval(self.update, 1/60)

        return self.root

    def add_boxes(self):
        for i in range(20):
            box = Box(pos=(random.randint(0, Window.width - self.box_size), Window.height + random.randint(0, 500)), size_hint=(None, None))
            self.root.add_widget(box)
            self.boxes.append(box)

    def update(self, dt):
        for box in self.boxes:
            box.pos = (box.pos[0], box.pos[1] - self.box_speed)
            if box.pos[1] < -50:
                box.pos = (random.randint(0, Window.width - self.box_size), Window.height + random.randint(0, 500))
                self.score += 1
                self.score_label.text = f"Score: {self.score}"

    def on_stop(self):
        # stop the game loop when the app closes
        self.game_loop.cancel()

if __name__ == "__main__":
    TenekeKutuKulesiApp().run()
