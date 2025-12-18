from player import storage
from player.playlist_manager import PlaylistManager

def test_add_song_blackbox(tmp_path, monkeypatch):
    test_file = tmp_path / "songs.json"
    test_file.write_text("[]")

    monkeypatch.setattr(storage, "DATA_FILE", str(test_file))
    monkeypatch.setattr(storage, "TEMP_FILE", str(tmp_path / "temp.json"))


