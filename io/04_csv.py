from ast import mod
import csv

# ------------------ Read CSV


def read_csv():
    filepath = "../data/cereal_grains.csv"
    with open(filepath, encoding="utf-8", newline="") as file:
        # quoting tells csv that non-numeric values are quoted
        # so the reader properly formats string and numeric values
        reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            print(row)


def read_csv_different_separator():
    filepath = "../data/country_info.txt"
    with open(filepath, encoding="utf-8", newline="") as file:
        # delimiter tells csv that the values are separated by
        # the specified delimiter so the reader formats the file properly
        reader = csv.reader(file, delimiter="|")
        for row in reader:
            print(row)


def read_csv_different_separator_automated():
    filepath = "../data/country_info.txt"
    with open(filepath, encoding="utf-8", newline="") as file:
        # Sniff csv format and return dialect
        # This enables to auto detect what delimiter has been used
        sample = ""
        for line in range(3):
            sample += file.readline()
        file_dialect = csv.Sniffer().sniff(sample)

        # Point to start of the file as 3 lines have already been read before
        file.seek(0)
        reader = csv.reader(file, dialect=file_dialect)
        for row in reader:
            print(row)


def get_csv_dialect_attributes():
    filepath = "../data/country_info.txt"
    with open(filepath, encoding="utf-8", newline="") as file:
        sample = ""
        for line in range(3):
            sample += file.readline()
        file_dialect = csv.Sniffer().sniff(sample)

    attributes = [
        "delimiter",
        "doublequote",
        "escapechar",
        "lineterminator",
        "quotechar",
        "quoting",
        "skipinitialspace",
    ]

    for attribute in attributes:
        print(f"{attribute}: {repr(getattr(file_dialect, attribute))}")


def read_csv_unformatted():
    filepath = "../data/OlympicMedals_2020.csv"
    with open(filepath, encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    # ----- csv.DictReader
    # Read CSV file as dictionary


def read_csv_dict():
    filepath = "../data/my_cereals.csv"

    with open(filepath, encoding="utf-8", newline="") as file:
        # Configure the heading to be lowercase for consistency
        # headings = file.readline().strip("\r\n").split(",")
        # for index, heading in enumerate(headings):
        #     headings[index] = heading.casefold()

        reader = csv.DictReader(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            print(row)


# ------------------ Write CSV

cereals = [
    ["Barley", 556, 1.7, 32.9, 10.1, 13.8],
    ["Durum", 339, 5, 27.4, 4.09, 9.7],
    ["Fonio", 240, 1, 4, 1.7, 0.05],
    ["Maize", 442, 7.4, 37.45, 6.15, 11.03],
    ["Millet", 484, 2, 37.9, 13.4, 9.15],
    ["Oats", 231, 9.2, 35.1, 10.3, 3.73],
    ["Rice (Brown)", 346, 2.8, 38.1, 9.9, 0.8],
    ["Rice, (White)", 345, 3.6, 37.6, 5.4, 0.1],
    ["Rye", 422, 2, 31.4, 18.2, 21.2],
    ["Sorghum", 316, 3, 37.8, 9.92, 9.15],
    ["Triticale", 338, 1.81, 36.6, 19, 0.9],
    ["Wheat", 407, 1.2, 27.8, 12.9, 13.8],
]

column_headings = ["Cereal", "Calories", "Fat", "Protein", "Fibre", "Vitamin E"]
output_filename = "../data/my_cereals.csv"


def write_csv():
    with open(output_filename, mode="w", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(column_headings)
        writer.writerows(cereals)


# ------------------ Tests


# read_csv()
# read_csv_different_separator()
# read_csv_different_separator_automated()
# get_csv_dialect_attributes()
read_csv_dict()


# write_csv()
