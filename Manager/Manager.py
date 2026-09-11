from enum import Enum
from Comandos.ls import Main_ls
from Comandos.python import Main_python

class ComandosManager(Enum):
    ls = ('LS', lambda Argumento: Main_ls.Comando_ls(Argumento))
    dirs = ('DIR', lambda Argumento: Main_ls.Comando_ls(Argumento))
    # cd = ('CD')
    python = ("PYTHON", lambda Argumento: Main_python.Comando_python(Argumento))

    def __init__(self, codigo, funcion):
        self.codigo = codigo
        self.ejecutar = funcion

    @classmethod
    def desde_string(cls, string_codigo):
        """Busca el Enum correspondiente al código str proporcionado."""
        string_codigo = string_codigo.upper()
        for operacion in cls:
            if operacion.codigo == string_codigo:
                return operacion
        
        # Lanza un error genérico o personalizado si no existe
        raise ValueError(f"Operación no soportada: {string_codigo}")

