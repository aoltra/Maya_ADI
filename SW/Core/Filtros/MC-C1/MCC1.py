# coding=utf-8
# MCC1
#
# Ejecuta el filtro 1: relevante/no relevante
#
# Autor: Alfredo Oltra
# Fecha: 17/4/2017
#

"""
Ejecuta el filtro 1 (MCC1): relevante/no relevante
"""

from sklearn.externals import joblib
from sklearn.base import TransformerMixin

class LimpiarTextoTransf(TransformerMixin):
    ## documentación
    """
    Transformación que limpia el texto
    """

    def fit(self, X, y=None, **fit_params):
        """
        Se encarga de realizar un ajuste, de realizar un trabajo, en los datos.
        Aunque se puede realizar en las transformaciones, tiene sentido en la estimación
        X son los datos a entrenar e Y los correspondientes valores de su entrenamiento
        """

        del X
        del y
        del fit_params
        return self

    def transform(self, X, **transform_params):
        """
        Transforma los datos a otro formato o los simplifica
        transform_params es un número indeterminado de tuplas
        """
        del transform_params

        return [limpia_texto(text) for text in X]


    def get_params(self, deep=True):
        """
        Obtiene los parámetros de esta transformación a partir de la lista
        de parámetros de la pipeline
        Esta transformación no permite parámetros
        """

        del deep
        return {}


def limpia_texto(text):
    """
    Limpia el texto antes de ser enviado a Tokenizing
    """

    # todo a minúsculas
    text = text.lower()

    # Elimino signos de puntuación
    text = text.replace("?", "").replace("¿", "").replace(",", "")
    text = text.replace(";", "").replace(":", "").replace("maya", "")
    text = text.strip()

    return text


PIPELINE = joblib.load('MCC1.mym')

PREDICCION = PIPELINE.predict(["¡Hola, buenos días!"])

if PREDICCION[0] == "0":
    print('No relevante')
else:
    print('Relevante')
