from datetime import time, date, datetime, timedelta, timezone
import zoneinfo


def time_intro():
    # Create time using time constructor
    meeting = time(hour=10, minute=15, second=0)
    print(meeting)

    end_time = time(hour=11, minute=30)  # second defaults to 0
    print(end_time)

    # Create time using ISO format
    time_from_isostring = time.fromisoformat("12:15:00")
    print(time_from_isostring)

    # Create date using ISO format
    date_from_isostring = date.fromisoformat("2025-06-18")
    print(date_from_isostring)


def timezone_intro():
    now = datetime.now()
    print(f"Now: {now}")

    germany_now = datetime.now(tz=zoneinfo.ZoneInfo("Europe/Berlin"))
    print(f"Germany now: {germany_now}")

    # UTC is a time standard
    # It is used to compare with other timezones
    utc_now = datetime.now(timezone.utc)
    print(f"UTC now: {utc_now}")

    local_now = utc_now.astimezone()
    print(f"Local now: {local_now}")

    new_york_tz = zoneinfo.ZoneInfo("America/New_York")
    ny_now = utc_now.astimezone(tz=new_york_tz)
    print(f"New York now: {ny_now}")

    france_tz = zoneinfo.ZoneInfo("Europe/Paris")
    france_now = utc_now.astimezone(tz=france_tz)
    print(f"France now: {france_now}")


def timezone_keys():
    for zone_key in sorted(zoneinfo.available_timezones()):
        print(zone_key)


def get_timezone(zones: tuple):
    utc_now = datetime.now(tz=timezone.utc)
    utc_now = utc_now.replace(microsecond=0)  # remove microsecond

    for zone in zones:
        tz = zoneinfo.ZoneInfo(zone)
        required_time = utc_now.astimezone(tz=tz)
        location = zone.split("/")[-1]
        print(
            f"The time in city {location}: {required_time.strftime('%d-%m-%Y %H:%M:%S %z %Z')}"
        )


def datetime_arithmetic():
    uk_tz = zoneinfo.ZoneInfo("Europe/London")
    us_tz = zoneinfo.ZoneInfo("America/New_York")

    year = 2025
    month = 7
    day = 27
    hour = 9
    minute = 30
    td = timedelta(minutes=25)

    uk_time = datetime(year, month, day, hour, minute, tzinfo=uk_tz)
    print(f"UK time: {uk_time}")

    # Convert to UTC timezone gives the local timezone with no DST
    utc_time = uk_time.astimezone(tz=timezone.utc)
    print(f"UK UTC time: {utc_time}")

    # Perform datetime arithmetic
    utc_time = utc_time + td
    print(f"UK UTC time with deltatime: {utc_time}")

    # Convert back to original timezone with DST
    uk_time = utc_time.astimezone(tz=uk_tz)
    print(f"UK time with deltatime: {uk_time}")


# ------------------ Test

# time_intro()
# timezone_intro()

# timezone_keys()

# zones = ("Europe/Paris", "Europe/Berlin", "Asia/Hong_Kong", "Africa/Nairobi")
# get_timezone(zones)

datetime_arithmetic()
