import numpy as np
from itertools import combinations
from seqICP import seqICP_s  # Asumiendo que tienes una implementación de seqICP.s en Python

def ptc_test_invariance(Y, X, ngrid=2, alpha=0.02, explore_all=True, silent=True, complements=True):
    """
    Encuentra un conjunto de miRNAs (predictores) que son padres causales de un gen objetivo.
    Este conjunto se define como la unión de conjuntos que son invariantes. La invarianza se
    determina utilizando la prueba desacoplada de seqICP.

    :param Y: Vector [nx1] que contiene la expresión génica secuencial de un gen objetivo Y.
    :param X: Matriz [nxp] que contiene la expresión génica secuencial de los padres plausibles (miRNAs).
    :param ngrid: Número de segmentos de la serie temporal utilizados para crear los entornos necesarios para la prueba estadística (por defecto 2).
    :param alpha: Nivel de significancia para la prueba estadística (por defecto 0.02).
    :param explore_all: Si es True, se exploran todas las combinaciones de predictores. Si es False, se detiene después de encontrar el primer conjunto invariante (por defecto True).
    :param silent: Si es True, no se muestra información durante la ejecución (por defecto True).
    :param complements: Si es True, cada entorno se compara contra su complemento (por defecto True).
    :return: Un diccionario con los índices de los padres inferidos por PTC.
    """

    test = "decoupled"
    X = np.array(X)

    # Parámetros para el test
    par_test = {
        "grid": np.linspace(0, X.shape[0], ngrid + 1, dtype=int),
        "complements": complements,
        "link": sum,
        "alpha": alpha,
        "B": 100
    }

    model = "iid"
    par_model = {"pknown": False, "p": 0, "max.p": 10}

    finish = False
    p = X.shape[1]

    S_union = set()
    aux = p
    model_rejected = True

    if isinstance(Y, dict):
        Y = np.array(list(Y.values())).reshape(-1, 1)

    while not finish:
        # Generar combinaciones de predictores
        sets = list(combinations(range(p), aux))

        # Eliminar subconjuntos ya evaluados en la unión actual
        if len(S_union) > 0:
            sets_to_remove = list(combinations(S_union, aux))
            if not silent:
                print(f" (PTC) nSets to REMOVE in current level = {{ {len(sets_to_remove)} }}")

            sets = [s for s in sets if s not in sets_to_remove]

        n_sets = len(sets)
        if not silent:
            print(f" (PTC) nSets to explore in current level = {{ {n_sets} }}")

        for current_set in sets:
            if not silent:
                print(f" Current evaluated set  = {{ {current_set} }}")

            res = seqICP_s(X, Y, list(current_set), test, par_test, model, par_model)
            if res['p_value'] > par_test['alpha']:
                model_rejected = False
                S_union.update(current_set)
                if not silent:
                    print(f" Accepted set  = {{ {current_set} }}")
                if not explore_all:
                    finish = True
                    break

            if len(S_union) == p:
                finish = True
                break

        aux -= 1
        if aux == 0:
            finish = True

    if not model_rejected:
        if not silent:
            print(f"{Y.columns[0]} PTC.findParents  = {{ {S_union} }}")
    else:
        S_union = set()
        print("----------------------PTC.findParents MODEL REJECTED------------------------")

    Parents = {Y.columns[0]: S_union}

    return Parents

# Ejemplo de uso
# Y = np.array([...])  # Vector de expresión génica del gen objetivo
# X = np.array([...])  # Matriz de expresión génica de los padres plausibles
# result = ptc_test_invariance(Y, X)
# print(result)
