from kivy.app import App
from kivy.uix.widget import Widget


class DrawsicMain(Widget):
    pass

    def create_sound(self):
        pass


class DrawsicApp(App):
    def build(self):
        return DrawsicMain()


if __name__ == '__main__':
    DrawsicApp().run()
