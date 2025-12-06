class MusicPlayer:
    """
    A simple simulated music player (no real audio).
    Tracks play, pause, and stop states.
    """

    def __init__(self, playlist_manager):
        self.manager = playlist_manager
        self.current_song_id = None
        self.state = "stopped"  # playing, paused, stopped


    def play(self, song_id: int) -> str:
        """
        Simulate playing a song with several branches:
        - invalid song id
        - already playing same song
        - paused same song -> resume
        - play new song
        """
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


