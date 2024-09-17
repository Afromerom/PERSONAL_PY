import numpy as np
import pandas as pd

def MAD(data):
    """Calcular la Desviación Absoluta Mediana (MAD)"""
    median = np.median(data, axis=0)
    mad = np.median(np.abs(data - median), axis=0)
    return mad

def FSbyMAD(data, value):
    """Seleccionar las 'value' columnas con mayor MAD"""
    mad_values = MAD(data)
    # Ordenar por MAD y seleccionar las 'value' mayores
    top_columns = np.argsort(mad_values)[-value:]
    return data[:, top_columns]

def getDatabyMAD(seqData, nmiR, nmR):
    # Seleccionar miRNAs usando MAD
    miRNAsData = FSbyMAD(seqData['miRs'].T, nmiR)
    miRs = seqData['miRs'].columns[miRNAsData.T.shape[1]]

    # Seleccionar mRNAs usando MAD
    mRNAsData = FSbyMAD(seqData['mRNAs'].T, nmR)
    mRNAsData = mRNAsData[:, ~pd.DataFrame(mRNAsData).duplicated().values]
    mRs = seqData['mRNAs'].columns[mRNAsData.T.shape[1]]

    # Combinar datos
    d = np.hstack([miRNAsData, mRNAsData])
    result = {'d': d, 'miRs': miRs, 'mRs': mRs}
    
    return result
