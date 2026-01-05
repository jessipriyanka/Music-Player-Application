from player import storage
from player.playlist_manager import PlaylistManager
from player.music_player import MusicPlayer


def test_full_music_player_flow(tmp_path, monkeypatch):
    test_file = tmp_path / "songs.json"
    test_file.write_text("[]")

    monkeypatch.setattr(storage, "DATA_FILE", str(test_file))
    monkeypatch.setattr(storage, "TEMP_FILE", str(tmp_path / "temp.json"))

    manager = PlaylistManager(storage)
    player = MusicPlayer(manager)

    song = manager.add_song("Test Song", "Artist", 120)
    assert song["id"] == 1

    assert player.play(1) == "playing"
    assert player.pause() == "paused"
    assert player.stop() == "stopped"


