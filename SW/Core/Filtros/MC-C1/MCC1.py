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
# pylint: disable=unused-import
from LimpiarTextoTransf import LimpiarTextoTransf

PIPELINE = joblib.load('MCC1.mym')

PREDICCION = PIPELINE.predict(["¡Hola, buenos días!"])

if PREDICCION[0] == "0":
    print('No relevante')
else:
    print('Relevante')
