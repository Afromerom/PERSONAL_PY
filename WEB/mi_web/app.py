from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

df = None  # Variable global para almacenar el dataframe

@app.route('/', methods=['GET', 'POST'])
def index():
    global df
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            return render_template('index.html', tables=[df.to_html()], titles=df.columns.values)
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    global df
    if df is not None:
        # Excluir las dos primeras columnas y calcular el promedio por columna
        df_filtered = df.iloc[:, 2:]
        averages = df_filtered.mean()
        # Añadir el promedio como una nueva fila al final del DataFrame
        df.loc['Promedio'] = pd.concat([df.iloc[:, :2], pd.DataFrame(averages).T], axis=1).iloc[0]
        return render_template('index.html', tables=[df.to_html(classes='data')])
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
