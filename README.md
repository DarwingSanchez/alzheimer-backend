# FastAPI Form Submission API

## Descripción
Este proyecto es un backend en FastAPI que expone un endpoint protegido por un token de autorización. El endpoint recibe un formulario con información personal y lo procesa.

## Requisitos
- Python 3.11.7
- FastAPI
- Uvicorn
- Pydantic

## Instalación
### 1. Clonar el repositorio
```sh
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

### 2. Crear y activar el entorno virtual
```sh
python3.11 -m venv env
source env/bin/activate  # En Linux/Mac
env\Scripts\activate  # En Windows
```

### 3. Instalar dependencias
```sh
pip install -r requirements.txt
```

## Configuración del entorno
Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:
```
SECRET_KEY="tu_clave_secreta"
```

## Ejecución del servidor
```sh
uvicorn main:app --reload
```

## Endpoints
### 1. `GET /`
- **Descripción:** Endpoint de prueba que devuelve un saludo.
- **Ejemplo de respuesta:**
```json
{
    "greeting": "Hello world"
}
```

### 2. `POST /form/`
- **Descripción:** Recibe un formulario con información personal y lo procesa.
- **Autenticación:** Requiere un token Bearer en el header `Authorization`.
- **Body esperado:**
```json
{
    "name": "Darwing",
    "age": 30,
    "gender": "Male",
    "education_level": "University",
    "bmi": 24.5,
    "physical_activity": "High",
    "smoking_status": "Non-smoker",
    "alcohol_consumption": "Low",
    "diabetes": false,
    "hypertension": false,
    "cholesterol_level": "Normal",
    "family_history_alzheimer": false,
    "cognitive_test_score": 90.5,
    "depression_level": "Low",
    "sleep_quality": "Good",
    "dietary_habits": "Healthy",
    "air_pollution_exposure": "Low",
    "employment_status": "Employed",
    "marital_status": "Single",
    "genetic_risk_factor": null,
    "social_engagement_level": "High",
    "income_level": "Medium",
    "stress_levels": "Low",
    "urban_vs_rural_living": "Urban"
}
```
- **Ejemplo de solicitud con `curl`**
```sh
curl -X POST "http://127.0.0.1:8000/form/" \
-H "Authorization: Bearer tu_token_aqui" \
-H "Content-Type: application/json" \
-d '{"country": "Colombia", "age": 30, "gender": "Male", "education_level": "University", "bmi": 24.5}'
```

## Documentación automática con Swagger
FastAPI genera documentación automática accesible en:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Autenticación
El sistema usa un token de autorización para proteger el endpoint `/form/`. El token debe enviarse en el header `Authorization`:
```sh
Authorization: Bearer tu_token_aqui
```

## Notas adicionales
- Asegúrate de que el entorno virtual esté activado antes de ejecutar los comandos.
- Si necesitas agregar más dependencias, instálalas con `pip install <paquete>` y actualiza `requirements.txt` con `pip freeze > requirements.txt`.

## Licencia
Este proyecto está bajo la licencia MIT.

