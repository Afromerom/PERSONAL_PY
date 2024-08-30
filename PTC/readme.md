<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PTC Python Functions - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1 {
            color: #0056b3;
            text-align: center;
        }
        h2 {
            color: #0056b3;
        }
        p {
            margin: 10px 0;
        }
        .function-name {
            font-weight: bold;
            color: #0056b3;
            background-color: #e0f7fa;
            padding: 5px;
            display: inline-block;
        }
        .code-block {
            background-color: #e8eaf6;
            padding: 10px;
            border-radius: 5px;
            font-family: "Courier New", Courier, monospace;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <h1 align="center"><br>
    PTC Python Functions<br>
    Fase Preliminar 🤖 <br> 
    Un enfoque de causalidad pseudotemporal para identificar interacciones miARN-ARNm durante procesos biológicos<br> 
    AndresMCB <br> 
    2024 📅</h1><br>

    <h2>👨‍💻 Python 🐍</h2>
    
    <h2>PTC Python Functions - README</h2>
    <p>Este documento proporciona un breve resumen de las funciones convertidas de R a Python
    para el análisis de interacciones miRNA-mRNA utilizando el modelo PTC (Pseudo-Temporal Causality).</p>

    <h2>Funciones Convertidas</h2>
    
    <p>Devuelve una lista con todas las interacciones miRNA-mRNA confirmadas experimentalmente, 
    basadas en una lista de interacciones inferidas.</p>
    <div class="code-block">
        <span class="function-name">confirmed_from_list</span>
    </div>

    <p>Filtra una matriz de interacciones miRNA-mRNA para devolver solo aquellas que están presentes 
    en una base de datos de interacciones confirmadas.</p>
    <div class="code-block">
        <span class="function-name">confirmed_from_matrix</span>
    </div>

    <p>Extrae los posibles padres causales (miRNAs) para un conjunto de mRNAs, basándose en los 
    resultados de PTC.GeneSel y PTC.TestInvariance.</p>
    <div class="code-block">
        <span class="function-name">extract_parents</span>
    </div>

    <p>Convierte una lista de interacciones miRNA-mRNA en una matriz donde cada fila representa 
    una interacción.</p>
    <div class="code-block">
        <span class="function-name">interlist_to_matrix</span>
    </div>

    <p>Convierte una matriz de interacciones miRNA-mRNA en una lista donde cada mRNA está asociado 
    con los miRNAs que pueden unirse a él.</p>
    <div class="code-block">
        <span class="function-name">intermatrix_to_list</span>
    </div>

    <p>Selecciona un conjunto de miRNAs y mRNAs basado en la Mediana de Desviación Absoluta (MAD) 
    para su uso en análisis de causabilidad temporal.</p>
    <div class="code-block">
        <span class="function-name">ptc_gene_sel</span>
    </div>

    <p>Realiza la estimación de padres causales de un conjunto de mRNAs utilizando un modelo lineal 
    y un análisis de invariancia.</p>
    <div class="code-block">
        <span class="function-name">ptc</span>
    </div>

    <p>Clasifica una matriz de relaciones miRNA-mRNA utilizando puntajes de contexto conservado 
    de TargetScan 7.0.</p>
    <div class="code-block">
        <span class="function-name">ptc_rank_by_context</span>
    </div>

    <p>Encuentra un conjunto de miRNAs que son padres causales de un mRNA objetivo utilizando 
    pruebas de invariancia secuencial.</p>
    <div class="code-block">
        <span class="function-name">ptc_test_invariance</span>
    </div>
</body>
</html>
