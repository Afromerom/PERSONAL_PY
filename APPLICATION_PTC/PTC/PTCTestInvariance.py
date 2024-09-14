import numpy as np
from itertools import combinations

def ptc_test_invariance(Y, X, ngrid=2, alpha=0.02, explore_all=True, silent=True, complements=True):
    """
    PTC Test Invariance: Encuentra un conjunto de miRNAs (predictores) que son padres causales
    de un gen objetivo. Este conjunto se define como la unión de conjuntos que son invariantes.

    :param Y: Vector (nx1) que contiene la expresión génica secuencial del gen objetivo (mRNA).
    :param X: Matriz (nxp) que contiene la expresión génica secuencial de p padres plausibles (miRNAs).
    :param ngrid: Número de segmentos de la serie temporal (por defecto 2).
    :param alpha: Nivel de significancia para el test estadístico (por defecto 0.02).
    :param explore_all: Si es True, explora todas las combinaciones de predictores (por defecto True).
    :param silent: Si es True, muestra los conjuntos evaluados actualmente (por defecto True).
    :param complements: Si es True, compara cada entorno con su complemento (por defecto True).
    :return: Diccionario con los índices de los padres inferidos para el gen objetivo.
    """

    # Parámetros para el test de independencia
    par_test = {
        'grid': np.linspace(0, X.shape[0], ngrid + 1, dtype=int),
        'complements': complements,
        'link': sum,
        'alpha': alpha,
        'B': 100
    }

    # Inicialización de variables
    finish = False
    p = X.shape[1]  # Número de predictores (miRNAs)
    S_Union = []
    aux = p
    model_rejected = True

    # Convertir Y a una matriz si es una lista
    if isinstance(Y, list):
        Y = np.array(Y)

    while not finish:
        # Generar todas las combinaciones de tamaño 'aux' de predictores
        Sets = np.array(list(combinations(range(p), aux)))

        # Eliminar subconjuntos que ya están en S_Union
        if len(S_Union) > 0:
            sets_to_remove = np.array(list(combinations(S_Union, aux)))
            if not silent:
                print(f"(PTC) nSets to REMOVE in current level = {len(sets_to_remove)}")

            for remove_set in sets_to_remove:
                Sets = np.array([s for s in Sets if not np.array_equal(np.intersect1d(s, remove_set), remove_set)])

        nSets = len(Sets)
        if not silent:
            print(f"(PTC) nSets to explore in current level = {nSets}")

        # Evaluar cada conjunto de predictores
        for s in Sets:
            if not silent:
                print(f"Current evaluated set = {s}")

            res = seqICP_s(X, Y, s, test="decoupled", par_test=par_test, model="iid")

            # Verificar si el modelo es aceptado
            if res["p_value"] > alpha:
                model_rejected = False
                S_Union = np.union1d(S_Union, s).tolist()
                if not silent:
                    print(f"Accepted set = {s}")

                # Si no se desea explorar todo, terminar después de la primera aceptación
                if not explore_all:
                    finish = True
                    break

        if len(S_Union) == p:
            finish = True

        aux -= 1
        if aux == 0:
            finish = True

    # Verificar si el modelo fue rechazado
    if not model_rejected:
        print(f"PTC.findParents = {S_Union}")
    else:
        S_Union = []
        print("----------------------PTC.findParents MODEL REJECTED------------------------")

    return {"Parents": S_Union}

# Función de prueba (secuencial ICP) para simular el resultado, puedes sustituirla con una implementación real
def seqICP_s(X, Y, set_indices, test, par_test, model):
    """
    Simulación de la función seqICP.s, usada para pruebas de independencia en conjuntos de predictores.
    Aquí se debe implementar un test adecuado según el enfoque que se esté utilizando.
    """
    # Esto es solo una simulación que siempre acepta el conjunto. En una implementación real,
    # se realizaría el test de independencia de predictores.
    return {"p_value": np.random.rand()}  # Simulación con un p-valor aleatorio
