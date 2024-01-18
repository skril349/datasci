
import pandas as pd
import os
from datetime import datetime
from collections import OrderedDict

# Exercici 2.1: Calculate air days and display top 10 series by air days
def calculate_air_days(df:pd.DataFrame):

    """
    Calculate the number of days each series was on air.

    This function adds a new column 'air_days' to the DataFrame, representing
    the number of days from the first air date to the last air date of a series.

    Parameters:
    df (DataFrame): A pandas DataFrame containing the columns 'first_air_date' and 'last_air_date'.

    Returns:
    DataFrame: The original DataFrame augmented with the 'air_days' column.
    """

    df['first_air_date'] = pd.to_datetime(df['first_air_date'], errors='coerce')
    df['last_air_date'] = pd.to_datetime(df['last_air_date'], errors='coerce')
    df['air_days'] = (df['last_air_date'] - df['first_air_date']).dt.days
    return df



# Exercici 2.2: Create a dictionary for series names and complete web address of their poster
def create_series_poster_dict(df: pd.DataFrame):

    """
    Create an ordered dictionary whose key will be the name of the 
    series (name) and whose value will be the full web address of 
    your poster (homepage and poster_path). If homepage or
    poster_path has the value NaN or "", the value will be the 
    string “NOT AVAILABLE”. Display the first 5 records of the dictionary..

    

    Parameters:
    df (DataFrame): A pandas DataFrame.

    Returns:
    Dictionary.
    """

    poster_dict = OrderedDict()
    for _, row in df.iterrows():
        name = row['name']
        homepage = row['homepage'] if pd.notna(row['homepage']) and row['homepage'] else "NOT AVAILABLE"
        poster_path = row['poster_path'] if pd.notna(row['poster_path']) and row['poster_path'] else "NOT AVAILABLE"
        poster_url = homepage + poster_path if homepage != "NOT AVAILABLE" and poster_path != "NOT AVAILABLE" else "NOT AVAILABLE"
        poster_dict[name] = poster_url
    return poster_dict



