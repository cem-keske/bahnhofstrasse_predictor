import pandas as pd
from workalendar.europe import Switzerland


def is_public_holiday(date):
    cal = Switzerland()
    return cal.is_holiday(date)


if __name__ ==  '__main__':
    # Example array of pandas dates
    dates = pd.to_datetime(['2024-01-01', '2024-02-15', '2024-04-19', '2024-07-25', '2024-12-25'])

    # Create an array indicating if each date is a public holiday in the canton of Zurich
    is_public_holiday_array = [is_public_holiday(date) for date in dates]

    print(is_public_holiday_array)
