# Projecte d'Anàlisi de Dades TMDB

Aquest projecte conté scripts de Python per processar i analitzar dades de The Movie Database (TMDB). Inclou funcionalitats per a descomprimir fitxers, llegir dades de fitxers CSV, i fusionar-les utilitzant diferents mètodes.

## Funcionalitats

El script principal `main.py` pot executar les següents tasques:

- **Descompressió de Fitxers**: Descomprimeix fitxers en format zip i tar.gz.
- **Fusió de Dades amb Pandas**: Llegeix múltiples fitxers CSV i els fusiona en un únic DataFrame utilitzant Pandas.
- **Fusió de Dades en un Diccionari**: Llegeix fitxers CSV i els integra en un únic diccionari utilitzant la llibreria `csv`.

## Com Utilitzar

Per executar el script `main.py`, podeu utilitzar diferents arguments de línia de comandes per executar tasques específiques:

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
- **`--air_days`**: Només executa la funció de calcular els 10 dies amb mes emisions.
    ```
    python main.py --air_days
    ```
- **`--series_dict`**: Només executa la funció de mostrar un diccionari amb les 5 series i els seus posters.
    ```
    python main.py --series_dict
    ```
## Resposta a l'Exercici 4

**Comparació entre la Fusió amb Pandas i en un Diccionari:**

- **Pandas vs. Diccionari**: La fusió amb Pandas ha resultat ser més ràpida que la fusió en un diccionari. Això és degut a l'optimització interna de Pandas per a la manipulació de grans conjunts de dades.

- **Eficiència amb Grans Fitxers**: Per a fitxers de gran mida (com 10GB), Pandas probablement seria més eficient si la memòria ho permet. Si la memòria és una preocupació, la lectura en parts (chunking) amb Pandas o l'aproximació basada en diccionaris pot ser una millor solució.

- **Conclusió**: Per a grans volums de dades i amb suficient memòria, Pandas és l'opció preferida. Per a situacions amb restriccions de memòria, el mètode basat en diccionaris pot ser més adequat.
