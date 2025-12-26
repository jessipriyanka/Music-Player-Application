from player.music_player import MusicPlayer
from player.playlist_manager import PlaylistManager
from player import storage


def test_play_valid_and_invalid_song(tmp_path, monkeypatch):
    test_file = tmp_path / "songs.json"
    test_file.write_text(
        '[{"id":1,"title":"A","artist":"B","duration":100}]'
    )

    monkeypatch.setattr(storage, "DATA_FILE", str(test_file))
    monkeypatch.setattr(storage, "TEMP_FILE", str(tmp_path / "temp.json"))

    manager = PlaylistManager(storage)
    player = MusicPlayer(manager)

    assert player.play(1) == "playing"
    assert player.play(999) == "not_found"



