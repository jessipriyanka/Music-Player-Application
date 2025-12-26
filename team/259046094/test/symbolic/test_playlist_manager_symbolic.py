from player.playlist_manager import PlaylistManager
from player import storage


def test_add_song_symbolic_paths(tmp_path, monkeypatch):
    test_file = tmp_path / "songs.json"
    test_file.write_text("[]")

    monkeypatch.setattr(storage, "DATA_FILE", str(test_file))
    monkeypatch.setattr(storage, "TEMP_FILE", str(tmp_path / "temp.json"))

    manager = PlaylistManager(storage)

    # Path 1: empty title
    try:
        manager.add_song("", "Artist", 120)
    except ValueError:
        pass

    # Path 2: empty artist
    try:
        manager.add_song("Title", "", 120)
    except ValueError:
        pass

    # Path 3: invalid duration
    try:
        manager.add_song("Title", "Artist", -5)
    except ValueError:
        pass

    # Path 4: valid execution
    song = manager.add_song("Title", "Artist", 120)
    assert song["id"] == 1



