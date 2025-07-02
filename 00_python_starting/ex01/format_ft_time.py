from time import time
from datetime import datetime
from calendar import month_abbr

seconds = time()
seconds_comma = '{:,}'.format(round(seconds, 4))
scientific_notation = '{:.2e}'.format(seconds)

date = datetime.now()
month = month_abbr[date.month]

print(f"Seconds since January 1, 1970: {seconds_comma} or {scientific_notation} in scientific notation")
print(f"{month} {date.day} {date.year}")