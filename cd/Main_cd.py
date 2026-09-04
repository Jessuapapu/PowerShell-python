import os

def mover_a_carpeta(ruta, carpeta: str | None):
    if not os.path.exists(ruta) or not os.path.isdir(ruta):
        return False

    if not os.path.exists(ruta+carpeta) or not os.path.isdir(ruta+carpeta):
        return False

    