<h1 align="center"><br>
PTC Python Functions<br>
Fase Preliminar 🤖 <br> 
Un enfoque de causalidad pseudotemporal para identificar interacciones miARN-ARNm durante procesos biológicos<br> 
AndresMCB <br> 
2024 📅</h1><br>
<h2>👨‍💻 Python 🐍</h2>
    
<h1>PTC Python Functions - README</h1>
    <p>Este documento proporciona un breve resumen de las funciones convertidas de R a Python
    para el análisis de interacciones miRNA-mRNA utilizando el modelo PTC (Pseudo-Temporal Causality).</p>

<h2>Funciones Convertidas</h2>
    <p class="function-name">confirmed_from_list</p>
    <p>Devuelve una lista con todas las interacciones miRNA-mRNA confirmadas experimentalmente, 
    basadas en una lista de interacciones inferidas.</p>

<p class="function-name">confirmed_from_matrix</p>
    <p>Filtra una matriz de interacciones miRNA-mRNA para devolver solo aquellas que están presentes 
    en una base de datos de interacciones confirmadas.</p>

    <p class="function-name">extract_parents</p>
    <p>Extrae los posibles padres causales (miRNAs) para un conjunto de mRNAs, basándose en los 
    resultados de PTC.GeneSel y PTC.TestInvariance.</p>

    <p class="function-name">interlist_to_matrix</p>
    <p>Convierte una lista de interacciones miRNA-mRNA en una matriz donde cada fila representa 
    una interacción.</p>

    <p class="function-name">intermatrix_to_list</p>
    <p>Convierte una matriz de interacciones miRNA-mRNA en una lista donde cada mRNA está asociado 
    con los miRNAs que pueden unirse a él.</p>

    <p class="function-name">ptc_gene_sel</p>
    <p>Selecciona un conjunto de miRNAs y mRNAs basado en la Mediana de Desviación Absoluta (MAD) 
    para su uso en análisis de causabilidad temporal.</p>

    <p class="function-name">ptc</p>
    <p>Realiza la estimación de padres causales de un conjunto de mRNAs utilizando un modelo lineal 
    y un análisis de invariancia.</p>

    <p class="function-name">ptc_rank_by_context</p>
    <p>Clasifica una matriz de relaciones miRNA-mRNA utilizando puntajes de contexto conservado 
    de TargetScan 7.0.</p>

    <p class="function-name">ptc_test_invariance</p>
    <p>Encuentra un conjunto de miRNAs que son padres causales de un mRNA objetivo utilizando 
    pruebas de invariancia secuencial.</p>
