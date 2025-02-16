from fastapi import FastAPI
from app.routes import form

app = FastAPI(
    title="Formulario API",
    description="API NeuroCheck AI.",
    version="1.0.0"
)

app.include_router(form.router)

@app.get("/", summary="Endpoint de prueba", description="Devuelve un mensaje de saludo.")
async def root():
    return {"greeting": "Hello world"}
