import os
from clases.archivos import Archivo
import table2ascii
from ..Plantilla import Comando

class Comando_ls(Comando):

    def __init__(self, StrArgumento: list):
        super().__init__(StrArgumentos=StrArgumento)
        """ ls [[-Path] <string[]>] [-r] [[-Filter] <string>] [-Include <string[]>] [-Directory]]"""
        try:
            self.__validacion_argumentos(StrArgumentos=StrArgumento,regex=r'^ls (("[a-zA-Z]:\\[\w\\]+")|\*|-r|)( -r|)(( -Filter \*(\.[\w]+|[\w]+\*))|)( -Directory|)$', 
            MsjException="Error en los argumentos, Ejemplode uso ls [[-Path] <string[]>] [-r] [[-Filter] <string>] [-Include <string[]>] [-Directory]]")
        except Exception as e:
            print(e)
            return -1

        
        
        

        
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
    

 