from player import storage


def test_load_songs_file_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_FILE", str(tmp_path / "missing.json"))
    assert storage.load_songs() == []


