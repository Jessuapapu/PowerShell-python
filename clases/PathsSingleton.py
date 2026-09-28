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
    
        self.disenio = 'PS ' + self.pathInicial[0]+'\\' + self.pathInicial[1] + '\\' + self.pathInicial[2] + '> '
        self.pathActual = self.pathInicial[0]+ '\\' + self.pathInicial[1] + '\\' + self.pathInicial[2]
        