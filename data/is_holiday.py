import pandas as pd
from datetime import datetime

def check_holiday(dates):

    holidays = [
        # January 2021
        '2021-01-01',  # New Year's Day
        # April 2021
        '2021-04-02',  # Good Friday
        '2021-04-05',  # Easter Monday
        # May 2021
        '2021-05-01',  # Labor Day
        '2021-05-13',  # Driveway
        '2021-05-24',  # Whit Monday
        # August 2021
        '2021-08-01',  # Swiss National Holiday
        # December 2021
        '2021-12-25',  # Christmas
        '2021-12-26',  # St. Stephen's Day
        # January 2022
        '2022-01-01',  # New Year's Day
        # April 2022
        '2022-04-15',  # Good Friday
        '2022-04-18',  # Easter Monday
        # May 2022
        '2022-05-01',  # Labor Day
        '2022-05-26',  # Driveway
        '2022-06-06',  # Whit Monday
        # August 2022
        '2022-08-01',  # Swiss National Holiday
        # December 2022
        '2022-12-25',  # Christmas
        '2022-12-26',  # St. Stephen's Day
        # January 2023
        '2023-01-01',  # New Year's Day
        # April 2023
        '2023-04-07',  # Good Friday
        '2023-04-10',  # Easter Monday
        # May 2023
        '2023-05-01',  # Labor Day
        '2023-05-18',  # Driveway
        '2023-05-29',  # Whit Monday
        # August 2023
        '2023-08-01',  # Swiss National Holiday
        # December 2023
        '2023-12-25',  # Christmas
        '2023-12-26',  # St. Stephen's Day
        # March 2024
        '2024-03-29',  # Good Friday
        # April 2024
        '2024-04-01',  # Easter Monday
        # May 2024
        '2024-05-01',  # Labor Day
        '2024-05-09',  # Driveway
        '2024-05-20',  # Whit Monday
        # August 2024
        '2024-08-01',  # Swiss National Holiday
        # December 2024
        '2024-12-25',  # Christmas
        '2024-12-26'   # St. Stephen's Day
    ]

    results = []

    for date in dates:
        date_only = date.split()[0]  # Extract only the date part
        if date_only in holidays:
            results.append(True)
        else:
            results.append(False)

    return results


if __name__ == '__main__':
    date_array = [
        '2024-05-01 12:00:00',
        '2024-08-01 15:30:00',
        '2024-12-28 09:45:00'
    ]

    results = check_holiday(date_array)

    for i, date in enumerate(date_array):
        if results[i]:
            print(f"{date} is a holiday.")
        else:
            print(f"{date} is not a holiday.")