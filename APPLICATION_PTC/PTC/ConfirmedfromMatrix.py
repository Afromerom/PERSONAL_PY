import numpy as np
from InterMatrixtoList import InterMatrixtoList
from GroundT import GroundT 

def Confirmed_fromMatrix(InterMatrix, GroundT):
    # Inicializamos una lista vacía para almacenar las interacciones confirmadas
    Confirmed = []
    
    # Obtenemos los miRNAs únicos de la primera columna de InterMatrix
    miRs = np.unique(InterMatrix[:, 0])
    
    # Bucle para cada miRNA
    for i in miRs:
        # Encuentra los índices en InterMatrix donde el miRNA es igual a 'i'
        indexes = np.where(InterMatrix[:, 0] == i)[0]
        
        # Obtiene los mRNAs correspondientes
        mRs = InterMatrix[indexes, 1]
        
        # Para cada mRNA, verifica si la interacción está en GroundT
        for j in mRs:
            if i in GroundT.get(j, []):
                Confirmed.append([i, j])  # Añadimos la interacción confirmada
                
    # Convertimos la lista a un array NumPy para devolver el resultado en formato de matriz
    return np.array(Confirmed)
