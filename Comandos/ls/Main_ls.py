import os
from clases.archivos import Archivo
from clases.PathsSingleton import SingletonPath
import table2ascii
from ..Plantilla import Comando
import re 

singlepath = SingletonPath()
class Comando_ls(Comando):
    r""" 
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
        self.Regex = r"""^(?:ls|dir)(?P<ruta>(\s(?:"|\')[a-zA-Z]:(\\|/|\\\\)[\w\\/ .-]+(?:"|\')|\s\*))?(?:(?P<r>\s-r)?|(?P<Filter>\s-Filter\s\*(\.[\w]+|[\w]+\*))?|(?P<Dir>\s-Directory)?)*$"""
        
        self.RegexRuta = r'("|\')[a-zA-Z]:(\\|/|\\\\)[\w(\\|/|\\\\)]+(| [\w\.\d]+| )("|\')'
        try:
            Argumentos = self._validacion_argumentos(StrArgumentos=StrArgumento,regex=self.Regex, 
            MsjException="Error en los argumentos, Ejemplo de uso ls [[-Path] <string[]>] [-r] [[-Filter] <string>] [-Include <string[]>] [-Directory]]")
        except Exception as e:
            print(e)
            return

        self.listar_archivos(ruta=Argumentos['path'],recursivo=Argumentos['recursivo'],SoloCarpeta=Argumentos['SoloDir'], filtro=Argumentos['filtro'])
         
        
    def listar_archivos(self, ruta: str | None, recursivo: bool, filtro: str | None, SoloCarpeta: bool):
        if not os.path.isdir(ruta) or not os.path.exists(ruta):
            return None

        lista_archivos = os.listdir(ruta)

        if recursivo:
            lista_archivos.reverse()

        lista_archivos_info = []

        for archivo in lista_archivos:
            tmpArchivo = Archivo(nombre=archivo,path=ruta)

            if SoloCarpeta and tmpArchivo.extension != 'CARPETA':
                continue

            if filtro and not re.match(f"^{filtro.replace('.', r'\.').replace('*', '.*')}$", archivo, re.IGNORECASE):
                continue

            lista_archivos_info.append(tmpArchivo)

        print(table2ascii.table2ascii(
            header=["permisos","Nombre","tamaño",'fecha',"extension"],
            body=[archivo.to_string() for archivo in lista_archivos_info]
        ))

        return lista_archivos_info
    
    def EmpaquetarArgumentos(self, Argumentos: tuple) -> dict:
        path = singlepath.pathActual
        
        if re.match(r'("|\')[a-zA-Z]:(\\|/|\\\\)[\w(\\|/|\\\\)]+("|\')', Argumentos[2].strip()):
            path = Argumentos[2].strip().replace('"','')
        
        recursivo = True if ' -r' in Argumentos else False
        SoloDirectorios = True if ' -Directory' in Argumentos else False 
        filtro = None 

        for Argumento in Argumentos[2:]:

            if type(Argumento) == str and ' -FILTER' in Argumento.upper():
                filtro = Argumento.split()[1]

        return {
            'path': path,
            'recursivo': recursivo,
            'SoloDir': SoloDirectorios,
            'filtro': filtro
        } 
 