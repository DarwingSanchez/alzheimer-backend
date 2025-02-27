from fastapi import APIRouter, Depends
from app.middleware.auth import verify_token
from app.controllers.form_controller import process_form
from app.models.form_model import FormModel

router = APIRouter(prefix="/api/diagnostic", tags=["Formulario"])

@router.post(
    "/",
    dependencies=[Depends(verify_token)],
    summary="Enviar formulario",
    description="Recibe un formulario con información personal y lo procesa."
)
async def submit_form(form_data: FormModel):
    print(form_data)
    return process_form(form_data)
