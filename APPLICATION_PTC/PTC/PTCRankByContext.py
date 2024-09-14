import numpy as np
import pandas as pd

def ptc_rank_by_context(ts70_context, relationships_m):
    """
    Esta función utiliza los puntajes de contexto conservado de TS70 para clasificar
    una matriz de relaciones inferidas entre miRNA y mRNA.

    :param ts70_context: Una matriz que contiene los puntajes de contexto conservado del sitio de TS70.
                         Las cabeceras de la matriz de TargetScan deben ser conservadas cuando el archivo se importa.
    :param relationships_m: Una matriz de dos columnas que contiene los nombres de miRNAs y mRNAs.
                            La primera columna representa los miRNAs y la segunda columna los mRNAs.
    :return: Una matriz de relaciones con cuatro columnas [Rank, miRNA, mRNA, Score].
             Cuanto más negativo sea el puntaje, mejor será la clasificación del par miRNA-mRNA correspondiente.
    """

    if relationships_m.shape[1] == 2:
        relationships_m.columns = ["miR", "mR"]
    else:
        raise ValueError("relationshipsM debe ser una matriz con 2 columnas [miR, mR]")

    # Convertir los nombres de miRNAs a la versión v21
    ts70_context["miRNA"] = ptc_mirv21(ts70_context["miRNA"])

    # -------------------- Calcular los índices de los pares miRNA-mRNA en TS70context
    indexes = relationships_m.apply(lambda row: ts70_context[
        (ts70_context["miRNA"] == row["miR"]) & 
        (ts70_context["Gene.Symbol"] == row["mR"])
    ].index, axis=1)

    # -------- Calcular el puntaje como el promedio de los puntajes de contexto de cada par
    score = indexes.apply(lambda idx: ts70_context.loc[idx, "context++score"].mean() if len(idx) > 0 else np.nan)
    
    # Añadir la columna de puntajes a relationships_m
    relationships_m["Score"] = score

    # Ordenar las relaciones por puntaje de manera descendente
    relationships_m = relationships_m.sort_values(by="Score", ascending=False).reset_index(drop=True)

    # Añadir una columna de ranking
    relationships_m.insert(0, "Rank", range(1, len(relationships_m) + 1))

    return relationships_m

# Función auxiliar para convertir nombres de miRNAs a la versión v21 (placeholder)
def ptc_mirv21(miRNA_names):
    # Implementación de la conversión de nombres de miRNAs a la versión v21
    pass

# Ejemplo de uso
# ts70_context = pd.read_csv("ruta/al/archivo/TS70context.csv")
# relationships_m = pd.DataFrame({
#     "miR": ["miRNA1", "miRNA2", "miRNA3"],
#     "mR": ["mRNA1", "mRNA2", "mRNA3"]
# })
# ranked_relationships = ptc_rank_by_context(ts70_context, relationships_m)
# print(ranked_relationships)
