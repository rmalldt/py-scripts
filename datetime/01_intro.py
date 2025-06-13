from calendar import month
import datetime

start = datetime.date(2025, 6, 13)
print(start)

formatted_start = start.strftime("%A %d %B %Y")
print(formatted_start)

year = start.year
month = start.month
day = start.day

print(f"The {year}, the {month} and the {day}")
