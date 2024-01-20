"""Filter data file"""
import pandas as pd

def filter_series_by_language_overview(df_value: pd.DataFrame, language: str, keywords: str):
    """
    Filters series where the original language is
    specified language and overview contains any of the keywords.
    :param df_value: DataFrame to filter.
    :param language: Language to filter by.
    :param keywords: List of keywords to look for in the overview.
    :return: DataFrame with filtered series.
    """
    def contains_keyword(overview: str):
        overview_lower = str(overview).lower()
        return any(keyword in overview_lower for keyword in keywords)

    return df_value[
        (df_value['original_language'] == language) & df_value['overview'].apply(contains_keyword)
    ][['name']]

def get_series_started_and_cancelled(df_value: pd.DataFrame, start_year: int, status: str):

    """
    Filters series that started in a given year and have a specific status.
    Parameters:
    df_value (dataframe): DataFrame to filter.
    start_year (int): Year to filter by.
    status (str): Status to filter by.
    Returns:
    DataFrame with filtered series.
    """

    df_value['first_air_date'] = pd.to_datetime(df_value['first_air_date'], errors='coerce')
    return df_value[
        (df_value['first_air_date'].dt.year == start_year) & (df_value['status'] == status)
    ][['name']]

def get_series_by_language(df_value: pd.DataFrame, language: str):
    """
    Filters series by language, including those with multiple languages.
    Parameters:
    df_value (dataframe): DataFrame to filter.
    language (str): Language to filter by.
    Returns:
    DataFrame with filtered series.
    """
    return df_value[
        df_value['languages'].str.contains(language, na=False)
    ][['name', 'original_name', 'networks', 'production_companies']]
