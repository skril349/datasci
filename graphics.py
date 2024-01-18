import pandas as pd
import matplotlib.pyplot as plt
/mnt/c/Users/tvive/Documents/UOC/programació_per_la_ciència_de_dades/PAC6/datasci_pac4/data
# EXERCICI 4.1: Nombre de sèries per any d'inici
def series_per_start_year(merged_df):

    """
    Generates a bar chart showing the number of series per start year.

    Parameters:
    df (DataFrame): DataFrame containing series data with a 'first_air_date' column.

    Returns:
    None: Displays the generated bar chart.
    """

    merged_df['first_air_date'] = pd.to_datetime(merged_df['first_air_date'], errors='coerce')
    year_counts = merged_df['first_air_date'].dt.year.value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    year_counts.plot(kind='bar')
    plt.title('Nombre de sèries per any d\'inici')
    plt.xlabel('Any')
    plt.ylabel('Nombre de sèries')
    plt.savefig('graphics/series_per_year.png')  # Guarda el gràfic en un fitxer
    print("saved file by year as /graphics/series_per_year.png ")

# EXERCICI 4.2: Nombre de sèries de cada "type" per dècada
def series_per_type_and_decade(merged_df):

    """
    Generates a line chart showing the number of series per decade.

    Parameters:
    df (DataFrame): DataFrame containing series data with a 'first_air_date' column.

    Returns:
    None: Displays the generated line chart.
    """

    merged_df['first_air_date'] = pd.to_datetime(merged_df['first_air_date'], errors='coerce')
    merged_df['decade'] = (merged_df['first_air_date'].dt.year // 10) * 10
    type_decade_counts = merged_df.groupby(['decade', 'type']).size().unstack().fillna(0)
    plt.figure(figsize=(10, 6))
    type_decade_counts.plot(kind='line')
    plt.title('Nombre de sèries per tipus i dècada')
    plt.xlabel('Dècada')
    plt.ylabel('Nombre de sèries')
    plt.legend(title='Tipus')
    plt.savefig('graphics/series_per_decade.png')  # Guarda el gràfic en un fitxer
    print("saved file by decade as /graphics/series_per_decade.png ")

# EXERCICI 4.3: Nombre de sèries per gènere
def series_per_genre(merged_df):

    """
    Obtaining the number of series by genre showing 
    the percentage of the total in a pie chart. 
    Genres that represent less than 1% of the 
    total will be included in the "Other" category.

    Parameters:
    df (DataFrame): pandas dataframe.

    Returns:
    None: Displays the generated pie chart.
    """

    genre_counts = merged_df['genres'].str.split(', ').explode().value_counts()
    total = genre_counts.sum()
    genre_counts = genre_counts[genre_counts / total >= 0.01]
    genre_counts['Other'] = total - genre_counts.sum()
    plt.figure(figsize=(10, 6))
    genre_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title('Percentatge de sèries per gènere')
    plt.ylabel('')
    plt.savefig('graphics/series_per_genre.png')  # Guarda el gràfic en un fitxer
    print("saved file by genre as /graphics/series_per_genre.png ")