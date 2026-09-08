import os
from clases.archivos import Archivo
import table2ascii
from ..Plantilla import Comando

class Comando_ls(Comando):
    """ 
        ls [[-Path] <string[]>] [-r] [[-Filter] <string>] [-Include <string[]>] [-Directory]]

        Regex = ^ls (("[a-zA-Z]:\\[\w\\]+")|\*|-r|)( -r|)(( -Filter \*(\.[\w]+|[\w]+\*))|)( -Directory|)$

        ls o dir la misma vaina xd
    """

    def __init__(self, StrArgumento: list):
        super().__init__(StrArgumentos=StrArgumento)
        # ls "C:\Users\Jessua\Documents" -r -Filter *Hola* -Directory
        # ls * -r -Filter *.Hol -Directory
        # ls -r -Filter *Hola*
        # ls -Directory
        self.Regex = r'^(ls|dir)((( "[a-zA-Z]:\\[\w\\]+")|\*|-r|)( -r|)(( -Filter \*(\.[\w]+|[\w]+\*))|)( -Directory|)|)$'
        try:
            Argumentos = self._validacion_argumentos(StrArgumentos=StrArgumento,regex=self.Regex, 
            MsjException="Error en los argumentos, Ejemplo de uso ls [[-Path] <string[]>] [-r] [[-Filter] <string>] [-Include <string[]>] [-Directory]]")
            print(Argumentos)
        except Exception as e:
            print(e)
            
 
        
        
        

        
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
    

 