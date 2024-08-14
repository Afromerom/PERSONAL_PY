from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

df = None  # Variable global para almacenar el DataFrame cargado

@app.route('/', methods=['GET', 'POST'])
def index():
    global df
    if request.method == 'POST':
        # Verifica si se ha subido un archivo
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # Verifica si se ha seleccionado un archivo
        if file.filename == '':
            return 'No selected file'
        # Verifica si el archivo subido es un CSV
        if file and file.filename.endswith('.csv'):
            # Carga el archivo CSV en un DataFrame
            df = pd.read_csv(file)
            # Renderiza la plantilla HTML con la tabla del DataFrame
            return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)
    # Si no hay un archivo subido, simplemente renderiza la página inicial
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    global df
    if df is not None:
        # Selecciona las filas desde la 0 hasta la 21 (incluyendo todas las columnas)
        df_filtered = df.iloc[0:22, 1:]  # Excluye solo la primera columna para el cálculo
        # Calcula el promedio de cada columna en el DataFrame filtrado
        averages = df_filtered.mean()

        # Inserta los promedios en el DataFrame, dejando solo la columna 'NAME' vacía
        df.loc['Promedio'] = pd.concat([pd.Series(['']), averages], axis=0).values

        # Renderiza la plantilla HTML con la tabla del DataFrame, incluyendo la fila de promedios
        return render_template('index.html', tables=[df.to_html(classes='data')])
    # Si no hay un DataFrame cargado, redirige a la página principal
    return redirect(url_for('index'))

if __name__ == "__main__":
    # Ejecuta la aplicación Flask en la red local, accesible desde cualquier dispositivo en la misma red
    app.run(host='0.0.0.0', port=5000, debug=True)
