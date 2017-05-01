# Convierte el conjunto de datos en formato ARFF en una lista de sentencias
# que forman parte del corpus
# Ejecución
#     awk -f arff2corpus.awk ../dataset.arff > ./corpus/corpus_maya_0a.txt

BEGIN {
  data=0;
  FS="\","
}

# estamos en el bloque de datos y no empieza por %
data == 1 && /^[^%]/ && /^\"/ {
  if ($2!=0) print substr($1, 2, length($1) - 1);
}
/^@DATA/ { data=1; }
