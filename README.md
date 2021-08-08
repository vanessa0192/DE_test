# 1. Creamos una variable de entorno
CLUSTERNAME=dplab-yourname
 
# 2. Configuramos la region de DATAPROC
gcloud config set dataproc/region us-central1
 
# 3. Creamos el cluster
gcloud dataproc clusters create ${CLUSTERNAME} \
  --scopes=cloud-platform \
  --tags qwiklab \
  --zone=us-central1-c \
  --worker-machine-type n1-standard-2 \
  --worker-boot-disk-size 500 \
  --master-machine-type n1-standard-2 \
  --master-boot-disk-size 500 \
  --image-version 2.0
 
# 4. Ejecutar un Job en un cluster de dataproc
gcloud dataproc jobs submit spark \
  --cluster ${CLUSTERNAME} \
  --class org.apache.spark.examples.SparkPi \
  ##--
 
# 5. Listar los Jobs asignados a un cluster
gcloud dataproc jobs list --cluster ${CLUSTERNAME}
 
# 6. Describir la configuracion con la que se creo un cluster
gcloud dataproc clusters describe ${CLUSTERNAME}