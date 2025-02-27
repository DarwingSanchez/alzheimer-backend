import pickle
import pandas as pd
import os
from app.models.form_model import FormModel

COLUMN_MAPPING = {
    "age": "Age",
    "gender": "Gender",
    "education_level": "Education Level",
    "bmi": "BMI",
    "physical_activity": "Physical Activity Level",
    "smoking_status": "Smoking Status",
    "alcohol_consumption": "Alcohol Consumption",
    "diabetes": "Diabetes",
    "hypertension": "Hypertension",
    "cholesterol": "Cholesterol Level",
    "family_history": "Family History of Alzheimers",
    "cognitive_score": "Cognitive Test Score",
    "depression": "Depression Level",
    "sleep_quality": "Sleep Quality",
    "dietary_habits": "Dietary Habits",
    "air_pollution": "Air Pollution Exposure",
    "employment_status": "Employment Status",
    "marital_status": "Marital Status",
    "genetic_risk": "Genetic Risk Factor (APOE-E4)",
    "social_engagement": "Social Engagement Level",
    "income_level": "Income Level",
    "stress_levels": "Stress Levels",
    "living_area": "Urban vs Rural Living"
}

def preprocess_data(data: FormModel) -> pd.DataFrame:  
    try:
        data_dict = data.model_dump(exclude={"name"})
    except AttributeError:
        data_dict = data.dict(exclude={"name"})
    
    data_dict["bmi"] = float(data_dict["bmi"])    
    formatted_data = {COLUMN_MAPPING[key]: [value] for key, value in data_dict.items() if key in COLUMN_MAPPING}
    formatted_data["Country"] = ["USA"]
    
    df = pd.DataFrame(formatted_data)    
    
    print(df.isnull().sum())
    print(df.info())
    return df

def predict_alzheimer(data: FormModel):    
    model_route = os.path.join(os.path.dirname(__file__), '../model_predict/modelo_alzheimer.pkl')
    with open(model_route, 'rb') as archivo:
      modelo = pickle.load(archivo)
    df_patient = preprocess_data(data)
    prediction = modelo.predict(df_patient)
    
    probability = modelo.predict_proba(df_patient)
    print(f'Patient: {data.name} - Prediction: {prediction} - Probability: {probability}')
    return 'Sí' if prediction == 'Yes' else 'No'

