class MusicPlayer:
    def __init__(self, playlist_manager):
        self.manager = playlist_manager
        self.current_song_id = None
        self.state = "stopped"

    def play(self, song_id: int) -> str:
        ids = [s["id"] for s in self.manager.songs]
        if song_id not in ids:
            return "not_found"

        if self.current_song_id == song_id and self.state == "playing":
            return "already_playing"

        if self.current_song_id == song_id and self.state == "paused":
            self.state = "playing"
            return "resumed"

        self.current_song_id = song_id
        self.state = "playing"
        return "playing"



