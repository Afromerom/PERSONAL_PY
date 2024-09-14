import numpy as np
import pandas as pd

def interlist_to_matrix(InterList):
    """
    Convierte una lista de interacciones miRNA-mRNA en una matriz donde cada fila representa una interacción.
    
    :param InterList: Diccionario donde cada clave es un mRNA y el valor es una lista de miRNAs que interactúan con él.
    :return: DataFrame con dos columnas: la primera contiene los miRNAs, la segunda contiene los mRNAs.
    """
    
    # Eliminar elementos NaN en la lista
    InterList = {key: value for key, value in InterList.items() if value is not None}
    
    # Crear una lista para almacenar las filas de la matriz
    rows = []
    
    # Recorrer el diccionario para llenar la matriz
    for mR, miRs in InterList.items():
        for miR in miRs:
            rows.append([miR, mR])
    
    # Convertir la lista de filas en un DataFrame de pandas con las columnas 'miR' y 'mR'
    InterMatrix = pd.DataFrame(rows, columns=['miR', 'mR'])
    
    return InterMatrix

# # Ejemplo de uso
# # InterList es un diccionario con mRNAs como claves y listas de miRNAs como valores
# InterList = {
#     'mRNA1': ['miRNA1', 'miRNA2'],
#     'mRNA2': ['miRNA3'],
#     'mRNA3': ['miRNA1', 'miRNA4']
# }

# Convertir la lista a una matriz (DataFrame)
InterMatrix = interlist_to_matrix(InterList)
print(InterMatrix)
