import pandas as pd  # Importa la librería pandas para manipulación y análisis de datos
import math  # Importa la librería math para funciones matemáticas

def get_csv_file():
    # Función para obtener la ruta del archivo CSV y cargarlo en un DataFrame
    file_path = input("Por favor, ingrese la ubicación del archivo CSV: ")
    return pd.read_csv(file_path), file_path  # Lee el archivo CSV y devuelve el DataFrame junto con la ruta del archivo

def validate_rows(data):
    # Función para validar y devolver el número de filas en el DataFrame
    num_rows = data.shape[0]
    return num_rows  # Devuelve el número de filas

def calculate_sample_size(num_rows, percentage):
    # Función para calcular el tamaño de la muestra basado en el número de filas y el porcentaje dado
    sample_size = math.ceil(num_rows * (percentage / 100))  # Calcula el tamaño de la muestra y redondea hacia arriba
    return sample_size  # Devuelve el tamaño de la muestra

def remove_zero_columns(data):
    # Función para eliminar columnas que tienen solo ceros desde la fila 1 hasta la fila final
    for col in data.columns:
        if (data[col] == 0).all():  # Verifica si todos los valores de la columna son cero
            data.drop(columns=[col], inplace=True)  # Elimina la columna si todos los valores son cero
    return data  # Devuelve el DataFrame modificado

def remove_insufficient_data_columns(data, sample_size):
    # Función para eliminar columnas que no tienen suficientes datos diferentes de cero
    for col in data.columns:
        non_zero_count = (data[col] != 0).sum()  # Cuenta los valores diferentes de cero en la columna
        if non_zero_count < sample_size:  # Verifica si la cantidad de valores diferentes de cero es menor al tamaño de la muestra
            data.drop(columns=[col], inplace=True)  # Elimina la columna si no tiene suficientes datos
    return data  # Devuelve el DataFrame modificado

def replace_na_with_zero(data):
    # Función para reemplazar todos los valores NA con 0 y contar cuántos fueron modificados
    na_count = data.isna().sum().sum()  # Cuenta el número total de valores NA
    data.fillna(0, inplace=True)  # Reemplaza todos los valores NA con 0
    print(f"Total de valores NA convertidos a 0: {na_count}")  # Imprime el número de valores NA reemplazados
    return data  # Devuelve el DataFrame modificado

def average_duplicate_columns(data):
    # Función para promediar columnas duplicadas y dejar una sola
    duplicated_columns = data.columns[data.columns.duplicated()]  # Encuentra las columnas duplicadas
    unique_duplicated_columns = duplicated_columns.unique()  # Obtiene las columnas duplicadas únicas
    
    columns_repeated_count = 0  # Inicializa el contador de columnas repetidas
    
    for col in unique_duplicated_columns:
        repeated_cols = data.loc[:, col]  # Obtiene las columnas repetidas
        averaged_col = repeated_cols.mean(axis=1)  # Calcula el promedio de las columnas repetidas
        data = data.drop(columns=col, axis=1)  # Elimina las columnas repetidas
        data[col] = averaged_col  # Añade la columna promedio
        columns_repeated_count += 1  # Incrementa el contador de columnas repetidas
    
    print(f"Número de columnas repetidas que se promediaron: {columns_repeated_count}")  # Imprime el número de columnas repetidas promediadas
    return data  # Devuelve el DataFrame modificado

def show_dataframe_shape(data):
    # Función para mostrar el número de filas y columnas del DataFrame
    num_rows, num_columns = data.shape  # Obtiene el número de filas y columnas
    print(f"El DataFrame ajustado tiene {num_rows} filas y {num_columns} columnas")  # Imprime el número de filas y columnas

def main():
    data, file_path = get_csv_file()  # Obtiene el archivo CSV y su ruta
    data = replace_na_with_zero(data)  # Reemplaza valores NA con 0
    data = remove_zero_columns(data)  # Elimina columnas con solo ceros
    
    num_rows = validate_rows(data)  # Valida y obtiene el número de filas
    print(f"Número de filas: {num_rows}")  # Imprime el número de filas
    
    percentage = float(input("Ingrese el porcentaje de datos que desea tomar: "))  # Solicita el porcentaje de datos
    sample_size = calculate_sample_size(num_rows, percentage)  # Calcula el tamaño de la muestra
    print(f"El tamaño del porcentaje calculado es: {sample_size}")  # Imprime el tamaño de la muestra
    
    data = remove_insufficient_data_columns(data, sample_size)  # Elimina columnas con datos insuficientes
    data = average_duplicate_columns(data)  # Promedia columnas duplicadas
    
    show_dataframe_shape(data)  # Muestra el número de filas y columnas del DataFrame
    
    # Sobrescribir el archivo CSV original
    data.to_csv(file_path, index=False)  # Guarda el DataFrame modificado en el archivo CSV original
    print(f"Archivo sobrescrito: {file_path}")  # Imprime un mensaje de confirmación

if __name__ == "__main__":
    main()  # Ejecuta la función principal