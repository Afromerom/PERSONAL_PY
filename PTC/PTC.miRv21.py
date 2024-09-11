import re
import pandas as pd

def ptc_mirv21(miRs, miRNA_converter):
    """
    Toma un vector que contiene los nombres de miRNAs y devuelve
    la versión de miRBase v21 de los mismos.

    :param miRs: Nombres de miRNAs que se van a cambiar a la versión miRBase v21.
    :param miRNA_converter: Una función o mapa que convierte los miRNAs a la versión miRBase v21.
    :return: Un vector con los nombres de los miRNAs en la versión miRBase v21.
    """
    
    # Remover cualquier sufijo después del punto en los nombres de los miRNAs
    miRs = [re.sub(r"\..*", "", miR) for miR in miRs]

    # Convertir los nombres de miRNAs a la versión v21 utilizando la función o mapa miRNA_converter
    aux = miRNA_converter(miRs, target_version="v21", exact=True, verbose=True)

    # Verificar si alguna conversión falló
    na_index = [idx for idx, x in enumerate(aux[:, 1]) if pd.isna(x)]

    # Recuperar los nombres originales de los miRNAs que no se pudieron convertir
    if len(na_index) > 0:
        print(f"{len(na_index)} conversions failed, original name is kept")
        for idx in na_index:
            aux[idx, 1] = miRs[idx]

    # Si hay múltiples coincidencias de miRNAs, seleccionar solo la primera
    aux[:, 1] = [re.sub(r"\&.*", "", miR) for miR in aux[:, 1]]

    # Devolver los miRNAs convertidos a la versión v21
    miRs_v21 = aux[:, 1]
    
    return miRs_v21

# Función placeholder para convertir los nombres de los miRNAs (esto debe ser reemplazado por la lógica real)
def miRNA_converter(miRs, target_version="v21", exact=True, verbose=True):
    # Este es solo un placeholder que representa una función o mapa que convierte los nombres de los miRNAs.
    # Debes reemplazar esto con una implementación que realice la conversión a miRBase v21.
    return pd.DataFrame({
        0: miRs,
        1: [miR + "_v21" for miR in miRs]  # Simula la conversión agregando "_v21" a cada miRNA
    }).values

# Ejemplo de uso
# miRs = ["miRNA1", "miRNA2.1", "miRNA3"]
# miRnames_v21 = ptc_mirv21(miRs, miRNA_converter)
# print(miRnames_v21)
