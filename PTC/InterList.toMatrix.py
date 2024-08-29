import numpy as np

def interlist_to_matrix(inter_list):
    """
    Dado un diccionario donde cada elemento es un mRNA que contiene el conjunto de miRNAs
    (padres) con los que ese mRNA puede interactuar, devuelve una matriz con las interacciones
    miRNA-mRNA. Cada fila representa una interacción. La primera columna contiene miRNAs y la
    segunda columna contiene mRNAs.

    :param inter_list: Un diccionario donde cada clave es un mRNA y cada valor es una lista de miRNAs.
    :return: Una matriz con 2 columnas que contiene las interacciones miRNA-mRNA.
    """
    
    # Filtrar elementos nulos o vacíos del diccionario
    inter_list = {k: v for k, v in inter_list.items() if v is not None and len(v) > 0}
    
    # Calcular el número total de interacciones
    total_interactions = sum(len(v) for v in inter_list.values())
    
    # Crear una matriz vacía para almacenar las interacciones
    inter_matrix = np.empty((total_interactions, 2), dtype=object)
    
    k = 0  # Contador para las filas de la matriz
    if len(inter_list) > 0:
        # Iterar sobre cada mRNA en el diccionario
        for mRNA, miRNAs in inter_list.items():
            # Iterar sobre cada miRNA asociado a ese mRNA
            for miRNA in miRNAs:
                inter_matrix[k, 0] = miRNA  # Primera columna: miRNA
                inter_matrix[k, 1] = mRNA   # Segunda columna: mRNA
                k += 1
    
    # Asignar nombres a las columnas de la matriz
    return inter_matrix

# Ejemplo de uso
inter_list_example = {
    "mRNA1": ["miRNA1", "miRNA2"],
    "mRNA2": ["miRNA3"],
    # Agregar más interacciones aquí
}

inter_matrix = interlist_to_matrix(inter_list_example)
print(inter_matrix)
