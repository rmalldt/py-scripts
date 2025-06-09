import json

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


def serialize_data():
    with open("../data/test.json", mode="w", encoding="utf-8") as file:
        json.dump(data, file)


# ------------------ Tests


serialize_data()
