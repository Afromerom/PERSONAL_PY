"""
TS7.0_Conserved_Site_Context_Scores: TargetScan 7.0 Conserved Site Context Scores

Descripción:
    Este archivo contiene una matriz con los puntajes de contexto conservado (Context++) y contribuciones
    para todos los sitios de miRNA conservados, descargados de TargetScan 7.0.

Formato:
    Un DataFrame de Pandas con los datos de los puntajes de contexto conservado de TargetScan 7.0.

Referencias:
    Agarwal, V.; Bell, G. W.; Nam, J.-W. & Bartel, D. P.
    "Predicting effective microRNA target sites in mammalian mRNAs"
    eLife, eLife Sciences Publications, Ltd, 2015, 4.
    https://www.targetscan.org/cgi-bin/targetscan/data_download.cgi?db=vert_70
"""
import pandas as pd

# Cargar los datos de puntajes de contexto conservado de TargetScan desde un archivo CSV
TS7_0_Conserved_Site_Context_Scores = pd.read_csv('APPLICATION_PTC\DATA\TS7.0_Conserved_Site_Context_Scores.csv')

# Mostrar la estructura básica del dataset
print(TS7_0_Conserved_Site_Context_Scores.shape)
print(TS7_0_Conserved_Site_Context_Scores.head())
