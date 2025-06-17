import datetime
import locale


def datetime_intro():
    start = datetime.date(2025, 6, 13)
    print(start)

    year = start.year
    month = start.month
    day = start.day
    print(f"Year: {year}, month: {month}, day: {day}")


def formatted_date():
    today = datetime.date.today()

    # Formatted datetime
    # strftime (string-format-time) => string to time
    #   - %A = name of the day of the week
    #   - %d = day of the month
    #   - %B = month name
    #   - %Y = year
    formatted_date = today.strftime("%A %d %B %Y")
    print(formatted_date)


def locale_intro():
    locale.setlocale(locale.LC_ALL, "en_GB.utf-8")
    today = datetime.date.today()

    print(today.strftime("%A %d %B %Y"))


def time_delta():
    today = datetime.date.today()

    # Create duration
    duration = datetime.timedelta(days=15)
    finish = today + duration
    print(finish)

    duration = datetime.timedelta(days=15, hours=48)  # technically 17 days
    finish = today + duration
    print(finish)

    # All units are converted to seconds under the hood
    d1 = datetime.timedelta(hours=1)
    d2 = datetime.timedelta(minutes=60)
    d3 = datetime.timedelta(seconds=3600)
    print(repr(d1), repr(d2), repr(d2))

    # Difference
    difference = finish - today
    print(f"Difference: {difference}")


# ------------------ Test

# datetime_intro()
# formatted_date()
# locale_intro()

time_delta()
