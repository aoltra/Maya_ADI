# GeneradorModelos
#
# Procesa el dataset con spaCy mediante diferentes algortimos
# Basado en el código de nicschrading
# http://nicschrading.com/project/Intro-to-NLP-with-spaCy/
#
# Autor: Alfredo Oltra
# Fecha: 9/4/2017
#

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC

# Extracción de texto
# Con CountVectorizer (obtenido de la libreria sklearn) creo los tokens y realizo el conteo
vectorizador = CountVectorizer()

# Algoritmo Clasificador
clasificador = LinearSVC();
