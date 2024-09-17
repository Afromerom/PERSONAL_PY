from InterListtoMatrix import interlist_to_matrix
from GroundT import GroundT
def Confirmed_fromList(InterList, GroundT):
    # Eliminar valores nulos en InterList
    InterList = {k: v for k, v in InterList.items() if v is not None}

    # Nombres de los mRNA (las claves del diccionario)
    mRs = InterList.keys()

    # Lista vacía para almacenar las interacciones confirmadas
    ConfirmedL = {}

    # Bucle para cada mRNA
    for i in mRs:
        for j in InterList[i]:
            # Verificar si el miRNA está en GroundT para el mRNA dado
            if j in GroundT.get(i, []):
                # Añadir el miRNA confirmado a la lista
                if i not in ConfirmedL:
                    ConfirmedL[i] = [j]
                else:
                    ConfirmedL[i].append(j)

    return ConfirmedL