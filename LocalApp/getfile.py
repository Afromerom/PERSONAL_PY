import rpy2.robjects as ro
from rpy2.robjects import pandas2ri
import pandas as pd

# Activa la conversión de objetos R a pandas DataFrames
pandas2ri.activate()

def convert_rda_to_csv(rda_file, csv_file):
    # Carga el archivo .rda
    ro.r['load'](rda_file)
    
    # Obtén la lista de objetos R en el entorno global
    r_objects = ro.r['ls']()
    
    if len(r_objects) == 0:
        print("No se encontraron objetos en el archivo .rda")
        return
    
    # Supongamos que el archivo .rda tiene un solo objeto, lo cargamos
    r_data = ro.globalenv[r_objects[0]]  # Puedes ajustar esto si tienes múltiples objetos
    
    # Convertimos el objeto R a un DataFrame de pandas
    df = pandas2ri.rpy2py_dataframe(r_data)
    
    # Guardamos el DataFrame en un archivo CSV
    df.to_csv(csv_file, index=False)
    print(f"Archivo CSV guardado como: {csv_file}")

# Uso del script
rda_file = r"C:\Users\Pipe\Desktop\SC_miRNAsdata.rda"  # Reemplaza con la ruta a tu archivo .rda
csv_file = r"C:\Users\Pipe\Desktop\SC_miRNAsdata.csv"  # Reemplaza con la ruta donde quieres guardar el archivo .csv

convert_rda_to_csv(rda_file, csv_file)

