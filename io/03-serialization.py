import json
import urllib.request


def serialize_data(data, path) -> None:
    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(data, file)


def deserialize_data(path):
    with open(path, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# ----- Get teprature data from a JSON file in a filesystem
# - Read/Deserialize the JSON file
# - Parse the JSON file to Python data structure
def temperature_data():
    data_source = "../data/temperature_anomaly.json"
    data = deserialize_data(data_source)
    print(f"Description: {data['description']}")

    for key, value in data["data"].items():
        year, anamoly = int(key), float(value["anomaly"])
        print(f"{year}: {anamoly:6.2f}")

    print(f"Citation: {data['citation']}")


# ----- Get teprature data from internet in JSON format
# - Read/Deserialize the JSON file
# - Parse the JSON file to Python data structure
def get_temperature_data_from_url():
    data_source = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json"

    with urllib.request.urlopen(data_source) as stream:
        data = stream.read().decode("utf-8")
        json_data = json.loads(data)

    for key, value in json_data["data"].items():
        year, anamoly = int(key), float(value["anomaly"])
        print(f"{year}: {anamoly:6.2f}")


# ------------------ Tests

data = [
    ["ABC", 1987],
    ["Algol 68", 1968],
    ["APL", 1962],
    ["C", 1973],
    ["Haskell", 1990],
    ["Lisp", 1958],
    ["Modula-2", 1977],
    ["Perl", 1987],
]

datatuples = [
    ("ABC", 1987),
    ("Algol 68", 1968),
    ("APL", 1962),
    ("C", 1973),
    ("Haskell", 1990),
    ("Lisp", 1958),
    ("Modula-2", 1977),
    ("Perl", 1987),
]

testfile_path = "../data/test.json"


# serialize_data(data, testfile_path)
# serialize_data(datatuples, testfile_path)  # tuples is serialzed as list
# print("Data:", deserialize_data(testfile_path))
# temperature_data()

get_temperature_data_from_url()
