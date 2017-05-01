# Generación de modelos

## Configuración

Para la generación de cada modelo es necesario:

* carpeta [modelo]/corpus. Ficheros con el corpus. El corpus 0a se puede generar a partir del fichero *arff* mediante el script *+arff2corpus.awk**


## Creación del modelo

Desde la carpeta del modelo ejecutar:

~~~
python3 ../../../vendors/spacy-dev-resources/training/plain_word_freqs.py "corpus/*a.txt" ./freq_word/es_maya_sm_freq.txt
~~~

