# ------------------ Parsing Text files
def read_data():
    with open("../data/country_info.txt") as file:
        for row in file:  # row is a line of single string
            # strip then split returns list of separated strings
            data = row.strip("\n").split(sep="|")
            print(data)


def read_data_to_dict():
    countries = {}
    with open("../data/country_info.txt") as file:
        file.readline()
        for row in file:
            data = row.strip("\n").split(sep="|")
            country, capital, code, code3, dialing, timezone, currency = data
            country_dict = {
                "name": country,
                "capital": capital,
                "country_code": code,
                "cc3": code3,
                "dialing_code": dialing,
                "timezone": timezone,
                "currency": currency,
            }
            # print(country_dict)
            countries[country.casefold()] = country_dict

    # print(countries)
    while True:
        chosen_country = input("Enter the name of the country: ")
        country_key = chosen_country.casefold()
        if country_key in countries:
            country_data = countries[country_key]
            print(f"The capital of {chosen_country} is {country_data['capital']}")
        elif chosen_country == "quit":
            break


# ------------------ Tests

# read_data()
read_data_to_dict()
