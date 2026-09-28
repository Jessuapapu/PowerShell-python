import os
class SingletonPath:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Create the instance only if it doesn't exist
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.pathInicial = os.getcwd().split('\\')
        
        self.disenio = 'PS ' + "\\".join(self.pathInicial[:3]) + '> '
        self.pathActual = self.pathInicial[0]+ '\\' + self.pathInicial[1] + '\\' + self.pathInicial[2]
        self.pathAnterior = None 
        self.pathHome = "\\".join(self.pathInicial[:3])

    def cambiarRuta(self,Ruta: str):
        self.pathAnterior = self.pathActual   
        self.pathActual = Ruta

        self.disenio = 'PS ' + self.pathActual.replace('\\\\','\\').replace("/","\\") + '> '