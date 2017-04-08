# Maya Core - Filtros

## Índice

[MC-C1](MC-C1.-Clasificador-nivel-1)
[MC-C2](#Hardware)

## MC-C1. Clasificador nivel 1

## Introducción

La etapa 1 consiste en la determinación de si la sentencia de entrada es relevante o no.
Para ello se utiliza un sistema de apredendizaje automático supervisado. El sistema utiliza un conjunto de datos (*Dataset*) en formato [ARFF](https://weka.wikispaces.com/ARFF)

El fichero tiene como atributos:

  * sentencia
  * módulo al que pertenece: ID del módulo (0 no relevante)

## Pipeline

El *Dataset* es preprocesado para generar un fichero ARFF con los atributos:

  * sentencia
  * relevante o no relevante [0,1] 
