import random
import numpy
import numpy as np
import pytest

from synesthesong.ss_sound import SSSound
from synesthesong.ss_sound_utils import SSSoundUtils


@pytest.fixture
def ss_sound_utils():
    ss_sound_utils_local = SSSoundUtils()
    yield ss_sound_utils_local


class TestSSSoundUtils:

    def test_load_sound(self, ss_sound_utils):
        ss_sound_utils.load_sound('media/boom.wav')
        assert isinstance(ss_sound_utils.data, numpy.ndarray)

    def test_set_sound(self, ss_sound_utils):
        test_file = 'downloads/test.wav'
        incremental_array = []
        for item in range(0, 16000):
            incremental_array.append(
                [random.randint(3000, 4000), random.randint(3500, 4500)]
            )

        data = np.ndarray(
            shape=(len(incremental_array), 2),
            dtype=numpy.int16,
            buffer=np.array([incremental_array])
        )
        ss_sound_utils.set_sound(data)
        ss_sound_utils.save_sound(test_file)
        sound = SSSound(test_file)
        sound.play()
