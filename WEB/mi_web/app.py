from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
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

if __name__ == "__main__":
    app.run(debug=True)
