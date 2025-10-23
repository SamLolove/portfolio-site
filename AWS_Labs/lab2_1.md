# Lab 2.1: Explorando AWS CloudShell y el IDE integrado
---
##  Objetivo
Familiarizarse con **AWS CloudShell** como entorno de desarrollo, verificar herramientas como **AWS CLI** y el **SDK para Python**, y practicar comandos básicos para interactuar con **Amazon S3**.
---
##  Pasos realizados

1. Se accedió al ícono de **AWS CloudShell** desde la consola de administración de AWS.  
2. Se verificó la instalación de la CLI ejecutando:

   ```bash
   aws --version
1. Se accedió al ícono de **AWS CloudShell** desde la consola de administración de AWS.  
2. Se verificó la instalación de la CLI ejecutando:

   ```bash
   aws --version
Se probó un comando básico de AWS CLI:

aws s3 ls

Obteniendo el nombre del bucket creado automáticamente.

Se dividió la pantalla del terminal en columnas para usar múltiples sesiones.

Se cargó el archivo list-buckets.py al entorno de CloudShell.

Se verificó el contenido del archivo con:

cat list-buckets.py


Se ejecutó el código Python para listar los buckets de S3:

python3 list-buckets.py


Se comparó la salida con el resultado del comando CLI.

Se copió el archivo list-buckets.py a un bucket S3 mediante:

aws s3 cp list-buckets.py s3://<bucket-name>


Se revisó el almacenamiento persistente de CloudShell ejecutando:

df -H /home

Resultado
Se comprobó el funcionamiento correcto de CloudShell como entorno de línea de comandos persistente, capaz de ejecutar tanto CLI como scripts SDK en Python para la administración de recursos AWS.

Parte 2: Usar AWS CloudShell IDE
Se accedió al entorno de VS Code IDE utilizando la URL y contraseña proporcionadas.
Se identificaron los componentes de la interfaz: panel de navegación, editor y terminal Bash.

Se listaron los buckets disponibles con:
aws s3 ls

Se descargó el archivo list-buckets.py desde S3 al entorno local:
aws s3 cp s3://<bucket-name>/list-buckets.py .
Se abrió el archivo y se intentó ejecutar con Python 3, encontrando el error de módulo faltante boto3.
Se instaló el SDK de AWS para Python con:
sudo pip3 install boto3

Se ejecutó nuevamente el script obteniendo el listado de buckets correctamente.
Se creó un nuevo archivo index.html con contenido básico:

<body>Hello World.</body>

Se cargó este archivo al bucket S3 mediante:

aws s3 cp index.html s3://<bucket-name>/index.html
Resultado

Se validó la integración del IDE con AWS CLI y S3, logrando ejecutar scripts Python con boto3 y alojar un archivo HTML en un bucket S3.
Esto demuestra la utilidad del entorno para desarrollo y despliegue de contenido.

# CAPTURA DEL LABORATORIO TERMINADO

![Texto alternativo](/imagenes/lab2_1.png "Título opcional")


Conclusión
El laboratorio permitió comprobar las capacidades de AWS CloudShell como entorno CLI preconfigurado y de VS Code IDE como entorno de desarrollo completo sobre AWS.
Ambas herramientas facilitan la ejecución de scripts, administración de recursos y despliegue de archivos hacia servicios como Amazon S3, optimizando el flujo de trabajo para desarrolladores y administradores en la nube.