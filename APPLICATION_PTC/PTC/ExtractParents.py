
def Extract_Parents(PTC_outcome, Predictors):
    # Filtramos los elementos de PTC_outcome que tienen al menos un padre causal
    PP = {k: v for k, v in PTC_outcome.items() if len(v) > 0}
    
    # Inicializamos un diccionario para almacenar los nombres de los miRNAs padres causales
    Names = {}

    # Recorremos cada mRNA en PP para obtener los nombres de los miRNAs padres
    for i in PP:
        Names[i] = [Predictors[i][idx] for idx in PP[i]]

    # Devolvemos una lista con tres elementos
    return {
        'Index': PP,                   # Índices de los padres causales
        'Names': {k: v for k, v in Names.items() if v},  # Nombres de los miRNAs padres
        'genes': list(PP.keys())       # Nombres de los mRNAs con padres causales
    }
