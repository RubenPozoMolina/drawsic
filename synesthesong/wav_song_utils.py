import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.io import wavfile
import mpmath


class WavSongUtils:
    n = 300
    sigma = 0.5
    min_t = 400000
    max_t = 400020
    x = 0
    y = 0
    z = 0
    v = 0
    yf = 0
    zf = 0
    vf = 0
    min = 0
    max = 0
    scale = []

    @staticmethod
    def get_notes():
        scale = []
        for k in range(35, 65):
            note = 440 * 2 ** ((k - 49) / 12)
            if k % 12 != 0 and k % 12 != 2 and k % 12 != 5 and k % 12 != 7 and k % 12 != 10:
                scale.append(note)  # add musical note (skip half tones)
        return scale

    @staticmethod
    def create_data(f, nobs, min_t, max_t, sigma):
        z_real = []
        z_imag = []
        z_modulus = []
        z = None
        incr_t = (max_t - min_t) / nobs
        for t in np.arange(min_t, max_t, incr_t):
            if f == 'Zeta':
                z = mpmath.zeta(complex(sigma, t))
            elif f == 'Eta':
                z = mpmath.altzeta(complex(sigma, t))
            z_real.append(float(z.real))
            z_imag.append(float(z.imag))
            modulus = np.sqrt(z.real * z.real + z.imag * z.imag)
            z_modulus.append(float(modulus))
        return (z_real, z_imag, z_modulus)

    def plot_data(self):
        mpl.rcParams['axes.linewidth'] = 0.3
        fig, ax = plt.subplots()
        ax.tick_params(axis='x', labelsize=7)
        ax.tick_params(axis='y', labelsize=7)
        plt.rcParams['axes.linewidth'] = 0.1
        plt.plot(self.x, self.y, color='red', linewidth=0.3)
        plt.plot(self.x, self.z, color='blue', linewidth=0.3)
        plt.plot(self.x, self.v, color='green', linewidth=0.3)
        plt.legend(['frequency', 'duration', 'volume'], fontsize="7",
                   loc="upper center", ncol=3)
        plt.show()

    @staticmethod
    def get_sine_wave(frequency, duration, sample_rate=22000, amplitude=4096):
        t = np.linspace(0, duration, int(sample_rate * duration))
        wave = amplitude * np.sin(2 * np.pi * frequency * t)
        return wave

    def main(self):
        self.scale = self.get_notes()
        n_notes = len(self.scale)
        (z_real, z_imag, z_modulus) = self.create_data('Eta', self.n, self.min_t, self.max_t, self.sigma)

        size = len(z_real)  # should be identical to nobs
        self.x = np.arange(size)

        # frequency of each note
        self.y = z_real
        self.min = np.min(self.y)
        self.max = np.max(self.y)
        self.yf = 0.999 * n_notes * (self.y - self.min) / (self.max - self.min)

        # duration of each note
        self.z = z_imag
        self.min = np.min(self.z)
        self.max = np.max(self.z)
        self.zf = 0.1 + 0.4 * (self.z - self.min) / (self.max - self.min)

        # volume of each note
        self.v = z_modulus
        self.min = np.min(self.v)
        self.max = np.max(self.v)
        self.vf = 500 + 2000 * (1 - (self.v - self.min) / (self.max - self.min))

    def write_sound_file(self, file_path):
        wave = []
        for t in self.x:  # loop over dataset observations, create one note per observation
            note = int(self.yf[t])
            duration = self.zf[t]
            frequency = self.scale[note]
            # Amplitude 2048
            amplitude = self.vf[t]
            new_wave = self.get_sine_wave(frequency, duration=duration, amplitude=amplitude)
            wave = np.concatenate((wave, new_wave))
        wavfile.write(file_path, rate=44100, data=wave.astype(np.int16))
