class Song:
    """
    Class to represent a song.

    Attributes:
        title (str): The title of the song.
        artist (str): The name of the song creator.
        duration (int): The duration of the song in seconds. May be zero.
    """

    def __init__(self, title: str, artist: str, duration: int = 0) -> None:
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    # In case, the name property is required by other methods processing this object.
    name = property(get_title)


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

    def add_song(self, album_name, year, title):
        """
        Add new songs to the collection of album. This method adds the song to
        an album in the collection. A new album is created in the collection if
        it doesn't already exist.

        Args:
            album_name (str): The name of the album.
            year (int): The year of the album was produced.
            title (str): The title of the song.
        """
        new_album = find_object(album_name, self.album)
        if new_album is None:
            print(f"{album_name} not found!")
            new_album = Album(album_name, year, self.name)
            self.add_album(new_album)
        else:
            print(f"Album found: {album_name}")

        new_album.add_song(title)


class Album:
    """
    Class to represent an Album, using its track list.

    Attributes:
        name (str): The name of the album.
        year (int): The year album was released.
        artist (str): The name of the artist responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artist".
        tracks (List[Song]): A list of the songs on the album.
    """

    def __init__(self, name: str, year: int, artist: str | None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song_name: str, position=None):
        """
        Adds a song to the track list.

        Args:
            song (str): The title of a song to add.
            position (int, optional): If specified, the song will be added to that position
            in the track list - inserting it between other songs if necessary otherwise the
            song will be added to the end of the list. Defaults to None.
        """
        new_song = find_object(song_name, self.tracks)
        if new_song is None:
            new_song = Song(song_name, self.artist)
            if position is None:
                self.tracks.append(new_song)
            else:
                self.tracks.insert(position, new_song)


def find_object(field, object_list):
    """
    Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists,
    return it if so
    """
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open("data/albums.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            artist_field, album_field, year_field, song_field = tuple(
                line.strip("\n").split("\t")
            )
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


# ------------------ Test


if __name__ == "__main__":
    # help(Song)
    # help(Song.__init__)
    # print(Song.__doc__)
    # print(Song.__init__.__doc__)

    data = load_data()
    print(f"There are {len(data)} data")
