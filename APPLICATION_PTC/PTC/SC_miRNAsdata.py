"""
SC_miRNAsdata: Original miRNAs dataset from GSE114071

Descripción:
    Este archivo contiene la expresión génica normalizada y transformada en log2
    de 2822 miRNAs obtenidos de 21 muestras. Los datos fueron extraídos del archivo GSE114071.

Formato:
    Un array NumPy o DataFrame de Pandas con 2822 filas y 23 columnas.
    - Las filas representan las muestras.
    - Las columnas contienen los nombres de los miRNAs, la descripción y los datos de las muestras.

Referencias:
    Wang, N., Zheng, J., Chen, Z. et al.
    "Single-cell microRNA-mRNA co-sequencing reveals non-genetic heterogeneity
    and mechanisms of microRNA regulation."
    Nat Commun 10, 95 (2019).
    https://doi.org/10.1038/s41467-018-07981-6
"""
import pandas as pd

# Cargar el dataset de miRNAs desde un archivo CSV (o similar)
SC_miRNAsdata = pd.read_csv('APPLICATION_PTC\DATA\SC_miRNAsdata.csv')

# Mostrar información básica del dataset
print(SC_miRNAsdata.shape)  # Debería mostrar (2822, 23)
print(SC_miRNAsdata.head())  # Mostrar las primeras filas del dataset
