import numpy as np

def ptc_ptime(matched_data, VIM):
    """
    Ordena la expresión génica de acuerdo con el orden de VIM_Time.

    :param matched_data: Una lista con dos elementos:
                         - Una matriz de expresión génica de miRNAs (primer elemento).
                         - Una matriz de expresión génica de mRNAs (segundo elemento).
                         Las columnas representan miRNAs o mRNAs, y las filas representan muestras.
    :param VIM: Vector que contiene la expresión de VIM que se utilizará para ordenar las muestras.
    :return: Los datos ordenados en pseudotiempo basados en el orden de VIM_Time.
    """
    
    # Ordenar el índice de VIM
    VIM_Time = np.argsort(VIM)

    # Reordenar las filas de la matriz de miRNAs y mRNAs según el orden de VIM_Time
    matched_data[0] = matched_data[0][VIM_Time, :]
    matched_data[1] = matched_data[1][VIM_Time, :]

    return matched_data

# Ejemplo de uso
# miRNA_data = np.array([[1, 2], [3, 4], [5, 6]])  # Ejemplo de datos de expresión de miRNAs
# mRNA_data = np.array([[7, 8], [9, 10], [11, 12]])  # Ejemplo de datos de expresión de mRNAs
# VIM = np.array([2, 1, 3])  # Ejemplo de valores de VIM
# matched_data = [miRNA_data, mRNA_data]

# Time_series = ptc_ptime(matched_data, VIM)
# print(Time_series)
