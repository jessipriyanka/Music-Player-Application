class PlaylistManager:
    """
    This class manages songs in memory.
    It loads songs from storage and provides add, remove, search, and list features.
    """

    def __init__(self, storage_module):
        self.storage = storage_module
        self.songs = self.storage.load_songs()

        if self.songs:
            self.next_id = max(song["id"] for song in self.songs) + 1
        else:
            self.next_id = 1


