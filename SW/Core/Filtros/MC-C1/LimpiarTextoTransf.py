# coding=utf-8
# LimpiarTextoTransf
#
# Transformaion para limpiar la cadena para que su procesamiento sea mejor
#
# Autor: Alfredo Oltra
# Fecha: 18/4/2017
#

"""
Limpiar la cadena para que su procesamiento sea mejor
"""

from sklearn.base import TransformerMixin

# Hereda de la clase TransformerMixin que implementa el método fit_transform, que primero
# hace un fit y luego lo transforma, luego es necesario definir esas dos funciones
# Cada paso del pipeline necesita ser un objeto con la función transform (trasformación), salvo
# el último que obligatoriamamete ha de tener la función fit (estimación)
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
