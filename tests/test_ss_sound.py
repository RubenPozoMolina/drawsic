import pytest

from synesthesong.ss_sound import SSSound, NOTES


@pytest.fixture
def drawsic_sound():
    drawsic_sound_local = SSSound('media/boom.wav')
    yield drawsic_sound_local


class TestDrawsicSound:

    def test_play(self, drawsic_sound):
        for octave in range(-1, 1):
            for note in list(NOTES.keys()):
                drawsic_sound.play(note, octave)

    def test_set_sound(self, drawsic_sound):

        sound_bytes = b'111111111111111111111111111111111111111111'
        drawsic_sound.set_sound(sound_bytes)
