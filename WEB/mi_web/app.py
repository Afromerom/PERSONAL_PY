from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import time

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para manejar sesiones

# Usuario y contraseña permitidos
USERNAME = 'sa'
PASSWORD = 'Krypton'

# Variables globales para almacenar los datos de mRNA y miRNA
mrna_data = None
mirna_data = None

# Ruta de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verifica usuario y contraseña
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))  # Redirige a la página principal
        else:
            return "Login incorrecto. Inténtalo de nuevo."
    
    return render_template('login.html')

# Ruta protegida para la página principal (carga de archivos)
@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))  # Redirige al login si no está autenticado

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

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.clear()  # Borra todos los datos de la sesión
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)