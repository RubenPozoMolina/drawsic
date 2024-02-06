import time
import wave

import numpy as np
import pyaudio
from scipy.io.wavfile import write


def create_sound():
    p = pyaudio.PyAudio()

    volume = 0.5  # range [0.0, 1.0]
    fs = 44100  # sampling rate, Hz, must be integer
    duration = 1.0  # in seconds, may be float
    f = 440.0  # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples = (np.cos(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)
    # samples_cos = (np.cos(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)
    # samples = np.vstack((samples_sin, samples_cos))
    # per @yahweh comment explicitly convert to bytes sequence
    output_bytes = (volume * samples).tobytes()

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(
        format=pyaudio.paFloat32,
        channels=2,
        rate=fs,
        output=True
    )
    write('downloads/sin.wav', fs, samples)

    # play. May repeat with different volume values (if done interactively)
    start_time = time.time()
    stream.write(output_bytes)
    print("Played sound for {:.2f} seconds".format(time.time() - start_time))

    stream.stop_stream()
    stream.close()

    p.terminate()


if __name__ == "__main__":
    create_sound()
