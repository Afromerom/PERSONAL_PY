def extract_parents(ptc_outcome, predictors):
    """
    Utiliza los resultados de PTC.GeneSel y PTC.TestInvariance para crear una lista de todos
    los mRNAs en Predictors con al menos un padre causal.

    :param ptc_outcome: Un diccionario que contiene los resultados de la función PTC.TestInvariance.
                        Cada elemento del diccionario debe tener la siguiente estructura:
                        {'name': nombre_mRNA, 'data': índices que indican la posición de los miRNAs inferidos en el vector de padres plausibles}.
    :param predictors: Un diccionario que contiene el conjunto de miRNAs que se usarán como predictores
                       (padres plausibles) de cada mRNA, obtenido de PTC.GeneSel.
    :return: Un diccionario con 3 elementos:
             - 'Index': Índices de miRNAs inferidos como padres causales de cada mRNA.
             - 'Names': Un diccionario donde cada elemento corresponde a un mRNA y contiene
                        los nombres de los miRNAs inferidos como padres causales de ese mRNA.
             - 'genes': Nombres de todos los mRNAs con al menos un padre inferido por PTC.
    """
    
    # Filtrar los mRNAs que tienen al menos un padre causal inferido
    pp = {k: len(v) > 0 for k, v in ptc_outcome.items()}

    # Obtener los índices de mRNAs con al menos un padre inferido
    pp_index = [i for i, v in enumerate(pp.values()) if v]
    
    # Filtrar los mRNAs en PTC.outcome usando los índices obtenidos
    filtered_ptc_outcome = {k: ptc_outcome[k] for k in pp if pp[k]}
    
    # Inicializar un diccionario para almacenar los nombres de los miRNAs inferidos como padres
    names = {}
    
    # Iterar sobre los mRNAs filtrados
    for i in filtered_ptc_outcome:
        # Asignar los nombres de los miRNAs inferidos a cada mRNA
        names[i] = [predictors[i][index] for index in filtered_ptc_outcome[i]]
    
    # Retornar el resultado como un diccionario con 'Index', 'Names', y 'genes'
    return {
        'Index': filtered_ptc_outcome,
        'Names': {k: v for k, v in names.items() if v},  # Eliminar cualquier entrada nula en 'Names'
        'genes': list(filtered_ptc_outcome.keys())
    }
