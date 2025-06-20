import os


def walk_dir(path: str):
    for path, directories, files in os.walk(path, topdown=True):
        print(f"Path: {path}")
        print(f"Directories: {directories}")
        for f in files:
            print(f"\t{f}")


# ------------------ Test
dir_path = "data/music"
walk_dir(dir_path)
