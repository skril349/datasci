import argparse
import file_processing

def main():
    parser = argparse.ArgumentParser(description="TMDB Data Processing Script")
    parser.add_argument('--extract', action='store_true', help='Extract zip file')
    parser.add_argument('--merge_pandas', action='store_true', help='Merge CSV files using Pandas')
    parser.add_argument('--merge_dict', action='store_true', help='Merge CSV files into a dictionary')

    args = parser.parse_args()

    if args.extract or (not args.merge_pandas and not args.merge_dict):
        zip_path = 'data/TMDB.zip'
        extracting_folder = 'data/'
        file_processing.extract_file(zip_path, extracting_folder)

    if args.merge_pandas or (not args.extract and not args.merge_dict):
        csv_files = ['data/TMDB_info.csv', 'data/TMDB_overview.csv', "data/TMDB_distribution.csv"]
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        print(merged_df.head(10))

    if args.merge_dict or (not args.extract and not args.merge_pandas):
        csv_files = ['data/TMDB_info.csv', 'data/TMDB_overview.csv', "data/TMDB_distribution.csv"]
        merged_dict = file_processing.read_and_merge_csv_dict(csv_files)
        print(dict(list(merged_dict.items())[:5]))  # Print first 5 items of the dictionary

if __name__ == "__main__":
    main()
