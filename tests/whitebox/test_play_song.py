from player import storage
from player.playlist_manager import PlaylistManager
from player.music_player import MusicPlayer


def test_play_song_whitebox(tmp_path, monkeypatch):
    test_file = tmp_path / "songs.json"
    test_file.write_text('[{"id":1,"title":"A","artist":"B","duration":120}]')

    monkeypatch.setattr(storage, "DATA_FILE", str(test_file))
    monkeypatch.setattr(storage, "TEMP_FILE", str(tmp_path / "temp.json"))

    manager = PlaylistManager(storage)
    player = MusicPlayer(manager)

    assert player.play(1) == "playing"
    assert player.play(1) == "already_playing"
    assert player.pause() == "paused"
    assert player.play(1) == "resumed"






