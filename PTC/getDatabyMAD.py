import numpy as np
import pandas as pd

def fs_by_mad(data, n):
    """
    Selecciona las n filas con la mayor Mediana de Desviación Absoluta (MAD).
    
    :param data: Matriz de datos donde las filas son genes (miRNAs o mRNAs) y las columnas son muestras.
    :param n: Número de genes a seleccionar.
    :return: Una matriz de datos con las n filas seleccionadas.
    """
    # Calcular la Mediana de Desviación Absoluta para cada fila
    mad_values = np.median(np.abs(data - np.median(data, axis=1, keepdims=True)), axis=1)
    
    # Obtener los índices de las n filas con la mayor MAD
    top_indices = np.argsort(mad_values)[-n:]
    
    # Seleccionar las filas correspondientes
    return data[top_indices, :]

def get_data_by_mad(seq_data, nmiR, nmR):
    """
    Dado un conjunto de datos de expresión génica que incluye miRNAs y mRNAs combinados, 
    encuentra los nmiR miRNAs y los nmR mRNAs con la mayor Mediana de Desviación Absoluta (MAD).
    
    :param seq_data: Diccionario que contiene dos elementos: 'miRs' (datos de miRNAs) y 'mRNAs' (datos de mRNAs).
    :param nmiR: Número de miRNAs a seleccionar basados en MAD.
    :param nmR: Número de mRNAs a seleccionar basados en MAD.
    :return: Un diccionario con tres elementos:
             - 'd': Matriz de datos combinados de miRNAs y mRNAs seleccionados.
             - 'miRs': Los nombres de los miRNAs seleccionados.
             - 'mRs': Los nombres de los mRNAs seleccionados.
    """
    
    # Seleccionar los miRNAs significativos utilizando MAD
    miRNAs_data = fs_by_mad(seq_data['miRs'].T, nmiR)
    
    # Obtener los nombres de los miRNAs seleccionados
    miRs = seq_data['miRs'].columns
    
    # Seleccionar los mRNAs significativos utilizando MAD
    mRNAs_data = fs_by_mad(seq_data['mRNAs'].T, nmR)
    
    # Eliminar datos duplicados (columnas repetidas)
    mRNAs_data = pd.DataFrame(mRNAs_data).T.drop_duplicates().values
    
    # Obtener los nombres de los mRNAs seleccionados
    mRs = seq_data['mRNAs'].columns
    
    # Combinar los datos de miRNAs y mRNAs
    d = np.hstack((miRNAs_data, mRNAs_data))
    
    # Crear el diccionario de salida
    result = {
        'd': d,
        'miRs': miRs,
        'mRs': mRs
    }
    
    return result

# Ejemplo de uso
# seq_data = {
#     'miRs': pd.DataFrame(np.random.rand(1000, 30)),  # Ejemplo de datos de miRNAs
#     'mRNAs': pd.DataFrame(np.random.rand(5000, 30))  # Ejemplo de datos de mRNAs
# }
# nmiR = 30
# nmR = 1500
# result = get_data_by_mad(seq_data, nmiR, nmR)
# print(result['d'].shape)  # Combinación de miRNAs y mRNAs seleccionados
