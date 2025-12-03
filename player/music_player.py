class MusicPlayer:
    """
    A simple simulated music player (no real audio).
    Tracks play, pause, and stop states.
    """

    def __init__(self, playlist_manager):
        self.manager = playlist_manager
        self.current_song_id = None
        self.state = "stopped"  # playing, paused, stopped
