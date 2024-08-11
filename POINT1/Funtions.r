# Función para buscar 'NAME' en el dataframe y ajustar el dataframe para eliminar filas y columnas hasta esa posición
find_name_and_adjust_dataframe <- function(df) {
  position <- NULL  # Inicializa la variable 'position' para almacenar la posición de 'NAME' si se encuentra

  # Recorre cada fila del dataframe
  for (row_idx in seq_len(nrow(df))) {
    # Recorre cada columna del dataframe en la fila actual
    for (col_idx in seq_len(ncol(df))) {
      # Verifica si el valor de la celda actual es 'NAME'
      if (df[row_idx, col_idx] == 'NAME') {
        # Guarda la posición de la celda que contiene 'NAME'
        position <- c(row_idx, col_idx)
        break  # Sale del bucle de columnas
      }
    }
    if (!is.null(position)) {
      break  # Sale del bucle de filas si se encontró 'NAME'
    }
  }

  if (is.null(position)) {
    # Si 'NAME' no se encuentra en el dataframe, lanza un error
    stop("'NAME' no se encontró en el dataframe.")
  }

  # Obtiene la posición de 'NAME' (fila y columna)
  row <- position[1]
  col <- position[2]

  # Ajusta el dataframe eliminando las filas y columnas hasta 'NAME'
  df <- df[row:nrow(df), col:ncol(df)]

  return(df)  # Devuelve el dataframe ajustado
}

transpose_csv <- function(input_file) {
  # Función para cargar un CSV, ajustar el dataframe, transponerlo

  # Carga el dataframe desde el archivo CSV
  df <- read.csv(input_file)

  # Verifica y ajusta el dataframe
  df <- find_name_and_adjust_dataframe(df)

  if (nrow(df) == 0) {
    # Si el dataframe está vacío después de ajustar, lanza un error
    stop("El dataframe está vacío después de eliminar filas y columnas.")
  }

  # Transpone el dataframe
  df_transpuesto <- t(df)

  # Elimina las filas que contienen solo un dato
  df_transpuesto <- remove_single_value_rows(df_transpuesto)

  return(df_transpuesto)  # Devuelve el dataframe transpuesto
}

remove_single_value_rows <- function(df) {
  # Función para eliminar las filas que contienen solo un dato
  df <- df[apply(df, 1, function(row) sum(!is.na(row)) > 1), ]
  return(df)
}

library(dplyr)  # Carga la librería dplyr para manipulación y análisis de datos
library(readr)  # Carga la librería readr para la lectura de archivos CSV

get_csv_file <- function() {
  # Función para obtener la ruta del archivo CSV y cargarlo en un DataFrame
  file_path <- readline(prompt = "Por favor, ingrese la ubicación del archivo CSV: ")
  data <- read_csv(file_path)  # Lee el archivo CSV y devuelve el DataFrame junto con la ruta del archivo
  return(list(data, file_path))
}

validate_rows <- function(data) {
  # Función para validar y devolver el número de filas en el DataFrame
  num_rows <- nrow(data)  # Obtiene el número de filas
  return(num_rows)  # Devuelve el número de filas
}

calculate_sample_size <- function(num_rows, percentage) {
  # Función para calcular el tamaño de la muestra basado en el número de filas y el porcentaje dado
  sample_size <- ceiling(num_rows * (percentage / 100))  # Calcula el tamaño de la muestra y redondea hacia arriba
  return(sample_size)  # Devuelve el tamaño de la muestra
}

remove_zero_columns <- function(data) {
  # Función para eliminar columnas que tienen solo ceros desde la fila 1 hasta la fila final
  zero_cols <- sapply(data, function(col) all(col == 0))  # Verifica si todos los valores de la columna son cero
  data <- data[, !zero_cols]  # Elimina las columnas si todos los valores son cero
  return(data)  # Devuelve el DataFrame modificado
}

remove_insufficient_data_columns <- function(data, sample_size) {
  # Función para eliminar columnas que no tienen suficientes datos diferentes de cero
  insufficient_cols <- sapply(data, function(col) sum(col != 0) < sample_size)  # Cuenta los valores diferentes de cero en la columna
  data <- data[, !insufficient_cols]  # Elimina las columnas si no tienen suficientes datos
  return(data)  # Devuelve el DataFrame modificado
}

replace_na_with_zero <- function(data) {
  # Función para reemplazar todos los valores NA con 0 y contar cuántos fueron modificados
  na_count <- sum(is.na(data))  # Cuenta el número total de valores NA
  data[is.na(data)] <- 0  # Reemplaza todos los valores NA con 0
  cat("Total de valores NA convertidos a 0:", na_count, "\n")  # Imprime el número de valores NA reemplazados
  return(data)  # Devuelve el DataFrame modificado
}

average_duplicate_columns <- function(data) {
  # Función para promediar columnas duplicadas y dejar una sola
  duplicated_columns <- names(data)[duplicated(names(data))]  # Encuentra las columnas duplicadas
  unique_duplicated_columns <- unique(duplicated_columns)  # Obtiene las columnas duplicadas únicas
  
  columns_repeated_count <- 0  # Inicializa el contador de columnas repetidas
  
  for (col in unique_duplicated_columns) {
    repeated_cols <- data[, col]  # Obtiene las columnas repetidas
    averaged_col <- rowMeans(repeated_cols, na.rm = TRUE)  # Calcula el promedio de las columnas repetidas
    data <- data[, !colnames(data) %in% col]  # Elimina las columnas repetidas
    data[[col]] <- averaged_col  # Añade la columna promedio
    columns_repeated_count <- columns_repeated_count + 1  # Incrementa el contador de columnas repetidas
  }
  
  cat("Número de columnas repetidas que se promediaron:", columns_repeated_count, "\n")  # Imprime el número de columnas repetidas promediadas
  return(data)  # Devuelve el DataFrame modificado
}

show_dataframe_shape <- function(data) {
  # Función para mostrar el número de filas y columnas del DataFrame
  num_rows <- nrow(data)  # Obtiene el número de filas
  num_columns <- ncol(data)  # Obtiene el número de columnas
  cat("El DataFrame ajustado tiene", num_rows, "filas y", num_columns, "columnas\n")  # Imprime el número de filas y columnas
}

main <- function() {
  result <- get_csv_file()  # Obtiene el archivo CSV y su ruta
  data <- result[[1]]
  file_path <- result[[2]]
  
  data <- replace_na_with_zero(data)  # Reemplaza valores NA con 0
  data <- remove_zero_columns(data)  # Elimina columnas con solo ceros
  
  num_rows <- validate_rows(data)  # Valida y obtiene el número de filas
  cat("Número de filas:", num_rows, "\n")  # Imprime el número de filas
  
  percentage <- as.numeric(readline(prompt = "Ingrese el porcentaje de datos que desea tomar: "))  # Solicita el porcentaje de datos
  sample_size <- calculate_sample_size(num_rows, percentage)  # Calcula el tamaño de la muestra
  cat("El tamaño del porcentaje calculado es:", sample_size, "\n")  # Imprime el tamaño de la muestra
  
  data <- remove_insufficient_data_columns(data, sample_size)  # Elimina columnas con datos insuficientes
  data <- average_duplicate_columns(data)  # Promedia columnas duplicadas
  
  show_dataframe_shape(data)  # Muestra el número de filas y columnas del DataFrame
  
  # Sobrescribir el archivo CSV original
  write_csv(data, file_path)  # Guarda el DataFrame modificado en el archivo CSV original
  cat("Archivo sobrescrito:", file_path, "\n")  # Imprime un mensaje de confirmación
}

main()  # Ejecuta la función principal
