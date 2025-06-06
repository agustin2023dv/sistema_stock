import csv
import os
from datetime import datetime

RUTA_ARCHIVO = "data/productos.csv"

def guardar_producto(codigo: str, nombre: str, cantidad: int):
    """Guarda un producto en el archivo CSV"""
    
    archivo_existe = os.path.isfile(RUTA_ARCHIVO)

    with open(RUTA_ARCHIVO, mode="a", newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        
        # Si el archivo es nuevo, escribimos los encabezados
        if not archivo_existe:
            escritor.writerow(["codigo", "nombre", "cantidad", "fecha"])

        escritor.writerow([codigo, nombre, cantidad, datetime.now().isoformat()])
