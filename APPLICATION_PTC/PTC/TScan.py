"""
TScan: TargetScan 7.0 - Predicciones de miRNAs y genes objetivo

Descripción:
    Este archivo contiene una matriz con los nombres de miRNAs y sus genes objetivo predichos,
    obtenidos de TargetScan Release 7.0. Los nombres de los miRNAs fueron transformados a la
    versión miRBase v21 utilizando el método PTC.miRv21.

Formato:
    Un DataFrame de Pandas con dos columnas:
    - 'miRNA_v21': Nombres de los miRNAs en la versión miRBase v21.
    - 'predicted_target': Genes mRNA predichos como objetivos de los miRNAs.

Referencias:
    Agarwal, V.; Bell, G. W.; Nam, J.-W. & Bartel, D. P.
    "Predicting effective microRNA target sites in mammalian mRNAs"
    eLife, eLife Sciences Publications, Ltd, 2015, 4.
    https://www.targetscan.org
"""
import pandas as pd

# Cargar los datos de miRNAs y sus genes objetivo predichos desde un archivo CSV
TScan = pd.read_csv('APPLICATION_PTC\DATA\TScan.csv')

# Mostrar la estructura básica del dataset
print(TScan.shape)
print(TScan.head())
