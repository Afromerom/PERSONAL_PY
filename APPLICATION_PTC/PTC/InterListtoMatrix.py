import numpy as np

def InterList_toMatrix(InterList):
    # Eliminar elementos NA y None de InterList
    InterList = {k: v for k, v in InterList.items() if v is not None and not any([x is None for x in v])}
    
    # Contar el número total de interacciones
    total_interactions = sum(len(v) for v in InterList.values())
    
    # Inicializar la matriz de interacciones
    InterMatrix = np.empty((total_interactions, 2), dtype=object)
    
    # Rellenar la matriz con las interacciones miRNA-mRNA
    k = 0
    for mR, miRs in InterList.items():
        for miR in miRs:
            InterMatrix[k, 0] = miR
            InterMatrix[k, 1] = mR
            k += 1

    # Etiquetar columnas
    return np.array(InterMatrix, dtype=object)
