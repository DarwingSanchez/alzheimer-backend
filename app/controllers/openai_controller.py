import os
from dotenv import load_dotenv
from openai import OpenAI

from app.models.form_model import FormModel

load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_KEY"),
)

def get_suggestion(data: FormModel, probability: str):
    prompt = f"""
    A continuación, se presentan datos de un usuario y una probabilidad calculada de desarrollar Alzheimer. 
    En base a estos datos, genera recomendaciones para reducir el riesgo, enfocándote en cambios en estilo de vida:

    Datos del usuario:
    - País: {data.country}
    - Edad: {data.age}
    - Género: {data.gender}
    - Nivel educativo: {data.education_level}
    - IMC: {data.bmi}
    - Nivel de actividad física: {data.physical_activity_level}
    - Fumador: {data.smoking_status}
    - Consumo de alcohol: {data.alcohol_consumption}
    - Diabetes: {data.diabetes}
    - Hipertensión: {data.hypertension}
    - Nivel de colesterol: {data.cholesterol_level}
    - Antecedentes familiares de Alzheimer: {data.family_history_alzheimer}
    - Puntuación en test cognitivo: {data.cognitive_test_score}
    - Nivel de depresión: {data.depression_level}
    - Calidad del sueño: {data.sleep_quality}
    - Hábitos alimenticios: {data.dietary_habits}
    - Exposición a contaminación del aire: {data.air_pollution_exposure}
    - Estado laboral: {data.employment_status}
    - Estado civil: {data.marital_status}
    - Factor de riesgo genético: {data.genetic_risk_factor}
    - Nivel de compromiso social: {data.social_engagement_level}
    - Nivel de ingresos: {data.income_level}
    - Niveles de estrés: {data.stress_levels}
    - Zona de residencia: {data.urban_vs_rural_living}

    Probabilidad de desarrollar Alzheimer: {probability}

    Basado en estos datos, proporciona recomendaciones específicas para reducir el riesgo de Alzheimer.
    Se bastante concreto en las recomendaciones para no generar respuestas muy largas, be concise, don't be verbose. 
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )    

    return response.choices[0].message.content