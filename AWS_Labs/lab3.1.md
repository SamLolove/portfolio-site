#  Lab 3.1: Working with Amazon S3

# CAPTURA DEL LABORATORIO TERMINADO

![Texto alternativo](/imagenes/lab2_1.png "Título opcional")


## 1) Objetivo
Crear y operar un bucket de **Amazon S3** en un entorno de laboratorio para:  

- Crear el bucket siguiendo buenas prácticas.  
- Subir, descargar y organizar objetos/carpetas.  
- Activar **versionado** y **encriptación SSE-S3**.  
- Aplicar una **regla de ciclo de vida** básica.  
- Limpiar recursos al final del laboratorio.

> Nota: Algunas acciones pueden estar limitadas en cuentas temporales de laboratorio.

---

## 2) Ambiente
- **Cuenta:** Temporal del laboratorio (credenciales efímeras)  
- **Región de trabajo:** `<REGIÓN>`  
- **Herramientas:** AWS Console, AWS CloudShell, AWS CLI v2  

---

## 3) Actividades realizadas (resumen)
1. Crear bucket con nombre único: `s3-lab31-sd-2025-10-15-s3site`.  
2. Subir y descargar objetos, creando estructura de carpetas (`evidencias/`).  
3. Habilitar versionado para conservar historial de archivos.  
4. Configurar encriptación SSE-S3 por defecto.  
5. Aplicar regla de ciclo de vida simple (expiración de objetos).  
6. Validar contenido, versiones y cifrado de objetos.  
7. Limpieza final del bucket y objetos si era necesario.

---

## 4) Pasos y comandos clave (CloudShell / CLI)
> Sustituye `<REGION>` y `<BUCKET>` por tus valores reales.

```bash
# Ver identidad y configuración
aws sts get-caller-identity
aws configure list

# Crear bucket
aws s3 mb s3://<BUCKET> --region <REGION>

# Subir y listar objetos
echo "Hola S3 - Lab 3.1" > nota.txt
aws s3 cp nota.txt s3://<BUCKET>/evidencias/nota.txt
aws s3 ls s3://<BUCKET>/evidencias/

# Descargar y verificar
aws s3 cp s3://<BUCKET>/evidencias/nota.txt ./nota_descargada.txt
cat nota_descargada.txt

# Habilitar versionado
aws s3api put-bucket-versioning \
  --bucket <BUCKET> \
  --versioning-configuration Status=Enabled

# Verificar versionado
aws s3api get-bucket-versioning --bucket <BUCKET>

# Encriptación SSE-S3
aws s3api put-bucket-encryption \
  --bucket <BUCKET> \
  --server-side-encryption-configuration '{
    "Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]
  }'

# Verificar encriptación
aws s3api get-bucket-encryption --bucket <BUCKET>

# Subir objetos para versionado
echo "v1" > versionado.txt
aws s3 cp versionado.txt s3://<BUCKET>/evidencias/versionado.txt
echo "v2" > versionado.txt
aws s3 cp versionado.txt s3://<BUCKET>/evidencias/versionado.txt

# Listar versiones
aws s3api list-object-versions --bucket <BUCKET> --prefix evidencias/versionado.txt

# Regla de ciclo de vida (expiración 7 días)
cat > lifecycle.json << 'JSON'
{
  "Rules": [
    {
      "ID": "expire-tmp-7d",
      "Filter": { "Prefix": "tmp/" },
      "Status": "Enabled",
      "Expiration": { "Days": 7 }
    }
  ]
}
JSON

aws s3api put-bucket-lifecycle-configuration \
  --bucket <BUCKET> \
  --lifecycle-configuration file://lifecycle.json

# Verificar regla de ciclo de vida
aws s3api get-bucket-lifecycle-configuration --bucket <BUCKET>

# Sincronización opcional
mkdir -p carpeta_local && echo "sync" > carpeta_local/ejemplo.txt
aws s3 sync carpeta_local/ s3://<BUCKET>/sync-demo/

# Limpieza final
# - Vaciar incluyendo versiones
aws s3api list-object-versions --bucket <BUCKET> \
  --query='{Objects: Versions[].{Key:Key,VersionId:VersionId}}' > objects.json
aws s3api list-object-versions --bucket <BUCKET> \
  --query='{Objects: DeleteMarkers[].{Key:Key,VersionId:VersionId}}' > deletes.json
jq -s '{Objects: (.[0].Objects + .[1].Objects)}' objects.json deletes.json > all.json
aws s3api delete-objects --bucket <BUCKET> --delete file://all.json

# Borrar bucket
aws s3 rb s3://<BUCKET> --force

