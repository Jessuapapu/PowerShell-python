
from Manager.Manager import ComandosManager
import os

def main():
# Comando que deseas ejecutar en PowerShell

    pathInicial = os.getcwd().split('\\')

    disenio = 'PS ' + pathInicial[0]+'\\' + pathInicial[1] + '\\' + pathInicial[2] + '> '
    path = pathInicial[0]+'\\' + pathInicial[1] + '\\' + pathInicial[2]
    while True:
        Argumentos = input(disenio)
        ArgumentoComando = Argumentos.split(' ')
        comando = ComandosManager.desde_string(ArgumentoComando[0])
        comando.ejecutar(Argumentos)
        
if "__main__":
    main()