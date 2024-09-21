import pandas as pd

def InterMatrix_toList(InterMatrix):
    # Convertir la matriz a un DataFrame de Pandas
    df = pd.DataFrame(InterMatrix, columns=['miR', 'mR'])

    # Eliminar filas con valores NA
    df = df.dropna()

    # Obtener los mRNAs únicos
    unique_mRs = df['mR'].unique()

    # Crear un diccionario para almacenar los miRNAs asociados a cada mRNA
    InterList = {mR: [] for mR in unique_mRs}

    # Asignar los miRNAs a cada mRNA en el diccionario
    for mR in unique_mRs:
        InterList[mR] = df[df['mR'] == mR]['miR'].tolist()

    return InterList