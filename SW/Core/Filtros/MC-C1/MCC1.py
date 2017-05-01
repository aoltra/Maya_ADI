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
import sys
from sklearn.externals import joblib
# pylint: disable=unused-import
from LimpiarTextoTransf import LimpiarTextoTransf

def main():
    """
    Función de arranque del script
    """

    if len(sys.argv) != 2:
        print("No existe una definición clara del texto a procesar. Tal vez falten comillas")
        sys.exit()

    texto = []
    texto.append(sys.argv[1])

    pipeline = joblib.load('MCC1.mym')

    prediccion = pipeline.predict(texto)

    if prediccion[0] == "0":
        print('No relevante')
    else:
        print('Relevante')

if __name__ == "__main__":
    main()
