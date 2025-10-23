# 🧾 Lab 6.1: Developing REST APIs with API Gateway

# CAPTURA DEL LABORATORIO TERMINADO

![Texto alternativo](/imagenes/lab6_1.jpg "Título opcional")

## 1) Objetivo
Desarrollar una **API REST** con **Amazon API Gateway** integrada a **AWS Lambda** para exponer un endpoint tipo **GET** (y opcionalmente **POST**), habilitar **CORS**, desplegar en un **stage** y validar su funcionamiento desde **curl** o el **Invoke URL**.  
El laboratorio se realiza con una **cuenta temporal** del entorno **AWS Academy (Canvas + Vocareum)**.

---

## 2) Ambiente
- **Alumno:** JESUS JHAIR CHAN INFANTE  
- **Curso/Sección:** Cómputo de Alto Desempeño  
- **Fecha de realización:** 05/10/2025 – 22:18  
- **Plataforma:** AWS Academy (Canvas + Vocareum)  
- **Evidencia en Canvas:** _Submission Details_ (calificación y marca de tiempo)  

**Arquitectura y servicios utilizados:**
- **Servicios:** Amazon API Gateway (REST), AWS Lambda (Python), CloudWatch (Logs).  
- **Región de trabajo:** `<REGION>`  
- **Cuenta:** Temporal del laboratorio (recursos efímeros).  
- **Patrón de integración:** API Gateway → Lambda (AWS_PROXY).

---

## 3) Actividades realizadas (resumen)
1. Crear una función Lambda con un handler Python para devolver un mensaje simple (“Hello from Lambda”).  
2. Crear una API REST en **API Gateway** con un recurso `/hello` y método **GET**.  
3. Integrar el método GET con la función Lambda usando **AWS_PROXY integration**.  
4. Habilitar **CORS** para permitir llamadas desde navegadores.  
5. Desplegar la API en un stage llamado `prod`.  
6. Probar el endpoint desde el navegador o con **curl**.  
7. Verificar logs de ejecución en **CloudWatch**.  
8. Realizar limpieza de los recursos creados.

---

## 4) Pasos y comandos clave (CloudShell / CLI)
> Sustituye `<REGION>`, `<ACCOUNT_ID>`, `<LAMBDA_NAME>`, `<API_NAME>` por tus valores reales.

### 4.1 Comprobar identidad y región
```bash
aws sts get-caller-identity
aws configure list
cat > lambda_function.py << 'PY'
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda via API Gateway!'
    }
PY

## 4.2 Crear función Lambda

zip function.zip lambda_function.py

aws lambda create-function \
  --function-name <LAMBDA_NAME> \
  --runtime python3.12 \
  --role arn:aws:iam::<ACCOUNT_ID>:role/LabRole \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip \
  --region <REGION>
aws apigateway create-rest-api \
  --name <API_NAME> \
  --region <REGION>

aws apigateway get-resources \
  --rest-api-id <API_ID> \
  --region <REGION>
aws apigateway create-resource \
  --rest-api-id <API_ID> \
  --parent-id <ROOT_ID> \
  --path-part hello \
  --region <REGION>

##4.3 Crear API REST y recurso

aws apigateway put-method \
  --rest-api-id <API_ID> \
  --resource-id <HELLO_ID> \
  --http-method GET \
  --authorization-type "NONE" \
  --region <REGION>
aws apigateway put-integration \
  --rest-api-id <API_ID> \
  --resource-id <HELLO_ID> \
  --http-method GET \
  --type AWS_PROXY \
  --integration-http-method POST \
  --uri arn:aws:apigateway:<REGION>:lambda:path/2015-03-31/functions/arn:aws:lambda:<REGION>:<ACCOUNT_ID>:function:<LAMBDA_NAME>/invocations \
  --region <REGION>

##4.4 Crear recurso /hello y método GET
aws lambda add-permission \
  --function-name <LAMBDA_NAME> \
  --statement-id apigateway-access \
  --action lambda:InvokeFunction \
  --principal apigateway.amazonaws.com \
  --source-arn arn:aws:execute-api:<REGION>:<ACCOUNT_ID>:<API_ID>/*/GET/hello \
  --region <REGION>
aws apigateway put-method-response \
  --rest-api-id <API_ID> \
  --resource-id <HELLO_ID> \
  --http-method GET \
  --status-code 200 \
  --response-models '{"application/json": "Empty"}' \
  --region <REGION>

  ##4.5 Integrar el método con Lambda
aws apigateway create-deployment \
  --rest-api-id <API_ID> \
  --stage-name prod \
  --region <REGION>

curl https://<API_ID>.execute-api.<REGION>.amazonaws.com/prod/hello

Hello from Lambda via API Gateway!

bash ~

## 5) Resultados y verificación

- El endpoint `/hello` respondió correctamente al método **GET**.  
- **CloudWatch** registró la ejecución y respuesta **HTTP 200**.  
- **CORS** habilitado para peticiones externas.  
- API desplegada exitosamente en el stage **prod**.  

---

## 2) Conclusión:

El laboratorio permitió comprender la arquitectura y flujo de **API Gateway + AWS Lambda**, donde se implementó una **API REST funcional** utilizando el modelo **AWS_PROXY**.  

Se reforzaron conceptos de **integración sin servidor**, **CORS**, **despliegues por stages** y el uso del **Invoke URL** para pruebas HTTP.  

Finalmente, se verificó la ejecución exitosa del endpoint y el registro de eventos en **CloudWatch**, demostrando el funcionamiento correcto de la **API REST**.
