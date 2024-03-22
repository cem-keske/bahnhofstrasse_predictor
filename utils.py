import numpy as np
import pandas as pd
from datetime import datetime

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

def hour_features(date):
    # Get the hour from each datetime in the array
    datets = pd.Timestamp(date)
    hours = datets.hour

    # Calculate the values for the two columns
    cos_values = np.cos(hours / 24 * 2 * np.pi)
    sin_values = np.sin(hours / 24 * 2 * np.pi)

    return cos_values, sin_values

def day_features(date):
    # Get the hour from each datetime in the array
    datets = pd.Timestamp(date)
    day = datets.dayofweek

    # Calculate the values for the two columns
    cos_values = np.cos(day / 7 * 2 * np.pi)
    sin_values = np.sin(day / 7 * 2 * np.pi)

    return cos_values, sin_values

def dayofyear_features(date):
    # Get the hour from each datetime in the array
    datets = pd.Timestamp(date)
    day = datets.dayofyear

    # Calculate the values for the two columns
    cos_values = np.cos(day / 365 * 2 * np.pi)
    sin_values = np.sin(day / 365 * 2 * np.pi)

    return cos_values, sin_values


def encode(original_dataframe: pd.DataFrame,
           feature_to_encode: str) -> pd.DataFrame:
    dummies = pd.get_dummies(original_dataframe[[feature_to_encode]], dtype=int)
    res = pd.concat([original_dataframe, dummies], axis=1)
    return res.drop(columns=feature_to_encode)


def load_and_preprocess(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Drop unnecessary columns
    df = df[['timestamp', 'location_id', 'weather_condition', 'temperature', 'pedestrians_count']]

    # Rearrange date
    df['date'] = df.apply(lambda row: str(datetime.strptime(row['timestamp'], '%Y-%m-%dT%H:%M:%SZ')), axis=1)
    df = df.drop(columns='timestamp')

    # One-hot encoding for weather
    df = encode(df, 'weather_condition')

    df['time_cos'] = df.apply(lambda row: hour_features(row['date'])[0], axis=1)
    df['time_sin'] = df.apply(lambda row: hour_features(row['date'])[1], axis=1)
    df['day_cos'] = df.apply(lambda row: day_features(row['date'])[0], axis=1)
    df['day_sin'] = df.apply(lambda row: day_features(row['date'])[1], axis=1)
    df['dayofyear_cos'] = df.apply(lambda row: dayofyear_features(row['date'])[0], axis=1)
    df['dayofyear_sin'] = df.apply(lambda row: dayofyear_features(row['date'])[1], axis=1)

    df = df.loc[df['location_id'] == 330]
    df = df.drop(columns=['date', 'location_id'])
    return df
