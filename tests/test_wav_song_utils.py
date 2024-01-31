import os.path

import pytest

from synesthesong.wav_song_utils import WavSongUtils


@pytest.fixture
def wav_song_utils():
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    wav_song_utils_local = WavSongUtils()
    yield wav_song_utils_local


class TestWavSongUtils:

    def test_get_notes(self, wav_song_utils):
        notes = wav_song_utils.get_notes()
        assert notes

    def test_all(self, wav_song_utils):
        wav_song_utils.main()
        sound_file = 'downloads/sound.wav'
        wav_song_utils.write_sound_file(sound_file)
        file_exists = os.path.exists(sound_file)
        assert file_exists
