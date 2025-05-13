import csv
from typing import Optional, List
from models import *
DATABASE= "bridges.csv"
column_fields=["X","Y","OBJECTID","TRONCAL","NUM_TRONCA","CODIGO_TRAMO","NOMBRE_TRAMO","TIPO_OBRA","ANCHO",
               "LONGITUD", "PLACA", "BARANDAS","ESTRIBO_DER","ESTRIBO_IZQ","FUENTE","VIGENCIA","ID_PUENTE"]
async def read_all_bridges() -> List[Bridge]:
    with open(DATABASE) as csvfile:
        reader = csv.DictReader(csvfile)
        return [Bridge(**row) for row in reader]
def read_one_bridge(id):
    with open(DATABASE) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row["OBJECTID"]) == id:
                return Bridge(**row)
