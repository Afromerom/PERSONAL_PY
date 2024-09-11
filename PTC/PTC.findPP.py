def ptc_find_pp(tscan=None, miRs=None, mRs=None):
    """
    Dado un vector de nombres de miRNAs y un vector de nombres de mRNAs,
    crea un conjunto de miRNAs (padres plausibles) que pueden dirigirse biológicamente a esos mRNAs,
    según lo predicho por TargetScan.

    :param tscan: Una matriz que contiene interacciones miRNA-mRNA predichas por TargetScan.
                  Si es None, se debe cargar un archivo predefinido con las interacciones de TargetScan 7.0.
    :param miRs: Un vector que contiene los nombres de miRNAs a verificar. Estos nombres
                 corresponden a los candidatos a predictores.
    :param mRs: Un vector que contiene los nombres de mRNAs a verificar. Estos nombres
                corresponden a los genes objetivo (variables de respuesta).
    :return: Un diccionario donde cada clave es un mRNA y cada valor es un conjunto de miRNAs
             que pueden unirse a ese mRNA.
    """

    if tscan is None:
        # Si tscan no está proporcionado, se debe cargar el archivo predefinido de TargetScan
        raise ValueError("TargetScan data (tscan) must be provided.")
    
    # Inicializar el diccionario para almacenar los padres plausibles
    p_parents = {mR: [] for mR in mRs}

    # Iterar sobre cada mRNA en la lista de mRs
    for i in mRs:
        # Encontrar los índices donde el mRNA en TargetScan es igual a 'i'
        index_miRs = [idx for idx, x in enumerate(tscan[:, 1]) if x == i]

        if len(index_miRs) > 0:
            # Obtener los miRNAs correspondientes a esos índices en la columna 1
            temp = tscan[index_miRs, 0]

            # Iterar sobre cada miRNA en la lista de miRs
            for j in miRs:
                if j in temp:
                    # Añadir el miRNA al conjunto de padres plausibles si coincide
                    p_parents[i].append(j)

    return p_parents

# Ejemplo de uso
# tscan = np.array([["miRNA1", "mRNA1"], ["miRNA2", "mRNA1"], ["miRNA3", "mRNA2"]])
# miRs = ["miRNA1", "miRNA2"]
# mRs = ["mRNA1", "mRNA2"]
# p_parents = ptc_find_pp(tscan, miRs, mRs)
# print(p_parents)
