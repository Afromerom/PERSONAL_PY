import pandas as pd

def check_and_adjust_dataframe(df):
    # Verificar y ajustar el dataframe para que el primer elemento sea 'NAME'
    while df.iat[0, 0] != 'NAME':
        df = df.iloc[1:, 1:]
    return df

def transpose_csv(input_file, output_file):
    # Cargar el dataframe desde el archivo CSV
    df = pd.read_csv(input_file)
    
    # Verificar y ajustar el dataframe
    df = check_and_adjust_dataframe(df)
    
    # Transponer el dataframe
    df_transpuesto = df.transpose()
    
    # Guardar el dataframe transpuesto en un nuevo archivo CSV
    df_transpuesto.to_csv(output_file, index=False)
    
    # Devolver el dataframe transpuesto
    return df_transpuesto

# Solicitar la ubicación del archivo al usuario
file_path = input("Ingrese la locación del archivo CSV: ")

# Solicitar la ubicación del archivo de salida al usuario
output_path = input("Ingrese la locación para guardar el archivo CSV transpuesto (ejemplo: C:/Users/Usuario/Downloads/dataframetransr.csv): ")

# Llamar a la función con los archivos de entrada y salida proporcionados por el usuario
df_transpuesto = transpose_csv(file_path, output_path)

# Mostrar las primeras filas del dataframe original
df_original = pd.read_csv(file_path)
print("Las primeras filas del dataframe original son:")
print(df_original.head())

# Mostrar el dataframe transpuesto
print("El dataframe transpuesto es:")
print(df_transpuesto)








##Solo para visualization
# # Mostrar las primeras filas del dataframe original
# df_original = pd.read_csv(file_path)
# print("Las primeras filas del dataframe original son:")
# print(df_original.head())

# # Mostrar el dataframe transpuesto
# print("El dataframe transpuesto es:")
# print(df_transpuesto)

