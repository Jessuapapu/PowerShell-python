import os # obtener el cwd
import subprocess # para lanzar python como proceso externo
from ..Plantilla import Comando

class Comando_python(Comando):
    """
        python <script.py> [args...]

        python hello.py
    """

    def __init__(self, StrArgumento: list):
        super().__init__(StrArgumentos=StrArgumento)

        # el Regex sera una propiedad de cada instancia del comando gcc
        self.Regex = r'^python\s+([\w.\\/-]+\.py)$'

        try:
            Argumentos = self._validacion_argumentos(
                StrArgumentos=StrArgumento,
                regex=self.Regex,
                MsjException="Error, uso python <script.py> [argumentos...]"
            )

            self.script = Argumentos[0]
            self.ejecucion()

        except self.Excepcion as e:
            print(e)

    def ejecucion(self):

        # verificar si el script existe
        if not os.path.isfile(self.script):
            self.Excepcion(f"No se encontro el script: {self.script}")

        # comando para ejecutar el script con python
        command = ["python", self.script]

        # ejecutar el script usando el subproceso
        try:
            result = subprocess.run(
                command,
                cwd=os.getcwd(),
                capture_output=True,
                text=True
            )
        # si el interprete no esta en el PATH, lanzar una excepcion
        except FileNotFoundError:
            self.Excepcion(
                "No se encontro el interprete 'python en el PATH."
                "Prueba instalar python."
            )

        # si el script termina con codigo de error, imprimir el codigo de error
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="")

        if result.returncode != 0:
            print(f"[python termino con codigo] {result.returncode}")

    def help(self):
        print("Uso: python <script.py> [argumentos...]")
        print("Ejecuta un archivo .py usando el interprete de Python")