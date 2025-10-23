#  Lab 5.1: Working with Amazon DynamoDB

# CAPTURA DEL LABORATORIO TERMINADO

![Texto alternativo](/imagenes/lab5_1.png "Título opcional")

## 1) Objetivo
Crear y operar una tabla en **Amazon DynamoDB** para:  
- Diseñar una **clave de partición** (y opcionalmente una **clave de ordenamiento**).  
- Cargar elementos usando **PutItem**, **BatchWriteItem** o **PartiQL**.  
- Consultar con **Query**, **Scan** y filtros.  
- Probar **índices secundarios** (LSI/GSI).  
- Ejecutar **condiciones de escritura** y **actualizaciones atómicas**.  
- Activar **TTL** y realizar **backup/restore** (si el laboratorio lo permite).  
- Limpiar recursos creados.  


## 2) Ambiente
- **Cuenta:** Temporal del laboratorio (credenciales efímeras)  
- **Región de trabajo:** `<REGIÓN>`  
- **Herramientas:** AWS Management Console, AWS CloudShell, AWS CLI v2  


## 3) Actividades realizadas (resumen)
1. Crear una tabla DynamoDB con clave primaria simple o compuesta.  
2. Verificar el estado y descripción de la tabla.  
3. Insertar elementos con comandos de la CLI o código Python.  
4. Consultar y filtrar registros mediante **Query** y **Scan**.  
5. Crear índices secundarios (GSI/LSI) y probar sus consultas.  
6. Activar TTL y explorar opciones de backup.  
7. Limpiar todos los recursos creados.  

## 4) Pasos y comandos clave (CloudShell / CLI)
> Sustituye `<REGION>`, `<TABLE>`, `<PK>`, `<SK>` y tipos `S|N` según tu diseño.

```bash
## Ver identidad y configuración
aws sts get-caller-identity
aws configure list

# (4.1) Crear tabla con PK y SK en modo On-Demand
aws dynamodb create-table \
  --table-name <TABLE> \
  --attribute-definitions AttributeName=<PK>,AttributeType=S AttributeName=<SK>,AttributeType=S \
  --key-schema AttributeName=<PK>,KeyType=HASH AttributeName=<SK>,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST \
  --region <REGION>

# (Si NO usarás SK, usa esta variante)
# aws dynamodb create-table \
#   --table-name <TABLE> \
#   --attribute-definitions AttributeName=<PK>,AttributeType=S \
#   --key-schema AttributeName=<PK>,KeyType=HASH \
#   --billing-mode PAY_PER_REQUEST \
#   --region <REGION>

# Esperar a que la tabla esté activa
aws dynamodb wait table-exists --table-name <TABLE> --region <REGION>

# Describir la tabla creada
aws dynamodb describe-table --table-name <TABLE> --region <REGION>

# (4.2) Insertar elementos de prueba
aws dynamodb put-item \
  --table-name <TABLE> \
  --item '{"<PK>":{"S":"ID001"},"<SK>":{"S":"2025-10-15"},"Producto":{"S":"Café Latte"},"Precio":{"N":"60"}}' \
  --region <REGION>

# Insertar múltiples elementos con BatchWrite
cat > batch-items.json << 'JSON'
{
  "RequestItems": {
    "<TABLE>": [
      {
        "PutRequest": {
          "Item": {
            "<PK>": {"S": "ID002"},
            "<SK>": {"S": "2025-10-15"},
            "Producto": {"S": "Café Americano"},
            "Precio": {"N": "40"}
          }
        }
      },
      {
        "PutRequest": {
          "Item": {
            "<PK>": {"S": "ID003"},
            "<SK>": {"S": "2025-10-16"},
            "Producto": {"S": "Cappuccino"},
            "Precio": {"N": "55"}
          }
        }
      }
    ]
  }
}
JSON

aws dynamodb batch-write-item --request-items file://batch-items.json --region <REGION>
# (4.3) Consultar la tabla
aws dynamodb scan --table-name <TABLE> --region <REGION>

# Consultar con filtro
aws dynamodb scan \
  --table-name <TABLE> \
  --filter-expression "Precio > :p" \
  --expression-attribute-values '{":p":{"N":"45"}}' \
  --region <REGION>
# (4.4) Crear un índice secundario global (GSI)
aws dynamodb update-table \
  --table-name <TABLE> \
  --attribute-definitions AttributeName=Producto,AttributeType=S \
  --global-secondary-index-updates \
    '[{"Create":{"IndexName":"ProductoIndex","KeySchema":[{"AttributeName":"Producto","KeyType":"HASH"}],"Projection":{"ProjectionType":"ALL"},"ProvisionedThroughput":{"ReadCapacityUnits":5,"WriteCapacityUnits":5}}}]' \
  --region <REGION>

# Consultar usando el índice
aws dynamodb query \
  --table-name <TABLE> \
  --index-name ProductoIndex \
  --key-condition-expression "Producto = :v" \
  --expression-attribute-values '{":v":{"S":"Café Americano"}}' \
  --region <REGION>
# (4.5) Activar TTL
aws dynamodb update-time-to-live \
  --table-name <TABLE> \
  --time-to-live-specification "Enabled=true, AttributeName=expira" \
  --region <REGION>

# (4.6) Limpieza final: eliminar tabla
aws dynamodb delete-table --table-name <TABLE> --region <REGION>
## Conclusión

El laboratorio permitió aplicar los conceptos fundamentales de **Amazon DynamoDB**, creando tablas, cargando y consultando datos mediante **AWS CLI**, **PartiQL** y **CloudShell**.  

Se reforzaron las nociones de **claves primarias**, **índices secundarios**, **capacidad bajo demanda** y **persistencia distribuida sin servidor**.  

Finalmente, se verificó la correcta eliminación de los recursos y se consolidó la práctica de **administración básica en DynamoDB**.


# CAPTURA DEL LABORATORIO TERMINADO

![Texto alternativo](/imagenes/lab3_1.png "Título opcional")
