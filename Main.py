from clases import PathsSingleton
from Manager.Manager import ComandosManager
import os

path = PathsSingleton.SingletonPath()

def main():
# Comando que deseas ejecutar en PowerShell
    limpiar_consola()
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

def limpiar_consola():
  # 'nt' corresponde a Windows
  if os.name == 'nt':
    os.system('cls')
  # 'posix' corresponde a Linux y macOS
  else:
    os.system('clear')


# Para usar la función:
limpiar_consola()
if "__main__":
    main()