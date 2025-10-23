#  Lab 7.1: Creating Lambda Functions Using the AWS SDK for Python

# CAPTURA DEL LABORATORIO TERMINADO

![Texto alternativo](/imagenes/lab7_1.jpg "Título opcional")

## Objetivo
Crear, desplegar, invocar y actualizar una **función AWS Lambda** usando **AWS SDK for Python (Boto3)** desde **CloudShell** o el **IDE del laboratorio**.  
Además, practicar la creación de un **paquete .zip**, la **invocación** desde CLI, la configuración de **variables de entorno**, el manejo de **versiones/aliases**, la consulta de **logs** y la **limpieza de recursos**.


## Ambiente
- **Alumno:** JESUS JHAIR CHAN INFANTE  
- **Curso/Sección:** Cómputo de Alto Desempeño  
- **Fecha de realización:** 05/10/2025 – 12:16  
- **Plataforma:** AWS Academy (Canvas + Vocareum)  
- **Evidencia en Canvas:** _Submission Details_ (calificación y marca de tiempo)  
- **Cuenta:** Temporal del laboratorio (recursos efímeros)  
- **Región:** `<REGION>` (por ejemplo: `us-east-1`)  
- **Herramientas:** AWS CloudShell o IDE del lab, **Python 3.x**, **Boto3**, **AWS CLI v2**

## Pasos realizados

### 1️ Verificar identidad y entorno
Se accedió a **AWS CloudShell** desde la consola.  
Se verificó la configuración de credenciales y región activa:

## Crear el archivo de función Lambda
```bash
aws sts get-caller-identity
aws configure list

cat > lambda_function.py << 'PY'
import json

def lambda_handler(event, context):
    message = "Hola desde Lambda con Boto3"
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
PY
zip function.zip lambda_function.py

##Crear la función Lambda con AWS CLI
aws lambda create-function \
  --function-name Lab7_Lambda_Boto3 \
  --runtime python3.12 \
  --role arn:aws:iam::<ACCOUNT_ID>:role/LabRole \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip \
  --region <REGION>

##Invocar la función Lambda
aws lambda invoke \
  --function-name Lab7_Lambda_Boto3 \
  --payload '{}' \
  response.json

cat response.json

##Actualizar la función y agregar variables de entorno
aws lambda update-function-configuration \
  --function-name Lab7_Lambda_Boto3 \
  --environment "Variables={ENTORNO='Lab7',AUTOR='SamanthaDuran'}"

aws lambda invoke \
  --function-name Lab7_Lambda_Boto3 \
  --payload '{}' \
  output.json
cat output.json


##Consultar logs en CloudWatch y se Limpieza de recursos
aws lambda delete-function --function-name Lab7_Lambda_Boto3 --region <REGION>

```bash

##  Resultados

- La función **Lambda** se creó y ejecutó exitosamente desde la **CLI**.  
- Se verificó la salida `"Hola desde Lambda con Boto3"`.  
- Los logs de ejecución se registraron correctamente en **CloudWatch**.  
- Se probaron **actualizaciones** y **variables de entorno**.  
- Todos los recursos fueron **eliminados correctamente** al finalizar.

---

## Conclusión

El laboratorio permitió poner en práctica el uso del **AWS SDK for Python (Boto3)** y la **CLI** para gestionar funciones **AWS Lambda**.  

Se reforzaron los conceptos de **creación**, **invocación** y **actualización** de funciones sin servidor, así como la interacción con **CloudWatch Logs** y el manejo de **configuraciones dinámicas** mediante **variables de entorno**.  

Finalmente, se validó el funcionamiento correcto de **AWS Lambda** y se consolidó la experiencia práctica en **computación sin servidor (serverless)**.



