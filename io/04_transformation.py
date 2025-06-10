import csv

# ------------------ Test data

keys = ["album", "artist", "year"]
albums = [
    ("One", "Tesseract", 2013),
    ("Periphery", "Periphery", 2010),
    ("Silhouettes", "Textures", 2008),
    ("Animals as Leaders", "Animals as Leaders", 2009),
    ("Language", "The Contortionists", 2014),
]


# As the data is List/Tuple, use csv.writer()
def write_csv(filepath):
    with open(filepath, mode="w", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(keys)
        writer.writerows(albums)


def zip_test():
    for item in zip([1, 2, 3], ["apple", "ball", "cat"]):
        print(item)


# The data is List/Tuple, so in order to use DictWriter,
# the data needs to be transformed first
def transform_seq_dict_zip(filepath):
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()
        for row in albums:
            zip_obj = zip(keys, row)  # get iterator of zipped object
            album_dict = dict(zip_obj)  # create dict passing the iterator
            print(album_dict)
            writer.writerow(album_dict)


# ------------------ Test

destfile = "../data/csvs/albums.csv"

# write_csv(destfile)
# zip_test()
transform_seq_dict_zip(destfile)
