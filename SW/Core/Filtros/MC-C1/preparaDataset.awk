# Convierte el conjunto de datos en formato ARFF en una lista de instancias
# sentencia y propiedad relevante (!=0)/no relevante (==0)
# Ejecución
#     awk -f preparaDataset.awk ../../modelos/dataset.arff > dataset_E1.temporal.raw

BEGIN {
  data=0;
  FS="\","
}

# estamos en el bloque de datos y no empieza por %
data == 1 && /^[^%]/ && /^\"/ {
  printf substr($1, 2, length($1) - 1);
  if ($2!=0) print ";1"; else print ";0";
}
/^@DATA/ { data=1; }
