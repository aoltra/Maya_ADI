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

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.base import TransformerMixin
from sklearn import svm
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# al no haber modelo (sólo tokeniza, y tiene stop words) es mejor realizar la carga con el
# import, no con load
from spacy.es import Spanish

# Cada paso del pipeline necesita ser un objeto con la función transform (trasformación), salvo
# el último que obligatoriamamete ha de tener la función fit (estimación)
# Hereda de la clase TransformerMixin que implementa el método fit_transform, que primero
# hace un fit y luego lo transforma, luego es necesario definir esas dos funciones
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

    # obtiene los parámetros de esta transformación a partir de la lista
    # de parámetros de la pipeline
    # Esta transformación no permite parámetros
    def get_params(self, deep=True):
        return {}


# Limpia el texto antes de ser enviado a Tokenizing
def limpiaTexto(text):

    # todo a minúsculas
    text = text.lower()

    # Elimino signos de puntuación
    text = text.replace("?", "").replace("¿", "").replace(",", "")
    text = text.replace(";", "").replace(":", "").replace("maya", "")
    text = text.strip()

    return text



# Imprime las propiedades de cada una de las clases en orden decreciente
# N: número de propiedades a mostrar
def imprimeCoeficientesPropiedades(vectorizador, clf, N):
    """
    Imprime las propiedades de cada una de las clases en orden decreciente
    """

    print("------------------------------------")
    print("COEFICIENTES PROPIEDADES IMPORTANTES")
    print("------------------------------------")
    nombrePropiedades = vectorizador.get_feature_names()
    coefs_con_propiedades = sorted(zip(clf.coef_.data, nombrePropiedades))
    topClass0 = coefs_con_propiedades[:N]
    topClass1 = coefs_con_propiedades[:-(N + 1):-1]
    print("\nSENTENCIAS NO RELEVANTES\n------------------------")
    for feat in topClass0:
        print(feat)
    print("\nSENTENCIAS RELEVANTES\n----------------------")
    for feat in topClass1:
        print(feat)


# Stop words o palabras vacías. Son las palabras sin significado como artículos,
# pronombres, preposiciones...
# Como a priori no aportan significado se eliminan de la frases
# Se contruye a partir de la lista de palabras vacias de ntlk más de la spaCy
STOPLIST = Spanish.Defaults.stop_words

# A partir del dataset genero dos ficheros para poder tratarlos como iterators
# a la hora de crear el modelo
entrenamiento = []
etiquetaEntrenamiento = []

ficheroDataset = open('dataset_E1.temporal.raw', 'rU')

with open('dataset_E1.temporal.raw', 'rU') as ficheroDataset:
    for linea in ficheroDataset:
        lineaPartida = linea.split(";")
        entrenamiento.append(lineaPartida[0])
        etiquetaEntrenamiento.append(lineaPartida[1].replace("\n", ""))

# Extracción de texto
# Con CountVectorizer (obtenido de la libreria sklearn) creo los tokens y realizo el conteo
# se excluyen las palabras vacias
# uso 1-gramas, luego no tengo en cuenta el orden de las palabras, se toma cada token por separado
# El tokenizador incluido no tiene en cuenta ningun tipo de análisis semántico, se puede implementar
# en un futuro creando una funcion que procesaria con spaCy cada entrada nlp(sample)
vectorizador = CountVectorizer(stop_words=STOPLIST, ngram_range=(1, 1))
# TfidfVectorizer evita estadisiticamente toknes que se repitan mucho. Por ahora no aporta mejoras

# Algoritmo clasificador
clasificador = svm.SVC(kernel='linear', C=1)
# Otras opciones
# SVC(kernel='rbf', gamma=0.7, C=1)
# SVC(kernel='poly', degree=3, C=1)
# SVC(kernel='linear', C=1)
# LinearSVC(C=1)

# Creación de la secuencia de procesos para la creación del modelo.
# Se define una cadena de pares (nombre, objetos transformacion)
# Es posible incorporar parámetros a la pipeline completa utilizando
# nombretransformación__nombreparametro
# se ejecutan con fit y predict
# todas las transformaciones han de implementar el método transform,
# salvo la última que en vez de transform necesita el método fit
# A la última se le llama estimación
pipe = Pipeline([('limpiar', LimpiarTextoTransf()), ('vectorizar', vectorizador),
                 ('clasificar', clasificador)])

# entrenamiento
# ajusta el modelo ejecutando todas las transformaciones del pipeline y la estimación final
pipe.fit(entrenamiento, etiquetaEntrenamiento)

# pruebas para clasificar
test = ["¿Está la ventana abierta?", "Maya, las mañanas son muy duras",
    "Habría que comprar azúcar", "Tengo que trabajar mucho",
    "¿a qué hora está puesto el despertador?", "apunta media sandia", "¿Esta tarde va a hacer sol?",
    "Son los efectos colaterales", "Añade chocolate a la lista de la compra", "Esto no va",
    "¿Has cerrado la puerta?","Generalmente la alergia al polen se puede dar a cualquier edad (como las demás alergias)",
    "Mañana me quiero despertar a las once","Me estoy lavando los dientes","Mañana es fiesta y hay que hacer la compra",
    "Me cedes el asiento","La vida es una tómbola","Adelanta la hora","Hoy me apetece comer pan",
    "Compra unos filetes de ternera"]
etiquetasTest= ["0", "0", "1", "0", "1", "1", "1", "0", "1", "0", "0", "0", "1", "0", "1", "0", "0", "1",
    "0", "1"]
preds = pipe.predict(test)

for (sample, pred, etiqueta) in zip(test, preds, etiquetasTest):
    if pred != etiqueta:
        print('\x1b[0;31;40m' + sample + ": P(" + pred + ') != E(' + etiqueta + ')\x1b[0m')
    else:
        print('\x1b[0;32;40m' + sample + ": P(" + pred + ') == E(' + etiqueta + ')\x1b[0m')

print("\nPrecisión:", accuracy_score(etiquetasTest, preds),"\n")

imprimeCoeficientesPropiedades(vectorizador, clasificador, 20)


print("--------------------------------------------------------------------------------------------")
print("Datos que llegan al clasificador después de tokenizar y quitar palabras vacias")

pipe = Pipeline([('cleanText', LimpiarTextoTransf()), ('vectorizer', vectorizador)])
transform = pipe.fit_transform(entrenamiento,etiquetaEntrenamiento)

# vocabulario
vocab = vectorizador.get_feature_names()

for i in range(len(entrenamiento)):
     s = ""
     idxEnVocabulario = transform.indices[transform.indptr[i]:transform.indptr[i+1]]
     numOcurrencias = transform.data[transform.indptr[i]:transform.indptr[i+1]]
     for idx, num in zip(idxEnVocabulario, numOcurrencias):
         s += str((vocab[idx], num))
         print("Muestra {}: {}".format(i, s))
