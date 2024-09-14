"""
wandTime.csv: Pseudotime obtenido mediante Wanderlust

Descripción:
    Este archivo contiene el pseudotiempo obtenido utilizando el algoritmo Wanderlust 
    (Bendall et al.) sobre el conjunto de datos `SC_mRNAsdata`. Los parámetros utilizados
    fueron: k=4, l=2, ng=2 y snn=0.

Formato:
    Un DataFrame de Pandas con 1 fila y 19 columnas, que representa el pseudotiempo 
    calculado con Wanderlust.

Referencias:
    Cifuentes-Bernal, A. M., Pham, V. H., Li, X., Liu, L., Li, J., & Le, T. D.
    "A Pseudo-Temporal Causality Approach to Identifying miRNA-mRNA Interactions During Biological Processes."
    bioRxiv, 2020. https://doi.org/10.1101/2020.07.07.192724

    Wang, N., Zheng, J., Chen, Z. et al.
    "Single-cell microRNA-mRNA co-sequencing reveals non-genetic heterogeneity and mechanisms of microRNA regulation."
    Nat Commun 10, 95 (2019). https://doi.org/10.1038/s41467-018-07981-6

    Bendall SC, Davis KL, Amir el-AD, et al.
    "Single-cell trajectory detection uncovers progression and regulatory coordination in human B cell development."
    Cell. 2014;157(3):714-725. https://doi.org/10.1016/j.cell.2014.04.005
"""
import pandas as pd

# Cargar el archivo wandTime.csv
wandTime = pd.read_csv('APPLICATION_PTC\DATA\wandTime.csv', header=None)

# Mostrar la estructura del dataset
print(wandTime.shape)
print(wandTime)
