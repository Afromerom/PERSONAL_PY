import pandas as pd
from PTCmiRv21 import PTC_miRv21
def PTC_RankByContext(TS70context, relationshipsM):

    # Verificación de las columnas de relationshipsM
    if relationshipsM.shape[1] == 2:
        relationshipsM.columns = ["miR", "mR"]
    else:
        raise ValueError("relationshipsM debe ser una matriz con 2 columnas [miR, mR]")

    # Convertir los nombres de miRNAs a la versión miRBase v.21
    TS70context["miRNA"] = PTC_miRv21(TS70context["miRNA"])

    # Obtener los índices que coinciden entre TS70context y relationshipsM
    indexes = relationshipsM.apply(
        lambda x: TS70context[
            (TS70context["miRNA"] == x["miR"]) &
            (TS70context["Gene.Symbol"] == x["mR"])
        ].index.tolist(),
        axis=1
    )

    # Calcular la puntuación media para cada par miRNA-mRNA
    scores = [
        TS70context.loc[idx, "context...score"].mean() if idx else float('nan')
        for idx in indexes
    ]

    # Agregar los puntajes a la matriz de relaciones
    relationshipsM["Score"] = scores

    # Ordenar la matriz de relaciones por puntaje de manera descendente
    relationshipsM = relationshipsM.sort_values(by="Score", ascending=False).reset_index(drop=True)

    # Asignar rangos
    relationshipsM.insert(0, "Rank", range(1, len(relationshipsM) + 1))

    return relationshipsM