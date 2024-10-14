from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import time

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Variables globales para almacenar los datos de mRNA y miRNA
mrna_data = None
mirna_data = None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'sa' and password == 'Krypton':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return "Login incorrecto. Inténtalo de nuevo."
    
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    global mrna_data, mirna_data
    if request.method == 'POST':
        mrna_file = request.files.get('mrna_file')
        if mrna_file and mrna_file.filename.endswith('.csv'):
            mrna_data = pd.read_csv(mrna_file)

        mirna_file = request.files.get('mirna_file')
        if mirna_file and mirna_file.filename.endswith('.csv'):
            mirna_data = pd.read_csv(mirna_file)

        if mrna_data is not None and mirna_data is not None:
            mrna_preview = mrna_data.iloc[:5, :4]
            mirna_preview = mirna_data.iloc[:5, :4]
            time.sleep(1)

            return render_template('index.html',
                                   mrna_table=mrna_preview.to_html(classes='data', header=True),
                                   mirna_table=mirna_preview.to_html(classes='data', header=True),
                                   mrna_loaded=True,
                                   mirna_loaded=True)

    return render_template('index.html', mrna_loaded=False, mirna_loaded=False)

# Ruta para manejar tanto GET como POST en /run-algorithm
@app.route('/run-algorithm', methods=['GET', 'POST'])
def run_algorithm():
    # Si es POST, procesamos la solicitud si se requiere
    if request.method == 'POST':
        # Aquí puedes agregar cualquier lógica adicional para procesar datos si es necesario
        pass
    
    # De cualquier manera, renderizamos la página de algoritmo
    return render_template('run_algorithm.html')

@app.route('/visualization')
def visualization():
    # Simulando una tabla de ejemplo
    table_data = [
        {'name': 'Gene A', 'value': 10},
        {'name': 'Gene B', 'value': 20},
        {'name': 'Gene C', 'value': 30},
        {'name': 'Gene D', 'value': 40},
    ]
    return render_template('visualization.html', table_data=table_data)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
