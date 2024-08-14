from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Variable global para almacenar el dataframe
df = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global df  # Usamos la variable global
    if request.method == 'POST':
        # Verificar si se subió un archivo
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and file.filename.endswith('.csv'):
            # Leer el archivo CSV con pandas
            df = pd.read_csv(file)
            # Aquí puedes procesar el archivo o guardarlo si lo deseas
            return render_template('index.html', tables=[df.to_html()], titles=df.columns.values)
    return render_template('index.html')

@app.route('/calcular-promedio', methods=['POST'])
def calcular_promedio():
    global df  # Usamos la variable global
    if df is not None:
        # Calcular el promedio de cada fila
        promedios = df.mean(axis=1)
        promedio_total = promedios.mean()
        return render_template('index.html', promedio=promedio_total, tables=[df.to_html()], titles=df.columns.values)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
