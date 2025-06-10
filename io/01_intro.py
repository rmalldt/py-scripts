# ------------------ Test data


from ast import mod


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


# ------------------ Reading from file


# ----- Opening a file (NOT RECOMMENDED)
def open_file(filepath: str) -> None:
    # Open a file with filepath, open() returns file object
    # Note:
    # - mode: default "r", no need to specify if reading file
    # - encoding: 'utf-8', always explicitly specify for consistency
    file = open(filepath, mode="r", encoding="utf-8")

    # Iterate the file line by line
    for line in file:
        # trim whitespaces (space, tab and newline) from the line
        # because print also adds its own '\n'
        # Alternative approach: print(line, end="")
        print(line.strip())

    # Never forget to close the file (resource)
    file.close()


# ----- Opening a file using 'with' (RECOMMENDED)
# 'with' will autoclose the file when the block terminates and avoids resource leaks.
#
# Resource leak: is a particular type of resource consumption by a program where
# the program does not release resource it has acquired.
def with_file(filepath: str) -> None:
    # Open the file with filepath and get the file object to use
    with open(filepath, "r") as file:
        for line in file:
            print(line.rstrip())


# read(): Read from the underlying buffer (containing all the characters of the file)
# until we hit EOF and return string
def read_file(filepath: str) -> None:
    with open(filepath, "r") as file:
        text = file.read()
    print(text)  # no need to apply strip() as single string is returned


# readline(): Read until newline or EOF (first line as single string)
def readline_file(filepath: str) -> None:
    with open(filepath, "r") as file:
        # Assignment expression
        while line := file.readline():
            print(line.strip("\n"))  # trim whitespace as each line is returned


# readlines(): Returns a list of lines
def readlines_file(filepath: str) -> None:
    with open(filepath, "r") as file:
        lines = file.readlines()  # a list containing all lines
        print(lines)

    # We can perform post processing on the list
    for line in reversed(lines):
        print(line.strip("\n"))


# ------------------ Writing to file


# Write to a file using print() (NOT RECOMMENDED)
# print() prints the string representation of any object
# It will also include its won default settings such as:
#   - sep: space
#   - end: newline
def print_write_file(destpath):
    # Always explicitly specify the mode and encoding when
    # writing to a file
    with open(destpath, mode="w", encoding="utf-8") as file:
        for song in data:
            print(song, file=file)  # write the output to file


# Write to a file using file.write() (RECOMMENDED)
# write() writes to file in a format we specify when writing.
# i.e if we need separator/newline, we have to format the data.
# It cannot write numerical values by default, they need to be
# converted to string.
def write_file(destpath):
    with open(destpath, mode="w", encoding="utf-8") as file:
        # Note: data is a list of tuple where:
        # - track is int
        # - song is str
        for track, song in data:
            file.write(f"{track}: {song}\n")  # add newline manually


# ------------------ Parsing Text files


def parse_data(sourcefile):
    with open(sourcefile, mode="r", encoding="utf-8") as file:
        for row in file:
            # Trim newline then return list of string separated by 'sep'
            data = row.strip("\n").split(sep="|")
            print(data)


def parse_data_to_dict(sourcefile):
    countries = {}
    with open(sourcefile, mode="r", encoding="utf-8") as file:
        file.readline()  # skip the headings
        for row in file:
            # For each row, read and create a dictionary
            data = row.strip("\n").split(sep="|")
            country, capital, code, code3, dialing, timezone, currency = data
            row_dict = {
                "name": country,
                "capital": capital,
                "country_code": code,
                "cc3": code3,
                "dialing_code": dialing,
                "timezone": timezone,
                "currency": currency,
            }

            # Store the row_dict in the countries dict with country name as key
            countries[country.casefold()] = row_dict
    print(countries)

    while True:
        chosen_country = input("Enter the name of the country: ")
        country_key = chosen_country.casefold()
        if country_key in countries:
            country_data = countries[country_key]
            print(f"The capital of {chosen_country} is {country_data['capital']}")
        elif chosen_country == "quit":
            break


# ------------------ Tests

sourcepath = "../data/texts/poem.txt"
# open_file(sourcepath)
# with_file(sourcepath)
# read_file(sourcepath)
# readline_file(sourcepath)
# readlines_file(sourcepath)

destpath = "../data/texts/albums.txt"
# print_write_file(destpath)
# write_file(destpath)

countryfile = "../data/texts/country_info.txt"
# parse_data(countryfile)
# parse_data_to_dict(countryfile)
