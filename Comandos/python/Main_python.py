import os  # comprobar existencia del .py y obtener el cwd del proceso
import re
import subprocess  # lanzar el interprete de Python como proceso externo
from ..Plantilla import Comando  # clase base compartida por todos los comandos


class Comando_python(Comando):
    r"""
        Uso esperado:
            python <script.py>

        Ejemplo:
            python hello.py
            python C:\proyectos-uni\PowerShell-python\prueba.py
    """

    def __init__(self, StrArgumento: list):
        # Inicializa la plantilla base (Comando)
        super().__init__(StrArgumentos=StrArgumento)

        self.Regex = (
            r'^python\s+'
            r'(?P<ruta>'
            r'[Cc]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]+\.py'
            r'|'
            r'[\w.\\/-]+\.py'
            r')$'
        )

        try:
            # Valida la entrada con el regex (metodo heredado de Plantilla).
            # Si coincide, Argumentos es el dict de EmpaquetarArgumentos;
            # si no, lanza Excepcion con el mensaje de uso.
            Argumentos = self._validacion_argumentos(
                StrArgumentos=StrArgumento,
                regex=self.Regex,
                MsjException="Error, uso: python <script.py>"
            )

            # ruta del script ya empaquetada en el dict
            self.script = Argumentos['ruta']

            # Tras validar, se ejecuta el script de inmediato
            self.ejecucion()

        # Excepcion viene de Plantilla: eleva un Exception con el mensaje
        except Exception as e:
            print(e)

    def EmpaquetarArgumentos(self, ArgumentosMatch: re.Match) -> dict:
        # Convierte el Match en un dict con la ruta del .py
        return {
            'ruta': ArgumentosMatch.group('ruta')
        }

    def ejecucion(self):
        # Verifica que el archivo exista en el directorio actual (o ruta dada)
        if not os.path.isfile(self.script):
            self.Excepcion(f"No se encontro el script: {self.script}")

        # Lista de argumentos para el proceso: interprete + script
        command = ["python", self.script]

        try:
            # Ejecuta el proceso externo y captura stdout/stderr como texto
            # cwd=os.getcwd() -> corre relativo al directorio actual del shell
            result = subprocess.run(
                command,
                cwd=os.getcwd(),
                capture_output=True,
                text=True
            )
        # FileNotFoundError: no hay ejecutable "python" en el PATH del sistema
        except FileNotFoundError:
            self.Excepcion(
                "No se encontro el interprete 'python' en el PATH. "
                "Prueba instalar python."
            )

        # Muestra la salida estandar del script (si produjo alguna)
        if result.stdout:
            print(result.stdout, end="")

        # Muestra la salida de error del script (si produjo alguna)
        if result.stderr:
            print(result.stderr, end="")

        # returncode != 0 indica que el script termino con error
        if result.returncode != 0:
            print(f"[python termino con codigo] {result.returncode}")

    def help(self):
        # Texto de ayuda del comando (uso basico)
        print("Uso: python <script.py>")
        print("Ejecuta un archivo .py usando el interprete de Python")
