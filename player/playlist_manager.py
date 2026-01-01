class PlaylistManager:
    def __init__(self, storage_module):
        self.storage = storage_module
        self.songs = self.storage.load_songs()

        if self.songs:
            self.next_id = max(song["id"] for song in self.songs) + 1
        else:
            self.next_id = 1

    def add_song(self, title: str, artist: str, duration: int) -> dict:
        # 1. Empty title check
        if title.strip() == "":
            raise ValueError("Song title cannot be empty")

        # 2. Empty artist check
        if artist.strip() == "":
            raise ValueError("Artist name cannot be empty")

        # 3. Duration lower bound
        if duration <= 0:
            raise ValueError("Duration must be greater than 0 seconds")

        # 4. Duration upper bound
        if duration > 600:
            raise ValueError("Duration must be less than or equal to 600 seconds")

        # 5. Title length check
        if len(title) > 100:
            raise ValueError("Song title too long")

        # 6. Artist length check
        if len(artist) > 100:
            raise ValueError("Artist name too long")

        # 7. Forbidden character check
        forbidden_chars = ["@", "#", "$", "%"]
        for ch in forbidden_chars:
            if ch in title or ch in artist:
                raise ValueError("Invalid character in title or artist")

        # 8. Duplicate song check
        for song in self.songs:
            if song["title"].lower() == title.lower() and song["artist"].lower() == artist.lower():
                return {"status": "duplicate"}

        # 9. Playlist size limit check
        if len(self.songs) >= 1000:
            raise ValueError("Playlist size limit reached")

        new_song = {
            "id": self.next_id,
            "title": title,
            "artist": artist,
            "duration": duration
        }

        # 10. Safe save with exception handling
        try:
            self.songs.append(new_song)
            self.storage.save_songs(self.songs)
        except Exception:
            raise IOError("Failed to save song")

        # 11. ID increment
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

