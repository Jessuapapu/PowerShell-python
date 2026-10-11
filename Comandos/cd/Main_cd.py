import os
from ..Plantilla import Comando
from clases.PathsSingleton import SingletonPath
import re

singlepath = SingletonPath()
class Comando_cd(Comando):
    def __init__(self, StrArgumento: list):
            super().__init__(StrArgumentos=StrArgumento)
            self.regex = r"""^(?:cd)((?P<ruta>(\s(?:"|\')[a-zA-Z]:(\\|/|\\\\)[\w\\/ .-]+(?:"|\')|\s\*))?|(?P<accion>(\s(..|.|~|-)))?|(?P<Carpeta>[\w\\/ .-]+)?)$"""

            try:
                Argumentos = self._validacion_argumentos(StrArgumentos=StrArgumento,regex=self.regex, 
                            MsjException="Error en los argumentos, Ejemplo de uso cd [[-Path] <string>] ")
            except Exception as e:
                print(e + '111')
                return

            self.mover_a_carpeta(Argumentos['ruta'],Argumentos['accion'],Argumentos['dir'])

    def mover_a_carpeta(self, ruta, accion,carpeta):
        if ruta:
            Ruta = ruta[1:].replace('"','').replace("'",'')
            if not os.path.exists(Ruta) or not os.path.isdir(Ruta):
                return False
            singlepath.cambiarRuta(Ruta)
            return True

        if accion:
            accion = accion.strip()
            if '-' == accion:
                singlepath.cambiarRuta(singlepath.pathAnterior)
            if '.' == accion:
                singlepath.cambiarRuta(singlepath.pathActual)
            if '..' == accion:

                RutaActual = singlepath.pathActual.replace('/','\\').replace('\\\\','\\').split("\\")

                if len(RutaActual) > 1:
                    RutaPadre = "\\".join(RutaActual[:len(RutaActual)-1])

                    if not '\\' in RutaPadre:
                        RutaPadre = RutaPadre + "\\"

                    singlepath.cambiarRuta(RutaPadre)
                    return True
                else:
                    print('could not change the directory')
                    return False
            if '~' == accion:
                singlepath.cambiarRuta(singlepath.pathHome)
            return True

        if carpeta:
            carpeta = carpeta[1:]
            if not os.path.exists(singlepath.pathActual+"\\"+carpeta) or not os.path.isdir(singlepath.pathActual+"\\"+carpeta):
                return False

            singlepath.cambiarRuta(singlepath.pathActual+"\\"+carpeta)
            return True

    def EmpaquetarArgumentos(self, ArgumentosMatch: re.Match) -> dict:  
            Argumentos:list[str] = ArgumentosMatch.groupdict()

            return {
                'ruta': Argumentos['ruta'],
                'accion': Argumentos['accion'],
                'dir': Argumentos['Carpeta']
            } 


    