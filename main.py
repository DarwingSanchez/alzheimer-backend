from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import form

app = FastAPI(
    title="Formulario API",
    description="API NeuroCheck AI.",
    version="1.0.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(form.router)

@app.get("/", summary="Endpoint de prueba", description="Devuelve un mensaje de saludo.")
async def root():
    return {"greeting": "Hello world"}

