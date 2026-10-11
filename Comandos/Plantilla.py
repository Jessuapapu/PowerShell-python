import re

class Comando():
    def __init__(self, StrArgumentos: str):
        pass

    def _validacion_argumentos(self, StrArgumentos: str, regex: str, MsjException: str):
        Argumentos = re.match(regex,StrArgumentos)
        
        if Argumentos:
            return self.EmpaquetarArgumentos(Argumentos) 
        
        return self.Excepcion(MsjException)
        
    def ejecucion(self):
        pass

    def help(self):
        pass 

    def Excepcion(self,msj):
        raise Exception(msj)

    def EmpaquetarArgumentos(self, ArgumentosMatch: re.Match) -> dict:
        pass
