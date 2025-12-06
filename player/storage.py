import json
import os


DATA_FILE = os.path.join("data", "songs.json")
TEMP_FILE = os.path.join("data", "songs_temp.json")


def load_songs() -> list:
    """
    Load the list of songs from songs.json.
    If the file does not exist or is invalid, return an empty list.
    """
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
    """
    Write the songs list to songs.json safely.
    Creates a temporary file and then replaces the old file.
    """
    with open(TEMP_FILE, "w") as temp:
        json.dump(songs, temp, indent=4)

    os.replace(TEMP_FILE, DATA_FILE)


