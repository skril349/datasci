import argparse
import file_processing
import data_processing
import filter_data
import graphics

def main():
    parser = argparse.ArgumentParser(description="TMDB Data Processing Script")
    parser.add_argument('--extract', action='store_true', help='Extract zip file')
    parser.add_argument('--merge_pandas', action='store_true', help='Merge CSV files using Pandas')
    parser.add_argument('--merge_dict', action='store_true', help='Merge CSV files into a dictionary')
    parser.add_argument('--air_days', action='store_true', help='Calculate highest 10 air days')
    parser.add_argument('--series_dict', action='store_true', help='Create series poster dict')
    parser.add_argument('--english_series', action='store_true', help='English series')
    parser.add_argument('--startandcancelled_series', action='store_true', help='Series started in 2023 and canceled')
    parser.add_argument('--japanese_series', action='store_true', help='Japanese series')
    parser.add_argument('--bar_chart', action='store_true', help='graphic bars')
    parser.add_argument('--decade_count', action='store_true', help='graphic bars decade counts')
    parser.add_argument('--chart_per_genre', action='store_true', help='graphic bars by genere')

    args = parser.parse_args()

    csv_files = ['data/TMDB_info.csv', 'data/TMDB_overview.csv', "data/TMDB_distribution.csv"]

    ''' EXERCICI 1 '''

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

    ''' EXERCICI 2 '''

    if args.air_days:
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        merged_df = data_processing.calculate_air_days(merged_df)
        top_10_air_days = merged_df.nlargest(10, 'air_days')[['name', 'air_days']]
        print("Top 10 series by air days:\n", top_10_air_days)

    if args.series_dict:
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        series_poster_dict = data_processing.create_series_poster_dict(merged_df)
        print("First 5 entries in the series poster dictionary:\n", dict(list(series_poster_dict.items())[:5]))

    ''' EXERCICI 3 '''

    if args.english_series:
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        english_series_with_keywords = filter_data.filter_series_by_language_overview(
            merged_df, 'en', ['mystery', 'crime']
        )
        print("English series with 'mystery' or 'crime' in overview:\n", english_series_with_keywords.head())

    if args.startandcancelled_series:
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        series_started_and_cancelled = filter_data.get_series_started_and_cancelled(merged_df, 2023, 'Canceled')
        print("Series started in 2023 and canceled:\\n", series_started_and_cancelled.head(20))

    if args.japanese_series:
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        japanese_series = filter_data.get_series_by_language(merged_df, 'ja')
        print("Japanese series:\\n", japanese_series.head(20))

    ''' EXERCICI 4 '''

    if args.bar_chart:
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        graphics.series_per_start_year(merged_df)
    
    if args.decade_count:
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        graphics.series_per_type_and_decade(merged_df)

    if args.chart_per_genre:
        merged_df = file_processing.read_and_merge_csv_pandas(csv_files)
        graphics.series_per_genre(merged_df)

    # If no arguments are provided, execute all the functions
    if not (args.extract or args.merge_pandas or args.merge_dict or args.air_days or args.series_dict or args.english_series or args.startandcancelled_series or args.japanese_series or args.bar_chart or args.decade_count or args.chart_per_genre):
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

        # English series
        english_series_with_keywords = filter_data.filter_series_by_language_overview(
        merged_df, 'en', ['mystery', 'crime']
        )
        print("English series with 'mystery' or 'crime' in overview:\\n", english_series_with_keywords.head())

        # Started and canceled series in 2023
        series_started_and_cancelled = filter_data.get_series_started_and_cancelled(merged_df, 2023, 'Canceled')
        print("Series started in 2023 and canceled:\\n", series_started_and_cancelled.head(20))

        #Japanese series
        japanese_series = filter_data.get_series_by_language(merged_df, 'ja')
        print("Japanese series:\\n", japanese_series.head(20))

        # Graphics 
        graphics.series_per_start_year(merged_df)
        graphics.series_per_type_and_decade(merged_df)
        graphics.series_per_genre(merged_df)


        pass

if __name__ == "__main__":
    main()
