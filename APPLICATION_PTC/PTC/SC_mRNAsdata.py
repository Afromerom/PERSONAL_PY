"""
SC_mRNAsdata: Original mRNAs dataset from GSE114071

Description:
    Este archivo contiene la expresión génica de mRNAs de 23284 mRNAs obtenidos de 22 muestras.
    Los datos fueron extraídos del archivo GSE114071.

Formato:
    Un array NumPy o DataFrame de Pandas con 23285 filas y 24 columnas.
    - Las filas representan las muestras (a partir de la fila 2).
    - Las columnas contienen los nombres de los miRNAs, la descripción, y las muestras.

Referencias:
    Wang, N., Zheng, J., Chen, Z. et al.
    "Single-cell microRNA-mRNA co-sequencing reveals non-genetic heterogeneity
    and mechanisms of microRNA regulation."
    Nat Commun 10, 95 (2019).
    https://doi.org/10.1038/s41467-018-07981-6
"""
import pandas as pd

# Carga del dataset desde un archivo CSV o similar
SC_mRNAsdata = pd.read_csv('APPLICATION_PTC/DATA/SC_mRNAsdata.csv')

# Información básica del dataset
print(SC_mRNAsdata.shape)  # Debería mostrar (23285, 24) si los datos están correctamente cargados
print(SC_mRNAsdata.head())  # Mostrar las primeras filas del dataset
