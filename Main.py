from clases import PathsSingleton
from Manager.Manager import ComandosManager
import os

path = PathsSingleton.SingletonPath()

def main():
# Comando que deseas ejecutar en PowerShell
    while True:

        Argumentos = input(path.disenio)
        try:
            if Argumentos.upper() in ('EXIT','SALIR'):
                return
            
            ArgumentoComando = Argumentos.split(' ')
            comando = ComandosManager.desde_string(ArgumentoComando[0])

            comando.ejecutar(Argumentos)
        except Exception as e:
            print(e)

if "__main__":
    main()