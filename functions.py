import pandas as pd
import math

def find_name_and_adjust_dataframe(df):
    # Función para buscar 'NAME' en el dataframe y ajustar el dataframe para eliminar filas y columnas hasta esa posición
    position = None  # Inicializa la variable 'position' para almacenar la posición de 'NAME' si se encuentra

    # Recorre cada fila del dataframe
    for row_idx in range(len(df)):
        # Recorre cada columna del dataframe en la fila actual
        for col_idx in range(len(df.columns)):
            # Verifica si el valor de la celda actual es 'NAME'
            if df.iat[row_idx, col_idx] == 'NAME':
                # Guarda la posición de la celda que contiene 'NAME'
                position = (row_idx, col_idx)
                break  # Sale del bucle de columnas
        if position:
            break  # Sale del bucle de filas si se encontró 'NAME'

    if not position:
        # Si 'NAME' no se encuentra en el dataframe, lanza un error
        raise ValueError("'NAME' no se encontró en el dataframe.")

    # Obtiene la posición de 'NAME' (fila y columna)
    row, col = position

    # Ajusta el dataframe eliminando las filas y columnas hasta 'NAME'
    df = df.iloc[row:, col:]

    return df  # Devuelve el dataframe ajustado

def transpose_csv(input_file):
    # Función para cargar un CSV, ajustar el dataframe, transponerlo

    # Carga el dataframe desde el archivo CSV
    df = pd.read_csv(input_file)

    # Verifica y ajusta el dataframe
    df = find_name_and_adjust_dataframe(df)

    if df.empty:
        # Si el dataframe está vacío después de ajustar, lanza un error
        raise ValueError("El dataframe está vacío después de eliminar filas y columnas.")

    # Transpone el dataframe
    df_transpuesto = df.transpose()

    # Elimina las filas que contienen solo un dato
    df_transpuesto = remove_single_value_rows(df_transpuesto)

    return df_transpuesto  # Devuelve el dataframe transpuesto

def get_transposed_dimensions(df_transpuesto):
    # Función para obtener la cantidad de filas y columnas del dataframe transpuesto
    num_rows = df_transpuesto.shape[0]  # Obtiene el número de filas
    num_cols = df_transpuesto.shape[1]  # Obtiene el número de columnas
    return num_rows, num_cols  # Devuelve la cantidad de filas y columnas

def remove_single_value_rows(df):
    # Función para eliminar las filas que contienen solo un dato
    return df[df.apply(lambda x: x.count() > 1, axis=1)]

def ask_percentage():
    # Función para solicitar al usuario un porcentaje de datos
    while True:
        try:
            percentage = int(input("Ingrese el porcentaje de datos que desea tomar (1-100): "))
            if 1 <= percentage <= 100:
                return percentage
            else:
                print("Por favor, ingrese un número entero entre 1 y 100.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def sample_dataframe(df, percentage):
    # Función para muestrear el dataframe basado en el porcentaje dado
    sample_size = int(len(df) * (percentage / 100))
    return df.sample(n=sample_size)

def calculate_sample_size(num_rows, percentage):
    # Función para calcular el tamaño de la muestra basado en el número de filas y el porcentaje dado
    sample_size = math.ceil((num_rows - 1) * (percentage / 100))
    return sample_size

def validate_columns(df_transpuesto, sample_size):
    # Función para validar cada columna y eliminar aquellas que no tienen al menos 'sample_size' datos diferentes de 0
    valid_columns = []
    for col in df_transpuesto.columns:
        count_non_zero = (df_transpuesto.iloc[1:, df_transpuesto.columns.get_loc(col)] != 0).sum()
        if count_non_zero >= sample_size:
            valid_columns.append(col)
    return df_transpuesto.loc[:, valid_columns]

def remove_all_zero_columns(df_transpuesto):
    # Función para eliminar las columnas que son completamente ceros desde la fila 2 en adelante
    valid_columns = [col for col in df_transpuesto.columns if (df_transpuesto.iloc[1:, df_transpuesto.columns.get_loc(col)] != 0).any()]
    return df_transpuesto.loc[:, valid_columns]

# Solicita la ubicación del archivo al usuario
file_path = input("Ingrese la locación del archivo CSV: ")

# Solicita la ubicación del archivo de salida al usuario
output_file_name = "dataframetransr.csv"
output_path = input(f"Ingrese la locación para guardar el archivo CSV transpuesto (ejemplo: C:/Users/Usuario/Downloads/{output_file_name}): ")

# Agrega el nombre del archivo al output_path si no está incluido
if not output_path.endswith(output_file_name):
    output_path = output_path.rstrip('/') + '/' + output_file_name

# Solicita el porcentaje de datos al usuario
percentage = ask_percentage()

try:
    # Llama a la función para cargar, ajustar y transponer el dataframe
    df_transpuesto = transpose_csv(file_path)

    # Obtiene la cantidad de filas y columnas del dataframe transpuesto
    num_rows, num_cols = get_transposed_dimensions(df_transpuesto)

    # Muestra las primeras filas del dataframe original
    df_original = pd.read_csv(file_path)
    print("Las primeras filas del dataframe original son:")
    print(df_original.head())

    # Muestra el dataframe transpuesto
    print("El dataframe transpuesto es:")
    print(df_transpuesto)

    # Muestra la cantidad de filas y columnas del dataframe transpuesto
    print(f"El dataframe transpuesto tiene {num_rows} filas y {num_cols} columnas.")

    # Calcula el tamaño de la muestra basado en el número de filas y el porcentaje dado
    sample_size = calculate_sample_size(num_rows, percentage)
    print(f"El tamaño de la muestra basado en el {percentage}% de {num_rows - 1} filas es: {sample_size}")

    # Elimina las columnas que son completamente ceros desde la fila 2 en adelante
    df_transpuesto = remove_all_zero_columns(df_transpuesto)
    print("El dataframe transpuesto después de eliminar columnas completamente ceros es:")
    print(df_transpuesto)

    # Valida las columnas del dataframe transpuesto basado en el tamaño de la muestra
    df_validado = validate_columns(df_transpuesto, sample_size)
    print("El dataframe transpuesto después de validar las columnas es:")
    print(df_validado)

    # Guarda el dataframe transpuesto y validado en un nuevo archivo CSV al final del proceso
    df_validado.to_csv(output_path, index=False, header=False)
    print(f"El archivo CSV transpuesto y validado se ha guardado en: {output_path}")

except Exception as e:
    # Muestra un mensaje de error si ocurre algún problema
    print(f"Ocurrió un error: {e}")