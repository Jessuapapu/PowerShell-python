import os  # comprobar si la ruta es carpeta y si el directorio padre existe
from ..Plantilla import Comando  # clase base compartida por todos los comandos

class Comando_touch(Comando):
    """
        Uso esperado:
            touch <archivo>

        Ejemplos:
            touch archivo.txt
            touch Comandos/touch/txt2.txt
    """

    def __init__(self, StrArgumento: list):
        # Inicializa la plantilla base (Comando)
        super().__init__(StrArgumentos=StrArgumento)

        # Regex del comando:
        # ^touch\s+  -> empieza con "touch" + espacios
        # ([\w.\\/-]+) -> captura la ruta/nombre del archivo
        #   [\w.\\/-]+ -> letras, numeros, ., \, /, -
        # $ -> no acepta nada mas despues del archivo
        self.Regex = r'^touch\s+([\w.\\/-]+)$'

        try:
            # Valida la entrada con el regex (metodo heredado de Plantilla).
            # Si coincide, Argumentos son los grupos capturados;
            # si no, lanza Excepcion con el mensaje de uso.
            Argumentos = self._validacion_argumentos(
                StrArgumentos=StrArgumento,
                regex=self.Regex,
                MsjException="Uso: touch <archivo>"
            )

            # tomar el primer grupo de la tupla retornada por _validacion_argumentos que guarda la ruta/nombre del archivo
            self.archivo = Argumentos[0]

            # Tras validar, se crea/actualiza el archivo de inmediato
            self.ejecucion()

        # Cualquier error de validacion o de creacion se imprime aqui
        except Exception as e:
            print(e)

    def ejecucion(self):
        # Si la ruta ya existe y es una carpeta, no se puede "tocar" como archivo
        if os.path.isdir(self.archivo):
            self.Excepcion(f"Es un directorio, no un archivo: {self.archivo}")

        # Saca la carpeta padre de la ruta (ej: "file/note.txt" -> "file")
        # Si el archivo esta en el cwd, dirname devuelve "" (string vacio)
        carpeta = os.path.dirname(self.archivo)

        # Solo valida el directorio padre si la ruta trae carpeta.
        # No crea carpetas nuevas: si no existe, falla.
        if carpeta and not os.path.isdir(carpeta):
            self.Excepcion(f"No existe el directorio: {carpeta}")

        try:
            # Modo "a" (append): crea el archivo si no existe;
            # si ya existe, lo abre sin borrar el contenido.
            # No se escribe nada: solo se abre y se cierra.
            with open(self.archivo, "a", encoding="utf-8"):
                pass
        # OSError: problemas del sistema al crear/abrir (permisos, disco, etc.)
        except OSError as e:
            self.Excepcion(f"No se pudo crear el archivo: {self.archivo} - {e}")

        # Confirma que el archivo quedo creado (o ya existia)
        print(f"Archivo creado: {self.archivo}")

    def help(self):
        # Texto de ayuda del comando (uso basico)
        print("Uso: touch <archivo>")
        print("Crea un archivo nuevo o lo actualiza si ya existe")
