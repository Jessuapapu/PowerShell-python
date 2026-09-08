import re

class Comando():
    def __init__(self, StrArgumentos: str):
        pass

    def _validacion_argumentos(self, StrArgumentos: str, regex: str, MsjException: str):
        Argumentos = re.match(regex,StrArgumentos)

        if Argumentos:
            return Argumentos.groups()
        
        return self.Excepcion(MsjException)
        
    def ejecucion(self):
        pass

    def help(self):
        pass 

    def Excepcion(self,msj):
        raise Exception(msj)
