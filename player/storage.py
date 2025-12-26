import json
import os

DATA_FILE = os.path.join("data", "songs.json")
TEMP_FILE = os.path.join("data", "songs_temp.json")



def load_songs() -> list:
    """Load songs from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except:
        pass

    return []



def save_songs(songs: list) -> None:
    """Safely write songs to JSON via temp file."""
    with open(TEMP_FILE, "w") as temp:
        json.dump(songs, temp, indent=4)

    os.replace(TEMP_FILE, DATA_FILE)


