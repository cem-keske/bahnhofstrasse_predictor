import numpy as np
import pandas as pd

def create_hour_features(datetime_array):
    # Get the hour from each datetime in the array
    hours = np.array([dt.hour for dt in datetime_array])

    # Calculate the values for the two columns
    cos_values = np.cos(hours / 24 * 2 * np.pi)
    sin_values = np.sin(hours / 24 * 2 * np.pi)

    # Create a DataFrame with the values
    df = pd.DataFrame({
        'hour_cos': cos_values,
        'hour_sin': sin_values
    })

    return cos_values, sin_values