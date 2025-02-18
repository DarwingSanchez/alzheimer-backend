from app.controllers.openai_controller import get_suggestion
from app.models.form_model import FormModel

def process_form(data: FormModel):
    print(data)
    try:
        
        recommendations = get_suggestion(data, "baja")
                
        return {
            "message": "Form received",
            "data": {
                "probability": "baja",
                "recommendations": recommendations
            }
        }
    except Exception as e:
        print(f"Error en process_form: {e}")  # Puedes usar logging en producción
        return {
            "message": "An error occurred while processing the form",
            "error": str(e)
        }

