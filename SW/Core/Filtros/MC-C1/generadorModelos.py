# coding=utf-8
# GeneradorModelos
#
# Procesa el dataset con spaCy mediante diferentes algoritmos
# Basado en el código de nicschrading
# http://nicschrading.com/project/Intro-to-NLP-with-spaCy/
#
# Autor: Alfredo Oltra
# Fecha: 9/4/2017
#

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import TransformerMixin
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

# Cada paso del pipeline necesita ser un objeto con la función transform (trasformación), salvo el último que
# obligatoriamamete ha de tener la función fit (estimación)
# Hereda de la clase TransformerMixin que implementa el método fit_transform, que primero hace un fit
# y luego lo transforma, luego es necesario definir esas dos funciones
class LimpiarTextoTransf(TransformerMixin):
    ## documentación
    """
    Transformación que limpia el texto
    """

    # se encarga de realizar un ajuste, de realizar un trabajo, en los datos.
    # Aunque se puede realizar en las transformaciones, tiene sentido en la estimación
    # X son los datos a entrenar e Y los correspondientes valores de su entrenamiento
    def fit(self, X, y=None, **fit_params):
        return self

    # transforma los datos a otro formato o los simplifica
    # transform_params es un número indeterminado de tuplas
    def transform(self, X, **transform_params):
        return [limpiaTexto(text) for text in X]

    # obtiene los parámetros de esta transformación a partir de la lista de parámetros de la pipeline
    # Esta transformación no permite parámetros
    def get_params(self, deep=True):
        return {}


# Limpia el texto antes de ser enviado a Tokenizing
def limpiaTexto(text):

    # Elimino signos de puntuación
    text = text.replace("?", "").replace("¿", "").replace(",", "").replace(";", "").replace(":", "")

    # todo a minúsculas
    text = text.lower()

    return text

# A partir del dataset genero dos ficheros para poder tratarlos como iterators a la hora de crear el modelo
entrenamiento = []
etiquetaEntrenamiento = []

ficheroDataset = open('dataset_E1.temporal.raw', 'rU')

with open('dataset_E1.temporal.raw', 'rU') as ficheroDataset:
    for linea in ficheroDataset:
        lineaPartida = linea.split(";")
        entrenamiento.append(lineaPartida[0])
        etiquetaEntrenamiento.append(lineaPartida[1])

# Extracción de texto
# Con CountVectorizer (obtenido de la libreria sklearn) creo los tokens y realizo el conteo
vectorizador = CountVectorizer()

# Algoritmo Clasificador
clasificador = LinearSVC();

# Creación de la secuencia de procesos para la creación del modelo.
# Se define una cadena de pares (nombre, objetos transformacion)
# Es posible incorporar parámetros a la pipeline completa utilizando nombretransformación__nombreparametro
# se ejecutan con fit y predict
# todas las transformaciones han de implementar el método transform, salvo la última que en vez de transform necesita el método fit
# A la última se le llama estimación
pipe = Pipeline([('limpiar', LimpiarTextoTransf()), ('vectorizar', vectorizador), ('clasificar', clasificador)])

# entrenamiento
# ejecuta todas las transformaciones del pipeline y del último (estimación)
pipe.fit(entrenamiento,etiquetaEntrenamiento)

test = ["Me cago en la mar", "Maya, pon una canción", "habría que comprar azúcar"]
preds = pipe.predict(test)
for (sample, pred) in zip(test, preds):
    print(sample, ":", pred)
