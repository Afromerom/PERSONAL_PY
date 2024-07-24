# Solicitar la ubicación del archivo al usuario
file_path <- readline(prompt = "Ingrese la locación del archivo CSV: ")
# Solicitar la ubicación del archivo de salida al usuario
output_path <- readline(prompt = "Ingrese la locación para guardar el archivo CSV transpuesto: ")
# Cargar las librerías necesarias
library(data.table)
# Definir la función para transponer un dataframe desde un archivo CSV
transpose_csv <- function(input_file, output_file) {
  # Cargar el dataframe desde el archivo CSV
  df <- fread(input_file)
  # Transponer el dataframe
  df_transpuesto <- t(df)
  # Convertir de matriz a dataframe
  df_transpuesto <- as.data.frame(df_transpuesto)
  # Guardar el dataframe transpuesto en un nuevo archivo CSV
  fwrite(df_transpuesto, output_file)
  # Devolver el dataframe transpuesto
  return(df_transpuesto)
}



##Lineas de Visualizacion 
# # Llamar a la función con los archivos de entrada y salida proporcionados por el usuario
# df_transpuesto <- transpose_csv(file_path, output_path)
# # Mostrar las primeras filas del dataframe original
# df_original <- fread(file_path)
# print("Las primeras filas del dataframe original son:")
# print(head(df_original))
# # Mostrar el dataframe transpuesto
# print("El dataframe transpuesto es:")
# print(df_transpuesto)

