#############################################################################
#Codigo 1 import data to python
import pandas as pd

#Upload CSV file
file_path = "C:/Users/Pipe/Downloads/SC_mRNAsdata1.csv"
df = pd.read_csv(file_path)

#Display the first rows of the dataframe
print(df.head())
#############################################################################

#############################################################################
# #Create the excel file
# import pandas as pd

# # Load CSV file
# file_path_csv = "C:/Users/Pipe/Downloads/SC_mRNAsdata1.csv"
# df = pd.read_csv(file_path_csv)

# # Define the path to the Excel file
# file_path_excel = "C:/Users/Pipe/Downloads/SC_mRNAsdata1.xlsx"

# # Save the dataframe as Excel file
# df.to_excel(file_path_excel, index=False, engine='openpyxl')

# print(f"Archivo Excel guardado en: {file_path_excel}")
#############################################################################

#############################################################################
#Code transpone el dataset
import pandas as pd

# Cargar el archivo CSV
file_path_csv = "C:/Users/Pipe/Downloads/SC_mRNAsdata1.csv"
df = pd.read_csv(file_path_csv)

# Transpose the dataframe
df_transposed = df.transpose()

# Define output paths
file_path_excel_transposed = "C:/Users/Pipe/Downloads/SC_mRNAsdataTrans.xlsx"
file_path_csv_transposed = "C:/Users/Pipe/Downloads/SC_mRNAsdataTrans.csv"

# Save the transposed dataframe in multiple Excel sheets
max_columns = 16384
num_sheets = (df_transposed.shape[1] // max_columns) + 1

with pd.ExcelWriter(file_path_excel_transposed, engine='openpyxl') as writer:
    for i in range(num_sheets):
        start_col = i * max_columns
        end_col = (i + 1) * max_columns
        sheet_name = f'Sheet_{i+1}'
        df_transposed.iloc[:, start_col:end_col].to_excel(writer, sheet_name=sheet_name, index=False)

#Save the transposed dataframe as a CSV file
df_transposed.to_csv(file_path_csv_transposed, index=False)

print(f"Archivo Excel transpuesto guardado en: {file_path_excel_transposed}")
print(f"Archivo CSV transpuesto guardado en: {file_path_csv_transposed}")
#############################################################################

#############################################################################
# #Codigo que cuenta los repetidos
# import pandas as pd
# # Cargar el archivo CSV
# file_path_csv_transposed = "C:/Users/Pipe/Downloads/SC_mRNAsdataTrans.csv"
# df_transposed = pd.read_csv(file_path_csv_transposed)
# # Count the names of the columns
# column_names = df_transposed.columns
# # Count repeated column names
# duplicated_columns = column_names[column_names.duplicated()]
# num_duplicated_columns = len(duplicated_columns)
# # Show duplicate columns and their number
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

# # Delete the columns in positions 1 and 2
# columns_to_remove = [1, 2]
# df = df.drop(df.columns[columns_to_remove], axis=1)

# # # Remove unwanted rows by position
# rows_to_remove = [1]
# df = df.drop(rows_to_remove, axis=0)

# # Save the resulting dataframe in a CSV file
# file_path_csv_cleaned = "C:/Users/Pipe/Downloads/SC_mRNAsdataTrans_cleaned.csv"
# df.to_csv(file_path_csv_cleaned, index=False)

# print(f"Archivo CSV limpio guardado en: {file_path_csv_cleaned}")

# # Show the first few rows of the clean dataframe for reference
# print("DataFrame limpio:")
# print(df.head())

#############################################################################
# # #Codigo borra filas
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
# # Show first rows for reference
# print("DataFrame original:")
# print(df.head())
# # Range of rows to consider (row 2 to 23, indexed from 0)
# start_row = 1
# end_row = 23
# # Convert the interest rows to floating rate
# df_values = df.iloc[start_row:end_row].astype(float)
# # Select columns that are not all 0's in the specified range of rows
# df_cleaned = df.loc[:, (df_values != 0).any(axis=0)]
# # Save the resulting dataframe in a new CSV file
# file_path_csv_cleaned = "C:/Users/Pipe/Downloads/SC_mRNAsdataTransAdj_cleaned.csv"
# df_cleaned.to_csv(file_path_csv_cleaned, index=False)
# print(f"Archivo CSV limpio guardado en: {file_path_csv_cleaned}")
# # Mostrar las primeras filas del dataframe limpio para referencia
# print("DataFrame limpio:")
# print(df_cleaned.head())

#############################################################################
#import pandas as pd
# Read CSV file
csv_file = "C:/Users/Pipe/Downloads/SC_mRNAsdataTransAdj_cleaned.csv"
df = pd.read_csv(csv_file)
# Write DataFrame to Excel file
excel_file = "C:/Users/Pipe/Downloads/SC_mRNAsdataTransAdj_cleaned.xlsx"
df.to_excel(excel_file, index=False)

#############################################################################
# import pandas as pd
# # Read the CSV file into a DataFrame
# mi_dataset = pd.read_csv('C:/Users/Pipe/Downloads/SC_mRNAsdataTransAdj_cleaned.csv')
# # Drop columns that contain any NA values
# mi_dataset = mi_dataset.dropna(axis=1)
# # Save the modified DataFrame to a new CSV file
# mi_dataset.to_csv('C:/Users/Pipe/Downloads/SC_mRNAsdataTransAdj_cleaned.csv', index=False)
# # Print the DataFrame to verify the changes
# print(mi_dataset)
#############################################################################
# import pandas as pd

# # Read the CSV file into a DataFrame
# mi_dataset = pd.read_csv('C:/Users/Pipe/Downloads/SC_mRNAsdataTransAdj_cleaned.csv')
# # Keep columns with at least 17 non-null values
# mi_dataset = mi_dataset.dropna(thresh=17, axis=1)
# # Identify columns with exactly 3 non-null values
# columns_to_drop = mi_dataset.columns[mi_dataset.isnull().sum() == (mi_dataset.shape[0] - 3)]
# # Drop columns with exactly 3 non-null values
# mi_dataset = mi_dataset.drop(columns=columns_to_drop)
# # Save the modified DataFrame to a new CSV file
# mi_dataset.to_csv('SC_mRNAsdataTransAdj_2.0.csv', index=False)


# #############################################################################
# # Remove the last three characters from each element in the first column
# mi_dataset['col1'] = mi_dataset['col1'].str[:-3]
# # Print the dataset to verify the changes
# print(mi_dataset)
import pandas as pd
# Read the first CSV file into a DataFrame
dataset1 = pd.read_csv('dataset1.csv')
# Read the second CSV file into a DataFrame
dataset2 = pd.read_csv('dataset2.csv')
# Perform intersection based on the first column 'NAME'
intersection = pd.merge(dataset1, dataset2, on='NAME')
# Save the intersection result to a new CSV file
intersection.to_csv('intersection.csv', index=False)
# Print the intersection DataFrame to verify the changes
print(intersection)