from app.controllers.openai_controller import get_suggestion
from app.controllers.prediction_controller import predict_alzheimer
from app.models.form_model import FormModel

def process_form(data: FormModel):
    try:
        prediction = predict_alzheimer(data)
        recommendations = get_suggestion(data, prediction)                
        return {
            "message": "Form received",
            "data": {
                "name": data.name,
                "probability": prediction,
                "recommendations": recommendations
            }
        }
    except Exception as e:
        print(f"Error en process_form: {e}")  # Puedes usar logging en producción
        return {
            "message": "An error occurred while processing the form",
            "error": str(e)
        }

