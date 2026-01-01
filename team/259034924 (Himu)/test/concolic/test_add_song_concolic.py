import pytest
from player.playlist_manager import PlaylistManager
from player import storage


def test_add_song_concolic(tmp_path, monkeypatch):
    """
    Concolic testing for PlaylistManager.add_song()
    """

    # --- Setup isolated JSON storage ---
    test_file = tmp_path / "songs.json"
    test_file.write_text("[]")

    monkeypatch.setattr(storage, "DATA_FILE", str(test_file))
    monkeypatch.setattr(storage, "TEMP_FILE", str(tmp_path / "temp.json"))

    manager = PlaylistManager(storage)

    # =========================================================
    # Concolic Execution 1: Base concrete execution
    # Symbolic: T != "", A != "", 0 < D <= 600
    # =========================================================
    song = manager.add_song("SongA", "ArtistA", 120)
    assert song["id"] == 1

    # =========================================================
    # Concolic Execution 2: Negate (T != "")
    # Symbolic negation: T == ""
    # =========================================================
    with pytest.raises(ValueError):
        manager.add_song("", "ArtistB", 120)

    # =========================================================
    # Concolic Execution 3: Negate (0 < D)
    # Symbolic negation: D <= 0
    # =========================================================
    with pytest.raises(ValueError):
        manager.add_song("SongB", "ArtistB", -10)

    # =========================================================
    # Concolic Execution 4: Negate (not duplicate)
    # Symbolic negation: duplicate song exists
    # =========================================================
    duplicate = manager.add_song("SongA", "ArtistA", 120)
    assert duplicate["status"] == "duplicate"


