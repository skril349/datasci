import argparse
import file_processing
import data_processing

def main():
    parser = argparse.ArgumentParser(description="TMDB Data Processing Script")
    parser.add_argument('--extract', action='store_true', help='Extract zip file')
    parser.add_argument('--merge_pandas', action='store_true', help='Merge CSV files using Pandas')
    parser.add_argument('--merge_dict', action='store_true', help='Merge CSV files into a dictionary')
    parser.add_argument('--air_days', action='store_true', help='Calculate highest 10 air days')
    parser.add_argument('--series_dict', action='store_true', help='Create series poster dict')

    args = parser.parse_args()

    csv_files = ['data/TMDB_info.csv', 'data/TMDB_overview.csv', "data/TMDB_distribution.csv"]

    if args.extract:
        zip_path = 'data/TMDB.zip'
        extracting_folder = 'data/'
        file_processing.extract_file(zip_path, extracting_folder)

    if args.merge_pandas:
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        print(merged_df.head(10))

    if args.merge_dict:
        merged_dict = file_processing.read_and_merge_csv_dict(csv_files)
        print(dict(list(merged_dict.items())[:5])) 

    if args.air_days:
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        merged_df = data_processing.calculate_air_days(merged_df)
        top_10_air_days = merged_df.nlargest(10, 'air_days')[['name', 'air_days']]
        print("Top 10 series by air days:\n", top_10_air_days)

    if args.series_dict:
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        series_poster_dict = data_processing.create_series_poster_dict(merged_df)
        print("First 5 entries in the series poster dictionary:\n", dict(list(series_poster_dict.items())[:5]))

    # If no arguments are provided, execute all the functions
    if not (args.extract or args.merge_pandas or args.merge_dict or args.air_days or args.series_dict):
        # Extract files
        zip_path = 'data/TMDB.zip'
        extracting_folder = 'data/'
        file_processing.extract_file(zip_path, extracting_folder)

        # Merge with pandas and print
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        print(merged_df.head(10))

        # Merge into a dictionary and print
        merged_dict = file_processing.read_and_merge_csv_dict(csv_files)
        print(dict(list(merged_dict.items())[:5]))

        # Calculate air days and print
        merged_df = data_processing.calculate_air_days(merged_df)
        top_10_air_days = merged_df.nlargest(10, 'air_days')[['name', 'air_days']]
        print("Top 10 series by air days:\n", top_10_air_days)

        # Create series poster dictionary and print
        series_poster_dict = data_processing.create_series_poster_dict(merged_df)
        print("First 5 entries in the series poster dictionary:\n", dict(list(series_poster_dict.items())[:5]))

        pass

if __name__ == "__main__":
    main()
