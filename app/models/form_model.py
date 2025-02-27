from pydantic import BaseModel, Field

class FormModel(BaseModel):    
    name: str
    age: int
    gender: str
    education_level: int = Field(alias="educationLevel")
    bmi: int
    physical_activity: str = Field(alias="physicalActivity")
    smoking_status: str = Field(alias="smokingStatus")
    alcohol_consumption: str = Field(alias="alcoholConsumption")
    cholesterol: str
    family_history: str = Field(alias="familyHistory")
    diabetes: str
    depression: str
    hypertension: str
    sleep_quality: str = Field(alias="sleepQuality")
    dietary_habits: str = Field(alias="dietaryHabits")
    air_pollution: str = Field(alias="airPollution")
    cognitive_score: int = Field(alias="cognitiveScore")
    employment_status: str = Field(alias="employmentStatus")
    marital_status: str = Field(alias="maritalStatus")
    genetic_risk: str = Field(alias="geneticRisk")
    social_engagement: str = Field(alias="socialEngagement")
    income_level: str = Field(alias="incomeLevel")
    stress_levels: str = Field(alias="stressLevels")
    living_area: str = Field(alias="livingArea")

    class Config:
        populate_by_name = True
