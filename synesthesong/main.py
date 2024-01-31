from kivy.app import App
from kivy.uix.widget import Widget


class SynesthesongMain(Widget):
    pass

    def create_sound(self):
        pass


class SynesthesongApp(App):
    def build(self):
        return SynesthesongMain()


if __name__ == '__main__':
    SynesthesongApp().run()
