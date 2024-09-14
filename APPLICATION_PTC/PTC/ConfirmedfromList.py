
def confirmed_from_list(inter_list, ground_t):
    """
    Devuelve una lista con todas las interacciones experimentalmente confirmadas
    inferidas por PTC.

    :param inter_list: Un diccionario donde cada elemento tiene la siguiente estructura:
                       {'name': nombre_mRNA, 'data': nombres_de_miRNAs_inferidos_como_padres}
    :param ground_t: Un diccionario donde cada elemento tiene la siguiente estructura:
                     {'name': nombre_mRNA, 'data': nombres_de_miRNAs_cuya_interaccion_con_mRNA_ha_sido_confirmada_experimentalmente}
    :return: Un diccionario donde cada elemento tiene la siguiente estructura:
             {'name': nombre_mRNA_con_al_menos_una_interacción_confirmada, 
              'data': nombres_de_miRNAs_cuya_interaccion_esta_en_ground_t}
    """
    
    # Eliminar cualquier valor nulo de la lista inter_list
    inter_list = {k: v for k, v in inter_list.items() if v is not None}
    
    # Crear una lista para almacenar las interacciones confirmadas
    confirmed_l = {}

    # Iterar sobre cada mRNA en inter_list
    for i in inter_list:
        # Iterar sobre cada miRNA inferido en la lista de ese mRNA
        for j in inter_list[i]:
            # Verificar si el miRNA está en la lista de ground_t para ese mRNA
            if j in ground_t.get(i, []):
                # Si no hay una entrada en confirmed_l para ese mRNA, crearla
                if i not in confirmed_l:
                    confirmed_l[i] = [j]
                else:
                    # Si ya existe, agregar el miRNA a la lista
                    confirmed_l[i].append(j)

    return confirmed_l
