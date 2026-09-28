from clases import PathsSingleton
from Manager.Manager import ComandosManager
import os

def main():
# Comando que deseas ejecutar en PowerShell
    diseño = PathsSingleton.SingletonPath().disenio
    while True:

        Argumentos = input(diseño)
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