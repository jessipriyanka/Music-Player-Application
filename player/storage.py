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


