# Maya Core - Filtros

## Índice

  [MC-C1](#MC-C1. Clasificador nivel 1).

## MC-C1. Clasificador nivel 1

## Introducción

El clasificador de nivel 1 (MC-C1) consiste en la determinación de si la sentencia de entrada es relevante o no.
Para ello se utiliza un sistema de aprendizaje automático supervisado que utiliza un conjunto de datos (*Dataset*) en formato [ARFF](https://weka.wikispaces.com/ARFF). El fichero tiene como atributos:

  * sentencia
  * módulo al que pertenece: ID del módulo (0 no relevante)

La implementación del mismo se realiza en dos fases:

  * **Creación del modelo**. Una vez creados los datos y entrenados, estos se preparan para ser introducidos en diferentes algoritmos que generarán sus correspondientes modelos. Esos modelos se evaluan para encontrar cual de ellos obtiene la mejor precisión (o si es necesario se mejora el entrenamiento)

  * **Uso del modelo**. El modelo elegido se pone en funcionamiento en el entorno indicado.

## Creación del modelo. Pipeline

El proceso de creación del modelo consiste en una serie de pasos secuenciales (pipeline):

  1. El *Dataset* es preprocesado para generar un fichero con los atributos: *sentencia* y *relevante*, separados por ;

  2. Se preprocesa el fichero que se obtiene del paso anterior para que pueda ser procesado por el algoritmo.

  Se trabaja con la técnica de *Bag of Words* (BOW) o bolsa de palabras, donde se ignora el orden de las palabras. Simplemente se crea un vocabulario basándonos en las veces que una palabra aparece en el dataset. Las principales ventajas de utilizar este modelo es su facilidad de uso y su eficiencia computacional. En general la mayoría de algoritmos esperan la información de entrada en forma de vectores númericos obtenidos de las propiedades del texto, no el texto puro. Para conseguirlo se realizan varios procesos:

   * *Tokenizing*: consiste en la obtención de bloques que componen el texto y asignarles un identificador. Estos bloques pueden ser palabras o conjuntos de palabras.

   * *Counting*: es el contado de cada una de las apariciones de cada token en los datos.

   * *Normalizado* y ponderación de los tokens con importancia decreciente.
    
  > Existen otras tareas como el etiquetado de voz (*part-of-speech tagging*, POS), el troceo de frases, el reconocimiento de entidades nombradas (*NER*) y el etiquetado de roles semánticos (*SRL*) que son importantes para el análisis semántico (se utilizan en los plugins)

