import unittest
import pandas as pd
import sys
import os
from io import StringIO
sys.path.append(os.path.abspath(os.path.join('..')))
import file_processing
import data_processing
import filter_data
import graphics


class FileProcessingTest(unittest.TestCase):
    # Testos per a file_processing.py

    def test_read_and_merge_csv_pandas(self):
        # Test per verificar la fusió correcta de CSV amb Pandas
        test_files = ['tests/test_TMDB_info.csv', 'tests/test_TMDB_overview.csv','tests/test_TMDB_distribution.csv']
        merged_df = file_processing.read_and_merge_csv_pandas(test_files)
        self.assertIsInstance(merged_df, pd.DataFrame)
        self.assertTrue('id' in merged_df.columns)
        self.assertEqual(len(merged_df), 50)

    def test_read_and_merge_csv_dict(self):
        # Test per verificar la fusió correcta de CSV en un diccionari
        test_files = ['tests/test_TMDB_info.csv', 'tests/test_TMDB_overview.csv','tests/test_TMDB_distribution.csv']
        merged_dict = file_processing.read_and_merge_csv_dict(test_files)
        self.assertIsInstance(merged_dict, dict)
        self.assertEqual(len(merged_dict), 50)

class DataProcessingTest(unittest.TestCase):
    # Testos per a data_processing.py

    def test_calculate_air_days(self):
        # Test per verificar el càlcul correcte dels dies d'emetició
        test_files = ['tests/test_TMDB_info.csv', 'tests/test_TMDB_overview.csv','tests/test_TMDB_distribution.csv']
        merged_df = file_processing.read_and_merge_csv_pandas(test_files)        
        df_with_air_days = data_processing.calculate_air_days(merged_df)
        self.assertIsInstance(df_with_air_days, pd.DataFrame)
        self.assertIn('air_days', df_with_air_days.columns)
        self.assertNotIn(None, df_with_air_days['air_days'])

    def test_create_series_poster_dict(self):
        # Test per verificar la creació correcta del diccionari de pòsters
        test_files = ['tests/test_TMDB_info.csv', 'tests/test_TMDB_overview.csv','tests/test_TMDB_distribution.csv']
        merged_df = file_processing.read_and_merge_csv_pandas(test_files)        
        poster_dict = data_processing.create_series_poster_dict(merged_df)
        self.assertIsInstance(poster_dict, dict)
        self.assertTrue(len(poster_dict) > 0)

class FilterDataTest(unittest.TestCase):
    # Testos per a filter_data.py

    def test_filter_series_by_language_overview(self):
        # Test per verificar el filtratge correcte per idioma i paraules clau en la descripció
        test_files = ['tests/test_TMDB_info.csv', 'tests/test_TMDB_overview.csv','tests/test_TMDB_distribution.csv']
        merged_df = file_processing.read_and_merge_csv_pandas(test_files)
        filtered_df = filter_data.filter_series_by_language_overview(merged_df, 'en', ['mystery', 'crime'])
        self.assertTrue(len(filtered_df) > 0)

    def test_get_series_started_and_cancelled(self):
        # Test per verificar el filtratge correcte de sèries iniciades i cancel·lades
        test_files = ['tests/test_TMDB_info.csv', 'tests/test_TMDB_overview.csv','tests/test_TMDB_distribution.csv']
        merged_df = file_processing.read_and_merge_csv_pandas(test_files)
        filtered_df = filter_data.get_series_started_and_cancelled(merged_df, 2023, 'Canceled')
        self.assertTrue(len(filtered_df) >= 0)

    def test_get_series_by_language(self):
        # Test per verificar el filtratge correcte de sèries per idioma
        test_files = ['tests/test_TMDB_info.csv', 'tests/test_TMDB_overview.csv','tests/test_TMDB_distribution.csv']
        merged_df = file_processing.read_and_merge_csv_pandas(test_files)
        filtered_df = filter_data.get_series_by_language(merged_df, 'ja')
        self.assertTrue(len(filtered_df) > 0)

if __name__ == '__main__':
    unittest.main()
