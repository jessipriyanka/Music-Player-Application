from player import storage
from player.playlist_manager import PlaylistManager


def test_add_song_symbolic(tmp_path, monkeypatch):
    test_file = tmp_path / "songs.json"
    test_file.write_text("[]")

    monkeypatch.setattr(storage, "DATA_FILE", str(test_file))
    monkeypatch.setattr(storage, "TEMP_FILE", str(tmp_path / "temp.json"))

    manager = PlaylistManager(storage)

    try:
        manager.add_song("", "Artist", 120)
    except ValueError:
        pass

    try:
        manager.add_song("Title", "", 120)
    except ValueError:
        pass

    try:
        manager.add_song("A", "B", -5)
    except ValueError:
        pass

    song = manager.add_song("A", "B", 200)
    assert song["id"] == 1

