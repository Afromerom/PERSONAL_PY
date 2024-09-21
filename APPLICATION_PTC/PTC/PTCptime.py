import numpy as np
import pandas as pd

def PTC_ptime(matchedData, VIM):
    # Calcular el orden de VIM_Time
    VIM_Time = np.argsort(VIM)

    # Reordenar las filas de las matrices en matchedData según VIM_Time
    matchedData[0] = matchedData[0].iloc[VIM_Time, :]
    matchedData[1] = matchedData[1].iloc[VIM_Time, :]

    return matchedData
