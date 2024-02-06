import matplotlib.pyplot as plt
from scipy.io import wavfile

DEFAULT_SAMPLE_RATE = 44100


class SSSoundUtils:
    data = None
    sample_rate = None

    def load_sound(self, sound_path):
        self.sample_rate, self.data = wavfile.read(sound_path)

    def set_sound(self, multidimensional_array, sample_rate=DEFAULT_SAMPLE_RATE):
        self.data = multidimensional_array
        self.sample_rate = sample_rate

    def save_sound(self, sound_path):
        wavfile.write(sound_path, self.sample_rate, self.data)

    def plot_sound(self):
        plt.plot(self.data)
        plt.show()
