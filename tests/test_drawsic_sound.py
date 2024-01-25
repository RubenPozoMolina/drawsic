import pytest

from src.drawsic_sound import DrawsicSound, NOTES


@pytest.fixture
def drawsic_sound():
    drawsic_sound_local = DrawsicSound('media/boom.wav')
    yield drawsic_sound_local


class TestDrawsicSound:

    def test_play(self, drawsic_sound):
        for octave in range(-2, 3):
            for note in list(NOTES.keys()):
                drawsic_sound.play(octave, note)
