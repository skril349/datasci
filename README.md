# Projecte d'Anàlisi de Dades TMDB

Aquest projecte conté scripts de Python per processar i analitzar dades de The Movie Database (TMDB). Inclou funcionalitats per a descomprimir fitxers, llegir dades de fitxers CSV, i fusionar-les utilitzant diferents mètodes.

El projecte està dividit de la següent manera:

- `graphics` conté les funcions per poder plotejar.
- `filter_data` conté les funcions per poder filtrar informació.
- `file_processing` conté les funcions per processar els fitxers csv.
- `data_procesing`conté les funcions per processar el dataframe.
- `main` is the main file, and the one that should be run.


## Funcionalitats

El script principal `main.py` pot executar les següents tasques:

- **Descompressió de Fitxers**: Descomprimeix fitxers en format zip i tar.gz.
- **Fusió de Dades amb Pandas**: Llegeix múltiples fitxers CSV i els fusiona en un únic DataFrame utilitzant Pandas.
- **Fusió de Dades en un Diccionari**: Llegeix fitxers CSV i els integra en un únic diccionari utilitzant la llibreria `csv`.

## Com Utilitzar

Per executar el script `main.py`, podeu utilitzar diferents arguments de línia de comandes per executar tasques específiques:

Es pot crear un entorn virtual si es vol:
```
virtualenv venv
```

Posteriorment instalarem els requeriments necessaris:
```
pip install -r requirements.txt
```
L'execució del codi es pot fer de dues maneres, sense arguments o amb arguments:

- **Sense Arguments**: Executa totes les funcions per defecte.
    ```
    python main.py
    ```
- **`--extract`**: Només executa la funció de descompressió.
    ```
    python main.py --extract
    ```
- **`--merge_pandas`**: Només executa la funció de fusió de dades amb Pandas.
    ```
    python main.py --merge_pandas
    ```
- **`--merge_dict`**: Només executa la funció de fusió de dades en un diccionari.
    ```
    python main.py --merge_dict
    ```
- **`--air_days`**: Només executa la funció de calcular les 10 series amb mes dies d'emissió.
    ```
    python main.py --air_days
    ```
- **`--series_dict`**: Només executa la funció de mostrar un diccionari amb les 5 series i els seus posters.
    ```
    python main.py --series_dict
    ```
- **`--english_series`**: Només executa la funció de mostrar les series en angles amb "overview" de misteri o crim.
    ```
    python main.py --english_series
    ```
- **`--startandcancelled_series`**: Només executa la funció de mostrar les series iniciades i cancelades en 2023.
    ```
    python main.py --startandcancelled_series
    ```
- **`--japanese_series`**: Només executa la funció de mostrar el dataframe amb les series japoneses.
    ```
    python main.py --japanese_series
    ```

    
### Tests
Els tests es poden executar mitjançant el següent comandament:
```
python3 -m tests.test
```

## Resposta a l'Exercici 1.4

**Comparació entre la Fusió amb Pandas i en un Diccionari:**

- **Pandas vs. Diccionari**: La fusió amb Pandas ha resultat ser més ràpida que la fusió en un diccionari. Això és degut a l'optimització interna de Pandas per a la manipulació de grans conjunts de dades.

- **Eficiència amb Grans Fitxers**: Per a fitxers de gran mida (com 10GB), Pandas probablement seria més eficient si la memòria ho permet. Si la memòria és una preocupació, la lectura en parts (chunking) amb Pandas o l'aproximació basada en diccionaris pot ser una millor solució.

- **Conclusió**: Per a grans volums de dades i amb suficient memòria, Pandas és l'opció preferida. Per a situacions amb restriccions de memòria, el mètode basat en diccionaris pot ser més adequat.
