from fastapi import FastAPI, Query
from starlette.responses import JSONResponse
from typing import Optional, List
from models import Bridge
from operations import read_all_bridges

app = FastAPI()


@app.get("/")
def home():
    return JSONResponse({"message": "Hello World"})


@app.get("/bridges", response_model=List[Bridge])
async def get_bridges(
        OBJECTID: Optional[int] = Query(None),
        TRONCAL: Optional[str] = Query(None),
        NOMBRE_TRAMO: Optional[str] = Query(None),
        TIPO_OBRA: Optional[str] = Query(None),
        ANCHO: Optional[float] = Query(None),
        LONGITUD: Optional[float] = Query(None),
        PLACA: Optional[str] = Query(None),
        BARANDAS: Optional[str] = Query(None),
        ESTRIBO_DER: Optional[str] = Query(None),
        ESTRIBO_IZQ: Optional[str] = Query(None),
        FUENTE: Optional[str] = Query(None),
        VIGENCIA: Optional[int] = Query(None),
        ID_PUENTE: Optional[int] = Query(None),
):
    # Fetch all bridges from the CSV via operations.py
    bridges = await read_all_bridges()

    # Apply filters only if the respective parameter is provided
    if OBJECTID is not None:
        bridges = [b for b in bridges if b.OBJECTID == OBJECTID]
    if TRONCAL is not None:
        bridges = [b for b in bridges if b.TRONCAL.lower() == TRONCAL.lower()]
    if NOMBRE_TRAMO is not None:
        bridges = [b for b in bridges if b.NOMBRE_TRAMO.lower() == NOMBRE_TRAMO.lower()]
    if TIPO_OBRA is not None:
        bridges = [b for b in bridges if b.TIPO_OBRA.lower() == TIPO_OBRA.lower()]
    if ANCHO is not None:
        bridges = [b for b in bridges if b.ANCHO == ANCHO]
    if LONGITUD is not None:
        bridges = [b for b in bridges if b.LONGITUD == LONGITUD]
    if PLACA is not None:
        bridges = [b for b in bridges if b.PLACA.lower() == PLACA.lower()]
    if BARANDAS is not None:
        bridges = [b for b in bridges if b.BARANDAS.lower() == BARANDAS.lower()]
    if ESTRIBO_DER is not None:
        bridges = [b for b in bridges if b.ESTRIBO_DER.lower() == ESTRIBO_DER.lower()]
    if ESTRIBO_IZQ is not None:
        bridges = [b for b in bridges if b.ESTRIBO_IZQ.lower() == ESTRIBO_IZQ.lower()]
    if FUENTE is not None:
        bridges = [b for b in bridges if b.FUENTE.lower() == FUENTE.lower()]
    if VIGENCIA is not None:
        bridges = [b for b in bridges if b.VIGENCIA == VIGENCIA]
    if ID_PUENTE is not None:
        bridges = [b for b in bridges if b.ID_PUENTE == ID_PUENTE]

    return bridges

