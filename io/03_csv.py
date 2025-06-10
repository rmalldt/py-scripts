import csv


# ------------------ Test data

cereal_headings = ["Cereal", "Calories", "Fat", "Protein", "Fibre", "Vitamin E"]
cereals = [
    ["Barley", 556, 1.7, 32.9, 10.1, 13.8],
    ["Durum", 339, 5, 27.4, 4.09, 9.7],
    ["Fonio", 240, 1, 4, 1.7, 0.05],
    ["Maize", 442, 7.4, 37.45, 6.15, 11.03],
    ["Millet", 484, 2, 37.9, 13.4, 9.15],
    ["Oats", 231, 9.2, 35.1, 10.3, 3.73],
    ["Rice (Brown)", 346, 2.8, 38.1, 9.9, 0.8],
    ["Rice (White)", 345, 3.6, 37.6, 5.4, 0.1],
    ["Rye", 422, 2, 31.4, 18.2, 21.2],
    ["Sorghum", 316, 3, 37.8, 9.92, 9.15],
    ["Triticale", 338, 1.81, 36.6, 19, 0.9],
    ["Wheat", 407, 1.2, 27.8, 12.9, 13.8],
]

country_headings = ["country", "gold", "silver", "bronze", "rank"]
medal_table = [
    {"country": "United States", "gold": 39, "silver": 41, "bronze": 33, "rank": 1},
    {"country": "China", "gold": 38, "silver": 32, "bronze": 18, "rank": 2},
    {"country": "Japan", "gold": 27, "silver": 14, "bronze": 17, "rank": 3},
    {"country": "Great Britain", "gold": 22, "silver": 21, "bronze": 22, "rank": 4},
    {"country": "ROC", "gold": 20, "silver": 28, "bronze": 23, "rank": 5},
    {"country": "Australia", "gold": 17, "silver": 7, "bronze": 22, "rank": 6},
]


# ------------------ Read CSV


def read_csv(filepath):
    # Note: newline="" (empty string) is required for csv module to function
    with open(filepath, encoding="utf-8", newline="") as file:
        # 'quoting' tells csv to quote non-numeric values which results in:
        # non-numeric:  quoted      -> str
        # numeric:      unquoted    -> float
        reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)

        # Each row is a list of separated values from CSV
        for row in reader:
            print(row)


def read_csv_different_separator():
    filepath = "../data/texts/country_info.txt"
    with open(filepath, encoding="utf-8", newline="") as file:
        # 'delimiter' tells csv to that the source file uses specified delimeter
        reader = csv.reader(file, delimiter="|")
        for row in reader:
            print(row)


def read_csv_different_separator_automated():
    filepath = "../data/texts/country_info.txt"
    with open(filepath, encoding="utf-8", newline="") as file:
        # Sniff csv format and return dialect
        # This enables to auto-detect what delimiter has been used
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
    filepath = "../data/texts/country_info.txt"
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


# ------------------ Read CSV using DictReader


# Read CSV file as dictionary
def read_csv_dict(filepath):
    cereals = {}
    with open(filepath, encoding="utf-8", newline="") as file:
        # Configure the headings to be lowercase for consistency e.g., for accessing dictionary items
        # readline returns string but split returns list of string separated by delimiter
        headings = file.readline().strip("\r\n").split(",")
        for index, heading in enumerate(headings):
            # Strip the double quotes around the string data in source csv file.
            # It is done when string data in CSV are stored with double quotes.
            headings[index] = heading.strip('"').casefold()

        # Read data from CSV but provide heading as fieldnames
        # DictReader processes the first line as the headings
        # which we've already processed manually above.
        reader = csv.DictReader(file, fieldnames=headings)

        # Each row of DictReader is a dictionary type
        for row in reader:
            # Store each row dict in the cereals dict with cereal name as key
            cereals[row["cereal"].casefold()] = row

    print(cereals)


# ------------------ Write CSV


def write_csv(filepath):
    with open(filepath, mode="w", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(cereal_headings)
        writer.writerows(cereals)


# Return the key which will be used to compare the sorting order
def sort_key(d: dict) -> str:
    return d["country"]


def write_csv_dictwriter():
    filepath = "../data/csvs/olympic_medals_2020_test.csv"
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=country_headings)
        writer.writeheader()
        writer.writerows(sorted(medal_table, key=sort_key))


# Read the CSV file, transform its data and create Python file with
# the transformed dataset simultaneously
def read_csv_write_python():
    # These headings correspond to the headings from the csv source file
    headings = ["Country", "Gold", "Silver", "Bronze", "Rank"]
    sourcefilepath = "../data/csvs/olympic_medals_2020.csv"
    destfilepath = "../data/medals_dict.py"

    with open(sourcefilepath, encoding="utf-8", newline="") as sourcefile, open(
        destfilepath, mode="w", encoding="utf-8"
    ) as destfile:
        # Arrange dest file: import and variable section without the actual data
        print("import csv", file=destfile)  # import statement
        print(file=destfile)  # space
        print("medal_table = [", file=destfile)  # variable

        reader = csv.DictReader(sourcefile)

        # Each row is a dictionary but we require the row to have:
        #   - key to lowercase
        #   - value to be numeric if numeric
        for row in reader:
            new_dict = {}
            for key in headings:
                value = row[key]
                if value.isnumeric():
                    value = int(value)  # numeric value
                new_dict[key.casefold()] = value  # lowercase key

            # For each row print the new_dict to destfile
            print(f"    {new_dict},", file=destfile)

        # Print the terminating ']' after all data is written
        # then finish off with the space at the end
        print("]", file=destfile)
        print(file=destfile)


# ------------------ Tests

cereals_filepath = "../data/csvs/cereals.csv"

# read_csv(cereals_filepath)
# read_csv_different_separator()
# read_csv_different_separator_automated()
# get_csv_dialect_attributes()

# read_csv_dict(cereals_filepath)

# write_csv(cereals_filepath)
write_csv_dictwriter()
# read_csv_write_python()
