class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song.
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds. May be zero.
    """

    def __init__(self, title, artist, duration=0) -> None:
        """Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): An Artist object representing the song's creator.
            duration (int, optional): Initial value for the duration attribute. Defaults to 0.
        """
        self.title = title
        self.artist = artist
        self.duration = duration
