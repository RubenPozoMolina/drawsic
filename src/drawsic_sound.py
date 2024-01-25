from time import sleep

from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty

NOTES = {
    "DO": 1,
    "RE": 9 / 8.,
    "MI": 5 / 4.,
    "FA": 4 / 3.,
    "SOL": 3 / 2.,
    "LA": 5 / 3.,
    "SI": 15 / 8.
}


class DrawsicSound:
    sound = None
    volume = None

    def __init__(self, sound_path=None):
        self.sound = SoundLoader.load(
            sound_path
        )
        self.volume = 1.0

    def play(self, octave, note):
        pitch = NOTES[note]
        self.sound.pitch = pitch * 2 ** octave
        self.sound.volume = self.volume
        self.sound.play()
        sleep(self.sound.length)

    def __del__(self):
        if self.sound:
            self.sound.stop()
            self.sound.unload()
            self.sound = None
