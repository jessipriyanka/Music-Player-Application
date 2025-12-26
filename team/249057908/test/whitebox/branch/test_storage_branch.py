from player import storage


def test_load_songs_invalid_json(tmp_path, monkeypatch):
    test_file = tmp_path / "songs.json"
    test_file.write_text("{ invalid json")

    monkeypatch.setattr(storage, "DATA_FILE", str(test_file))
    assert storage.load_songs() == []
