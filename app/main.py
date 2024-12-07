from fastapi import FastAPI
from app.routers import gestion_datos

app = FastAPI(title="Mejor CDT API")

app.include_router(gestion_datos.router, prefix="/gestion-datos", tags=["Gestión de Datos"])
