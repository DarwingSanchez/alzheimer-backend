from app.models.form_model import FormModel

def process_form(data: FormModel):
    print(data)
    return {"message": "Form received", "data": data.dict()}
