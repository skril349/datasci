import pandas as pd
import matplotlib.pyplot as plt

# Llegir i fusionar les dades (aquest codi assumeix que ja teniu un DataFrame combinat)
# merged_df = pd.concat([pd.read_csv(file) for file in csv_files])

# EXERCICI 4.1: Nombre de sèries per any d'inici
def series_per_start_year(merged_df):
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
    return type_decade_counts

# EXERCICI 4.3: Nombre de sèries per gènere
def series_per_genre(merged_df):
    genre_counts = merged_df['genres'].str.split(', ').explode().value_counts()
    total = genre_counts.sum()
    genre_counts = genre_counts[genre_counts / total >= 0.01]
    genre_counts['Other'] = total - genre_counts.sum()
    return genre_counts
