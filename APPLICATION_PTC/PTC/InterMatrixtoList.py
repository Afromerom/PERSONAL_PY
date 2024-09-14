import numpy as np
def intermatrix_to_list(inter_matrix):
    """
    Dada una matriz que contiene interacciones miRNA-mRNA, crea un diccionario donde cada
    elemento corresponde a un mRNA y contiene los miRNAs relacionados con ese mRNA.

    :param inter_matrix: Una matriz de dos columnas que contiene relaciones miRNA-mRNA.
                         La primera columna corresponde a los miRNAs y la segunda a los mRNAs.
    :return: Un diccionario donde cada clave es un nombre de mRNA y el valor es una lista de
             los nombres de los miRNAs asociados a ese mRNA.
    """
    
    # Eliminar cualquier fila con valores faltantes (NaN) de la matriz
    inter_matrix = inter_matrix[~np.isnan(inter_matrix).any(axis=1)]
    
    # Obtener la lista única de mRNAs de la segunda columna de inter_matrix
    unique_mrnas = np.unique(inter_matrix[:, 1])
    
    # Inicializar un diccionario para almacenar las relaciones mRNA-miRNA
    inter_list = {}
    
    # Iterar sobre cada mRNA único
    for mRNA in unique_mrnas:
        # Encontrar los índices donde el mRNA coincide en la segunda columna
        indexes = np.where(inter_matrix[:, 1] == mRNA)[0]
        # Obtener los miRNAs correspondientes a esos índices en la primera columna
        inter_list[mRNA] = inter_matrix[indexes, 0].tolist()
    
    return inter_list

# # Ejemplo de uso
# inter_matrix_example = np.array([
#     ["miRNA1", "mRNA1"],
#     ["miRNA2", "mRNA1"],
#     ["miRNA3", "mRNA2"],
#     # Agregar más interacciones aquí
# ])

inter_list = intermatrix_to_list(intermatrix_to_list)
print(inter_list)
