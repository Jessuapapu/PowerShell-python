import re

class Comando():
    def __init__(self, StrArgumentos: str):
        pass

    def __validacion_argumentos(self, StrArgumentos: str, regex: str, MsjException: str):
        if re.Match(regex,StrArgumentos):
            return
        
        return self.Excepcion(MsjException)
        
    def ejecucion(self):
        pass

    def help(self):
        pass 

    def Excepcion(self,msj):
        raise Exception(msj)
