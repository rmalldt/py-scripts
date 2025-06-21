import os
import fnmatch


# os.walk is a generator so does not read every file at once into a huge list.
# It only yields the details for a single directoru at a time.
# So, we can process large dataset without running out of memory.
def walk_dir(filepath: str):
    for path, directories, files in os.walk(filepath, topdown=True):
        print(f"Path: {path}")
        print(f"Directories: {directories}")
        for f in files:
            print(f"\t{f}")


def walk_dir_format(filepath: str):
    for path, directories, files in os.walk(filepath, topdown=True):
        if files:
            print(f"Path: {path}")
            first_split = os.path.split(path)
            print(f"First split: {first_split}")
            second_split = os.path.split(first_split[0])
            print(f"Second split: {second_split}")
            for f in files:
                song_details = f[:-5].split(" - ")  # remove extension (last 5 chars)
                print(song_details)
            print("*" * 40)


def find_albums(filepath, name):
    caps_name = name.upper()
    for path, directories, files in os.walk(filepath, topdown=True):
        # for artist in fnmatch.filter(directories, name):
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album  # yield path and album


def list_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):  # get path, not the album name
            yield song


# ------------------ Test


dir_path = "../data/music"

walk_dir(dir_path)
# walk_dir_format(dir_path)

# album_list = find_albums(dir_path, "black*")
# # for a in album_list:
# #     print(a)

# song_list = list_songs(album_list)
# for a in song_list:
#     print(a)
