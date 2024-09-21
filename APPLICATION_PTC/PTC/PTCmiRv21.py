import re
def PTC_miRv21(miRs):
    # Eliminar cualquier parte del nombre después de un punto
    miRs = [re.sub(r"\..*", "", miR) for miR in miRs]
    
    # Diccionario de conversiones, a sustituir con un método real para conversión
    conversion_dict = {
        'miR-1': 'miR-1-3p',
        'miR-2': 'miR-2-5p',
        # Añadir más conversiones según miRBase v.21
    }

    # Convertir los nombres de miRNAs usando el diccionario
    converted_miRs = [conversion_dict.get(miR, miR) for miR in miRs]

    # Manejo de conversiones fallidas (mantener el nombre original)
    failed_indices = [i for i, x in enumerate(converted_miRs) if x is None]
    if failed_indices:
        for i in failed_indices:
            converted_miRs[i] = miRs[i]

    # Seleccionar la primera coincidencia si hay múltiples
    converted_miRs = [re.sub(r"&.*", "", miR) for miR in converted_miRs]

    return converted_miRs
