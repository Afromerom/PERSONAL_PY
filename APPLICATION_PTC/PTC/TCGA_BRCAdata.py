"""
TCGA_BRCAdata: miRNA-mRNA matched bulk data from TCGA BRCA project

Descripción:
    Este archivo contiene los datos de expresión génica de 518 miRNAs y 17403 mRNAs
    provenientes de 503 muestras del proyecto TCGA BRCA (cáncer de mama).

Formato:
    Un objeto tipo diccionario o DataFrame de Pandas con dos elementos: 
    - 'miRs': Datos de expresión de 518 miRNAs.
    - 'mRNAs': Datos de expresión de 17403 mRNAs.

Referencias:
    Pham, V., Zhang, J., Liu, L. et al.
    "Identifying miRNA-mRNA regulatory relationships in breast cancer with invariant causal prediction."
    BMC Bioinformatics 20, 143 (2019).
    https://doi.org/10.1186/s12859-019-2668-x
"""
import pandas as pd

# Cargar los datos combinados de miRNAs y mRNAs desde archivos CSV (o similares)
miRs_data = pd.read_csv('APPLICATION_PTC\DATA\SC_miRNAsdata.csv')  # Datos de miRNAs
mRNAs_data = pd.read_csv('APPLICATION_PTC\DATA\SC_mRNAsdata.csv')  # Datos de mRNAs

# Crear un diccionario para representar los datos como el formato en R
TCGA_BRCAdata = {
    'miRs': miRs_data,
    'mRNAs': mRNAs_data
}

# Mostrar información básica de los datos de miRNAs y mRNAs
print(f"miRNAs data shape: {TCGA_BRCAdata['miRs'].shape}")  # (518, 503)
print(f"mRNAs data shape: {TCGA_BRCAdata['mRNAs'].shape}")  # (17403, 503)
