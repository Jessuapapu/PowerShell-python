import subprocess
from Comandos.ls.Main_ls import *
import os

def main():
# Comando que deseas ejecutar en PowerShell

    pathInicial = os.getcwd().split('\\')

    disenio = 'PS ' + pathInicial[0]+'\\' + pathInicial[1] + '\\' + pathInicial[2] + '> '
    path = pathInicial[0]+'\\' + pathInicial[1] + '\\' + pathInicial[2]
    while True:
        comando = input(disenio)
        

if "__main__":
    main()