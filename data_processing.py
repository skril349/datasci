
import pandas as pd
import os
from datetime import datetime
from collections import OrderedDict

# Exercici 2.1: Calculate air days and display top 10 series by air days
def calculate_air_days(df):
    df['first_air_date'] = pd.to_datetime(df['first_air_date'], errors='coerce')
    df['last_air_date'] = pd.to_datetime(df['last_air_date'], errors='coerce')
    df['air_days'] = (df['last_air_date'] - df['first_air_date']).dt.days
    return df



# Exercici 2.2: Create a dictionary for series names and complete web address of their poster
def create_series_poster_dict(df):
    poster_dict = OrderedDict()
    for _, row in df.iterrows():
        name = row['name']
        homepage = row['homepage'] if pd.notna(row['homepage']) and row['homepage'] else "NOT AVAILABLE"
        poster_path = row['poster_path'] if pd.notna(row['poster_path']) and row['poster_path'] else "NOT AVAILABLE"
        poster_url = homepage + poster_path if homepage != "NOT AVAILABLE" and poster_path != "NOT AVAILABLE" else "NOT AVAILABLE"
        poster_dict[name] = poster_url
    return poster_dict



