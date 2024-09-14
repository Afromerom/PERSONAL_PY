import numpy as np
import pandas as pd
from PTCptime import ptc_ptime
from getDatabyMAD import get_data_by_mad
from PTCTestInvariance import ptc_test_invariance
from ExtractParents import extract_parents
from InterListtoMatrix import interlist_to_matrix
from PTCRankByContext import ptc_rank_by_context


def ptc(miRNAs, mRNAs, VIM, nmiR=30, nmR=1500, ngrid=2, alpha=0.02, complements=True, explore_all=True, silent=True, TScan=None):
    # Transformar los nombres de mRNAs a mayúsculas
    mRNAs.columns = mRNAs.columns.str.upper()

    # Cargar los puntajes de contexto conservado de TargetScan 7.0 si no se proporciona TScan
    if TScan is None:
        TScan = pd.read_csv('APPLICATION_PTC/PTC/TScan.py')  # Ruta al archivo TScan predicho de miRNA-mRNA

    # Pseudotiempo de los datos de expresión
    seqData = ptc_ptime({'miRs': miRNAs, 'mRNAs': mRNAs}, VIM)
    
    # Seleccionar los miRNAs y mRNAs más significativos usando la Mediana de Desviación Absoluta (MAD)
    SelData = get_data_by_mad(seqData, nmiR=nmiR, nmR=nmR)
    
    # Inicializar un diccionario para almacenar los resultados
    PTC_outcome = {}
    
    # Para cada mRNA, estimar las interacciones causales con miRNAs
    for gene in SelData['mRs']:
        temp = SelData['PParents'][gene]
        X_TScan = SelData['d'][:, temp]
        
        if len(X_TScan) > 0:
            if not silent:
                print(f" Current mRNA = {gene}")
            np.random.seed(1)
            try:
                PTC_outcome[gene] = ptc_test_invariance(Y=SelData['d'][:, gene], X=X_TScan, ngrid=ngrid, alpha=alpha, explore_all=explore_all, silent=silent, complements=complements)
            except Exception as e:
                print(f"Error en la inferencia para {gene}: {str(e)}")
    
    # Extraer los padres causales de cada mRNA
    Results = extract_parents(PTC_outcome, SelData['PParents'])
    
    # Calcular la clasificación de las interacciones usando los puntajes de TargetScan
    Results['Summary'] = interlist_to_matrix(Results['Names'])
    TS7_0_Conserved_Site_Context_Scores = pd.read_csv('APPLICATION_PTC/PTC/TS7_0_Conserved_Site_Context_Scores.py')
    Results['Summary'] = ptc_rank_by_context(TS7_0_Conserved_Site_Context_Scores, Results['Summary'])
    
    return Results

# Funciones auxiliares necesarias:
# - ptc_ptime
# - get_data_by_mad
# - ptc_test_invariance
# - extract_parents
# - interlist_to_matrix
# - ptc_rank_by_context

# Ejemplo de uso
# miRNAs = pd.DataFrame(np.random.rand(500, 30))  # Ejemplo de datos de miRNAs
# mRNAs = pd.DataFrame(np.random.rand(500, 1500))  # Ejemplo de datos de mRNAs
# VIM = np.random.rand(500)  # Ejemplo de pseudotiempo
# result = ptc(miRNAs, mRNAs, VIM)
# print(result)
