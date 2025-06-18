class Artist:
    """
    Class to store Artist details.

    Attributes:
        name (str): The name of the artist.

    Methods:
        add_album: Use to add a new album to the artist's albums list.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.album = []

    def add_album(self, album):
        """
        Add a new album to the list.

        Args:
            album (Album): Album object to add to the list. If the album
            is already present, it will not be added again.
        """
        self.album.append(album)


class Song:
    """
    Class to represent a song.

    Attributes:
        title (str): The title of the song.
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds. May be zero.
    """

    def __init__(self, title: str, artist: Artist, duration: int = 0) -> None:
        """
        Song init method.

        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): An Artist object representing the song's creator.
            duration (int, optional): Initial value for the duration attribute. Defaults to 0.
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """
    Class to represent an Album, using its track list.

    Attributes:
        name (str): The name of the album.
        year (int): The year album was released.
        artist (Artist): The artist responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artist".
        tracks (List[Song]): A list of the songs on the album.
    """

    def __init__(self, name: str, year: int, artist: Artist | None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song: Song, position: int | None):
        """
        Adds a song to the track list.

        Args:
            song (Song): A song to add.
            position (int, optional): If specified, the song will be added to that position
            in the track list - inserting it between other songs if necessary otherwise the
            song will be added to the end of the list. Defaults to None.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


def load_data():
    # new_artist = None
    # new_album = None
    # artist_list = []

    with open("data/albums.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            artist_field, album_field, year_field, song_field = tuple(
                line.strip("\n").split("\t")
            )
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            new_artist = Artist(artist_field)


# ------------------ Test


if __name__ == "__main__":
    # help(Song)
    # help(Song.__init__)
    # print(Song.__doc__)
    # print(Song.__init__.__doc__)

    load_data()
