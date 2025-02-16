from pydantic import BaseModel
from typing import Optional

class FormModel(BaseModel):
    country: str
    age: int
    gender: str
    education_level: str
    bmi: float
    physical_activity_level: str
    smoking_status: str
    alcohol_consumption: str
    diabetes: bool
    hypertension: bool
    cholesterol_level: str
    family_history_alzheimer: bool
    cognitive_test_score: float
    depression_level: str
    sleep_quality: str
    dietary_habits: str
    air_pollution_exposure: str
    employment_status: str
    marital_status: str
    genetic_risk_factor: Optional[str] = None
    social_engagement_level: str
    income_level: str
    stress_levels: str
    urban_vs_rural_living: str
