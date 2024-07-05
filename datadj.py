#############################################################################
##Codigo 1 import data to python 
#import pandas as pd

# Cargar el archivo CSV
#file_path = "C:/Users/Pipe/Downloads/SC_mRNAsdata1.csv"
#df = pd.read_csv(file_path)

# Mostrar las primeras filas del dataframe
#print(df.head())
#############################################################################

#############################################################################
##Create the excel file 
#import pandas as pd

# Cargar el archivo CSV
#file_path_csv = "C:/Users/Pipe/Downloads/SC_mRNAsdata1.csv"
#df = pd.read_csv(file_path_csv)

# Definir la ruta para el archivo Excel
#file_path_excel = "C:/Users/Pipe/Downloads/SC_mRNAsdata1.xlsx"

# Guardar el dataframe como archivo Excel
#df.to_excel(file_path_excel, index=False, engine='openpyxl')

#print(f"Archivo Excel guardado en: {file_path_excel}")
#############################################################################

#############################################################################
#Code transpone el dataset
# import pandas as pd

# # Cargar el archivo CSV
# file_path_csv = "C:/Users/Pipe/Downloads/SC_mRNAsdata1.csv"
# df = pd.read_csv(file_path_csv)

# # Transponer el dataframe
# df_transposed = df.transpose()

# # Restablecer los nombres de las columnas (opcional)
# df_transposed.reset_index(inplace=True)
# df_transposed.columns = df_transposed.iloc[0]  # Usa la primera fila como nombres de columnas
# df_transposed = df_transposed[1:]  # Eliminar la primera fila que ahora son nombres de columnas

# # Definir las rutas de salida
# file_path_excel_transposed = "C:/Users/Pipe/Downloads/SC_mRNAsdataTrans.xlsx"
# file_path_csv_transposed = "C:/Users/Pipe/Downloads/SC_mRNAsdataTrans.csv"

# # Guardar el dataframe transpuesto en múltiples hojas de Excel
# max_columns = 16384
# num_sheets = (df_transposed.shape[1] // max_columns) + 1

# with pd.ExcelWriter(file_path_excel_transposed, engine='openpyxl') as writer:
#     for i in range(num_sheets):
#         start_col = i * max_columns
#         end_col = (i + 1) * max_columns
#         sheet_name = f'Sheet_{i+1}'
#         df_transposed.iloc[:, start_col:end_col].to_excel(writer, sheet_name=sheet_name, index=False)

# Guardar el dataframe transpuesto como archivo CSV
#df_transposed.to_csv(file_path_csv_transposed, index=False)

#print(f"Archivo Excel transpuesto guardado en: {file_path_excel_transposed}")
#print(f"Archivo CSV transpuesto guardado en: {file_path_csv_transposed}")
#############################################################################

#############################################################################
# #Codigo que cuenta los repetidos 
# import pandas as pd

# # Cargar el archivo CSV
# file_path_csv_transposed = "C:/Users/Pipe/Downloads/SC_mRNAsdataTrans.csv"
# df_transposed = pd.read_csv(file_path_csv_transposed)

# # Contar los nombres de las columnas
# column_names = df_transposed.columns

# # Contar nombres de columnas repetidos
# duplicated_columns = column_names[column_names.duplicated()]
# num_duplicated_columns = len(duplicated_columns)

# # Mostrar las columnas duplicadas y su cantidad
# print(f"Número de columnas con nombres duplicados: {num_duplicated_columns}")
# if num_duplicated_columns > 0:
#     print("Columnas duplicadas:")
#     print(duplicated_columns)
#############################################################################

#############################################################################
# #Codigo borra las columnas 
# import pandas as pd

# # Cargar el archivo CSV
# file_path_csv = "C:/Users/Pipe/Downloads/SC_mRNAsdataTrans.csv"
# df = pd.read_csv(file_path_csv)

# # Mostrar las primeras filas para referencia
# print("DataFrame original:")
# print(df.head())

# # Eliminar columnas no deseadas por posición
# # Ejemplo: eliminar las columnas en las posiciones 1 y 2 (comienza en 0)
# columns_to_remove = [1, 2]
# df = df.drop(df.columns[columns_to_remove], axis=1)

# # Eliminar filas no deseadas por posición
# # Ejemplo: eliminar las filas en las posiciones 0 y 1 (comienza en 0)
# rows_to_remove = [1]
# df = df.drop(rows_to_remove, axis=0)

# # Guardar el dataframe resultante en un archivo CSV
# file_path_csv_cleaned = "C:/Users/Pipe/Downloads/SC_mRNAsdataTrans_cleaned.csv"
# df.to_csv(file_path_csv_cleaned, index=False)

# print(f"Archivo CSV limpio guardado en: {file_path_csv_cleaned}")

# # Mostrar las primeras filas del dataframe limpio para referencia
# print("DataFrame limpio:")
# print(df.head())

#############################################################################
#Codigo borra filas 
# import pandas as pd

# # Cargar el archivo CSV
# file_path_csv = "C:/Users/Pipe/Downloads/SC_mRNAsdataTrans.csv"
# df = pd.read_csv(file_path_csv)

# # Mostrar las primeras filas para referencia
# print("DataFrame original:")
# print(df.head())

# # Eliminar filas no deseadas por posición
# # Ejemplo: eliminar las filas en las posiciones 0, 2, y 4 (comienza en 0)
# rows_to_remove = [0]
# df = df.drop(rows_to_remove, axis=0)

# # Guardar el dataframe resultante en un archivo CSV
# file_path_csv_cleaned = "C:/Users/Pipe/Downloads/SC_mRNAsdataTrans_cleaned.csv"
# df.to_csv(file_path_csv_cleaned, index=False)

# print(f"Archivo CSV limpio guardado en: {file_path_csv_cleaned}")

# # Mostrar las primeras filas del dataframe limpio para referencia
# print("DataFrame limpio:")
# print(df.head())

#############################################################################


#############################################################################
# #Limpia las columnas que tengan 0 datos 
# import pandas as pd

# # Cargar el archivo CSV con la primera fila como nombres de columna
# file_path_csv = "C:/Users/Pipe/Downloads/SC_mRNAsdataTransAdj.csv"
# df = pd.read_csv(file_path_csv, header=0)

# # Mostrar las primeras filas para referencia
# print("DataFrame original:")
# print(df.head())

# # Rango de filas a considerar (de la fila 2 a la 23, indexadas desde 0)
# start_row = 1
# end_row = 23

# # Convertir las filas de interés a tipo flotante
# df_values = df.iloc[start_row:end_row].astype(float)

# # Seleccionar columnas que no sean todas 0 en el rango de filas especificado
# df_cleaned = df.loc[:, (df_values != 0).any(axis=0)]

# # Guardar el dataframe resultante en un nuevo archivo CSV
# file_path_csv_cleaned = "C:/Users/Pipe/Downloads/SC_mRNAsdataTransAdj_cleaned.csv"
# df_cleaned.to_csv(file_path_csv_cleaned, index=False)

# print(f"Archivo CSV limpio guardado en: {file_path_csv_cleaned}")

# # Mostrar las primeras filas del dataframe limpio para referencia
# print("DataFrame limpio:")
# print(df_cleaned.head())

#############################################################################
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri

# Activar la conversión automática entre pandas y R
pandas2ri.activate()

# Cargar el archivo CSV en un dataframe de pandas
file_path_csv = "C:/Users/Pipe/Downloads/SC_mRNAsdataTransAdj_cleaned.csv"
df = pd.read_csv(file_path_csv)

# Convertir el dataframe de pandas a un dataframe de R
r_df = pandas2ri.py2rpy(df)

# Definir el archivo RDA de salida
file_path_rda = "C:/Users/Pipe/Downloads/SC_mRNAsdataTransAdj_cleaned.rda"

# Guardar el dataframe de R como un archivo RDA
ro.r.assign("df_r", r_df)
ro.r(f"save(df_r, file='{file_path_rda}')")

print(f"Archivo RDA guardado en: {file_path_rda}")
