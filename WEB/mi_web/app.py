from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import time

app = Flask(__name__)

# Variables globales para almacenar los datos de mRNA y miRNA
mrna_data = None
mirna_data = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global mrna_data, mirna_data
    if request.method == 'POST':
        # Cargar archivo mRNA
        mrna_file = request.files.get('mrna_file')
        if mrna_file and mrna_file.filename.endswith('.csv'):
            mrna_data = pd.read_csv(mrna_file)

        # Cargar archivo miRNA
        mirna_file = request.files.get('mirna_file')
        if mirna_file and mirna_file.filename.endswith('.csv'):
            mirna_data = pd.read_csv(mirna_file)

        # Verificar si ambos archivos han sido cargados
        if mrna_data is not None and mirna_data is not None:
            # Obtener las primeras 5 filas y 4 columnas de ambos archivos
            mrna_preview = mrna_data.iloc[:5, :4]
            mirna_preview = mirna_data.iloc[:5, :4]

            # Simular tiempo de carga (progreso de 1 segundo por ejemplo)
            time.sleep(1)

            # Renderizar las tablas en la página HTML
            return render_template('index.html',
                                   mrna_table=mrna_preview.to_html(classes='data', header=True),
                                   mirna_table=mirna_preview.to_html(classes='data', header=True),
                                   mrna_loaded=True,
                                   mirna_loaded=True)

    return render_template('index.html', mrna_loaded=False, mirna_loaded=False)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
