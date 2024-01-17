
import file_processing

# Example usage of the file_processing
# You can replace these file paths with the actual paths you will be using
example_zip_path = 'data/TMDB.zip'
example_extract_folder = 'data/'
file_processing.extract_file(example_zip_path, example_extract_folder)

example_csv_files = ['data/TMDB_info.csv', 'data/TMDB_overview.csv',"data/TMDB_distribution.csv"]
merged_df = file_processing.read_and_merge_csv_pandas(example_csv_files)
print(merged_df.head(10))

merged_dict = file_processing.read_and_merge_csv_dict(example_csv_files)
print(dict(list(merged_dict.items())[:5])) # Print first 5 items of the dictionary
