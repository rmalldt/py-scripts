# ------------------ Reading from file
# ----- Opening a file (NOT RECOMMENDED)
def open_file():
    file = open("../data/poem.txt", mode="r", encoding="utf-8")
    for line in file:
        # print(line, end="")  # disable print '\n' as the file's line already has '\n'
        print(line.strip())  # strip trims the whitespaces (space, tab and newline)
    file.close()


# ----- Opening a file using 'with' (RECOMMENDED)
# 'with' will autoclose the file when block terminates and avoids resource leaks.
#
# Resource leak: is a particular type of resource consumption by a program where
# the program does not release resource it has acquired.
def with_file():
    with open("../data/poem.txt", "r") as file:
        for line in file:
            print(line.rstrip())


# read
# Returns the string containing all the characters of the file
def read_file():
    with open("../data/poem.txt", "r") as file:
        text = file.read()
    print(text)


# readlines
# Returns the list of lines which enables to post processing the text
def readlines_file():
    with open("../data/poem.txt", "r") as file:
        lines = file.readlines()

    # Post processing
    for line in reversed(lines):
        print(line, end="")


# readline
# Returns the first line as single string
def readline_file():
    with open("../data/poem.txt", "r") as file:
        # Assignment expression
        while line := file.readline():
            print(line)


# ------------------ Writing to file
data = [
    (1, "Insomnia"),
    (2, "The Walk"),
    (3, "Letter Experiment"),
    (4, "Jetpacks Was Yes!"),
    (5, "Light"),
    (6, "All New Materials"),
    (7, "Buttersnips"),
    (8, "Icarus Lives!"),
    (9, "Totla Mad"),
    (10, "Ow My Feelings"),
    (11, "Zyglrox"),
    (12, "Racecar"),
]


# print() will print the string representation of any object
# It will also include a defaults such as:
#   - separator: space
#   - end: newline
def print_write_file():
    filename = "../data/albums.txt"
    with open(filename, "w") as file:
        for song in data:
            print(song, file=file)  # write the output to file


# write will only print the data. No separators and newline
# It cannot write numerical values in default text mode
# We must convert number to string in order to use write().
def write_file():
    filename = "../data/albums.txt"
    with open(filename, "w") as file:
        for track, song in data:
            file.write(f"{track}: {song}\n")


# ------------------ Tests


# read_file()
# with_file()
# read_file()
# readlines_file()
# readline_file()

# print_write_file()
write_file()
