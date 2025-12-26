class PlaylistManager:
    def __init__(self, storage_module):
        self.storage = storage_module
        self.songs = self.storage.load_songs()

        if self.songs:
            self.next_id = max(song["id"] for song in self.songs) + 1
        else:
            self.next_id = 1

    def add_song(self, title: str, artist: str, duration: int) -> dict:
        if title.strip() == "":
            raise ValueError("Song title cannot be empty")

        if artist.strip() == "":
            raise ValueError("Artist name cannot be empty")

        if duration <= 0 or duration > 600:
            raise ValueError("Duration must be between 1 and 600 seconds")

        for song in self.songs:
            if song["title"].lower() == title.lower() and song["artist"].lower() == artist.lower():
                return {"status": "duplicate"}

        new_song = {
            "id": self.next_id,
            "title": title,
            "artist": artist,
            "duration": duration
        }

        self.songs.append(new_song)
        self.storage.save_songs(self.songs)
        self.next_id += 1
        return new_song

    def remove_song(self, song_id: int) -> bool:
        for i, song in enumerate(self.songs):
            if song["id"] == song_id:
                self.songs.pop(i)
                self.storage.save_songs(self.songs)
                return True
        return False

    def search(self, query: str) -> list:
        query = query.lower()
        return [song for song in self.songs
                if query in song["title"].lower() or query in song["artist"].lower()]

    def list_songs(self) -> list:
        return sorted(self.songs, key=lambda x: x["id"])

