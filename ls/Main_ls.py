import os
from clases.archivos import Archivo
import table2ascii
def listar_archivos(ruta):
    if not os.path.isdir(ruta) or not os.path.exists(ruta):
        return None

    lista_archivos = os.listdir(ruta)
    lista_archivos_info = []

    for archivo in lista_archivos:
        lista_archivos_info.append(Archivo(nombre=archivo,path=ruta))

    print(table2ascii.table2ascii(
        header=["permisos","Nombre","tamaño",'fecha',"extension"],
        body=[archivo.to_string() for archivo in lista_archivos_info]
    ))

    return lista_archivos_info
    

 