import numpy as np

def confirmed_from_matrix(inter_matrix, ground_t):
    """
    Dada una matriz con interacciones miRNA-mRNA, devuelve una matriz con todas
    aquellas interacciones que están presentes en ground_t.

    :param inter_matrix: Una matriz que contiene interacciones miRNA-mRNA.
                         La primera columna corresponde a miRNAs y la segunda a mRNAs.
    :param ground_t: Un diccionario donde cada clave es el nombre de un mRNA y el valor
                     es una lista de miRNAs cuya interacción con el mRNA ha sido confirmada.
    :return: Una matriz que contiene todas las interacciones en inter_matrix que están en ground_t.
    """
    
    # Inicializar una lista para almacenar las interacciones confirmadas
    confirmed = []
    
    # Obtener la lista única de miRNAs de la primera columna de inter_matrix
    miRs = np.unique(inter_matrix[:, 0])
    
    # Iterar sobre cada miRNA
    for i in miRs:
        # Encontrar los índices de inter_matrix donde la primera columna (miRNA) coincide con 'i'
        indexes = np.where(inter_matrix[:, 0] == i)[0]
        # Obtener los mRNAs correspondientes a esos índices
        mRs = inter_matrix[indexes, 1]
        
        # Iterar sobre cada mRNA asociado al miRNA actual
        for j in mRs:
            # Verificar si el miRNA está en la lista de ground_t para ese mRNA
            if j in ground_t and i in ground_t[j]:
                # Si es así, agregar la interacción a la lista de confirmados
                confirmed.append([i, j])
    
    # Convertir la lista de confirmados en una matriz de numpy
    confirmed_matrix = np.array(confirmed)
    
    return confirmed_matrix
