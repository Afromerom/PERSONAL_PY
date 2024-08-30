<h1 align="center"><br>
PTC Python Functions<br>
Fase Preliminar 🤖 <br> 
Un enfoque de causalidad pseudotemporal para identificar interacciones miARN-ARNm durante procesos biológicos<br> 
AndresMCB <br> 
2024 📅</h1><br>

## 👨‍💻 Python 🐍

## PTC Python Functions - README

Este documento proporciona un breve resumen de las funciones convertidas de R a Python para el análisis de interacciones miRNA-mRNA utilizando el modelo PTC (Pseudo-Temporal Causality).

## Funciones Convertidas

### `confirmed_from_list`
Devuelve una lista con todas las interacciones miRNA-mRNA confirmadas experimentalmente, basadas en una lista de interacciones inferidas.

### `confirmed_from_matrix`
Filtra una matriz de interacciones miRNA-mRNA para devolver solo aquellas que están presentes en una base de datos de interacciones confirmadas.

### `extract_parents`
Extrae los posibles padres causales (miRNAs) para un conjunto de mRNAs, basándose en los resultados de PTC.GeneSel y PTC.TestInvariance.

### `interlist_to_matrix`
Convierte una lista de interacciones miRNA-mRNA en una matriz donde cada fila representa una interacción.

### `intermatrix_to_list`
Convierte una matriz de interacciones miRNA-mRNA en una lista donde cada mRNA está asociado con los miRNAs que pueden unirse a él.

### `ptc_gene_sel`
Selecciona un conjunto de miRNAs y mRNAs basado en la Mediana de Desviación Absoluta (MAD) para su uso en análisis de causabilidad temporal.

### `ptc`
Realiza la estimación de padres causales de un conjunto de mRNAs utilizando un modelo lineal y un análisis de invariancia.

### `ptc_rank_by_context`
Clasifica una matriz de relaciones miRNA-mRNA utilizando puntajes de contexto conservado de TargetScan 7.0.

### `ptc_test_invariance`
Encuentra un conjunto de miRNAs que son padres causales de un mRNA objetivo utilizando pruebas de invariancia secuencial.
