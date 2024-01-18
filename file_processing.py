
import zipfile
import tarfile
import os
import pandas as pd
import csv
from collections import defaultdict
import time

def extract_file(file_path, extract_to_folder):
    """
    Extracts a zip file to the specified folder.

    Parameters:
    zip_path (str): Path to the zip file to be extracted.
    extracting_folder (str): Destination folder where the contents of the zip file will be extracted.

    Returns:
    None
    """

    start_time = time.time()
    if file_path.endswith('.zip'):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to_folder)
        print(f"Extracted {file_path} in {extract_to_folder}")
    elif file_path.endswith('.tar.gz'):
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall(extract_to_folder)
        print(f"Extracted {file_path} in {extract_to_folder}")
    else:
        print("Error: Unsupported file format. Only zip and tar.gz are supported.")
    end_time = time.time()
    print(f"Extraction Time: {end_time - start_time} seconds")

def read_and_merge_csv_pandas(file_paths, key_column='id'):

    """
    Read and merge all csv by id to create pandas dataframe.

    Parameters:
    file_paths (array): csv files paths.
    Returns: 
    dataframe

    """

    start_time = time.time()
    merged_df = pd.DataFrame()
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        if merged_df.empty:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on=key_column, how='outer')
    end_time = time.time()
    print(f"CSV Merge (Pandas) Time: {end_time - start_time} seconds")
    return merged_df

def read_and_merge_csv_dict(file_paths, key_column='id'):

    """
    Read and merge all csv by id to create dictionary.

    Parameters:
    file_paths (array): csv files paths.
    Returns: 
    dictionary
    
    """

    start_time = time.time()
    merged_data = defaultdict(dict)
    for file_path in file_paths:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id_value = row[key_column]
                merged_data[id_value].update(row)
    end_time = time.time()
    print(f"CSV Merge (Dictionary) Time: {end_time - start_time} seconds")
    return merged_data
