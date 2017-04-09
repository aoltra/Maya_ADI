# MAYA. Intelligent Domestic Assistant

## Índice

[Introducción](#Introduccion)
[Hardware](#Hardware)
  [Topología](#Topologia)

## Introducción

MAYA tiene por objetivo crear un asistente doméstico inteligente (IDA) para personas mayores con minusvalías (en particular minusvalías visuales).

El contexto en el que se mueve es en el de personas que debido a su minusvalía y a su edad no puede aprovechar de la manera más eficiente la tecnología actual para resolver problemas de su día a día.

## Hardware

### Topología

## Software

### Arquitectura

### Herramientas

#### Python 3.X

**macOs**
> La instalación de XCode trae de serie la versión 2.X de Python. Para evitar problemas con el gestor de paquetes [pip](https://pypi.python.org/pypi/pip), es recomendable utilizar Python 3.X.

La instalación se puede realizar a partir de la descarga del instalador desde la [página oficial de Pyhton](https://www.python.org/downloads/). Para su uso desde consola hay que utilizar el comando `python3`

#### pip

*pip* es el gestor de paquetes que utilizaremos para la descarga y actualización de las librerías necesarias. Viene por defecto con python 3.X. Para actualizarlo:

~~~
pip3 install --upgrade pip
~~~

#### spaCy

[spaCy](https://spacy.io/) es una librería desarrollada en Python para realizar Procesamiento de Lenguaje Natural (NLP). Se distribuye con licencia [MIT](https://opensource.org/licenses/MIT).

#### scikit-learn

[Scikit-learn](http://scikit-learn.org/stable/) es la principal librería que existe para trabajar con Machine Learning, incluye la implementación de un gran número de algoritmos de aprendizaje. La podemos utilizar para clasificaciones, extraccion de características, regresiones, agrupaciones, reducción de dimensiones, selección de modelos, o preprocesamiento[\*](http://relopezbriega.github.io/blog/2015/10/10/machine-learning-con-python/#Scikit-Learn). Se distribuye con licencia [BSD](https://www.freebsd.org/copyright/freebsd-license.html).

## Licencia

El proyecto está liberado bajo licencia [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0-standalone.html) salvo en aquellos submódulos que tienen su licencia específica.
