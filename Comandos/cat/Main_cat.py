import os  # comprobar existencia y si la ruta es un archivo
from ..Plantilla import Comando  # clase base compartida por todos los comandos


class Comando_cat(Comando):
    """
        Uso esperado:
            cat <archivo> [archivo...]

        Ejemplos:
            cat archivo.txt
            cat archivo.txt archivo2.txt
            cat Comandos/cat/archivo2.txt
            cat Comandos/cat/archivo2.txt archivo.txt
    """

    def __init__(self, StrArgumento: list):
        # Inicializa la plantilla base (Comando)
        super().__init__(StrArgumentos=StrArgumento)

        # Regex del comando:
        # ^cat\s+  -> empieza con "cat" + espacios
        # ([\w.\\/-]+(?:\s+[\w.\\/-]+)*) -> captura uno o mas archivos/rutas
        #   [\w.\\/-]+ -> nombre o ruta (letras, numeros, ., \, /, -)
        #   (?:\s+[\w.\\/-]+)* -> opcionalmente mas archivos separados por espacio
        # $ -> no acepta nada mas despues de los archivos
        self.Regex = r'^cat\s+([\w.\\/-]+(?:\s+[\w.\\/-]+)*)$'

        try:
            # Valida la entrada con el regex (metodo heredado de Plantilla).
            # Si coincide, Argumentos son los grupos capturados;
            # si no, lanza Excepcion con el mensaje de uso.
            Argumentos = self._validacion_argumentos(
                StrArgumentos=StrArgumento,
                regex=self.Regex,
                MsjException="Uso: cat <archivo> [archivo...]"
            )

            # Primer grupo del match: todos los archivos juntos en un solo string.
            # split() los separa en una lista para recorrerlos uno por uno.
            self.archivos = Argumentos[0].split()

            # Tras validar, se muestra el contenido de inmediato
            self.ejecucion()

        # Cualquier error de validacion o de lectura se imprime aqui
        except Exception as e:
            print(e)

    def ejecucion(self):
        # Recorre cada ruta pedida por el usuario
        for ruta in self.archivos:
            # Verifica que la ruta exista (archivo o carpeta)
            if not os.path.exists(ruta):
                self.Excepcion(f"No existe: {ruta}")

            # Verifica que sea un archivo (no una carpeta)
            if not os.path.isfile(ruta):
                self.Excepcion(f"No es un archivo: {ruta}")

            try:
                # Abre el archivo en modo lectura como texto UTF-8
                # y guarda todo el contenido en memoria
                with open(ruta, 'r', encoding='utf-8') as f:
                    contenido = f.read()
            # UnicodeDecodeError: el archivo no es texto UTF-8 (binario, otra codificacion, etc.)
            except UnicodeDecodeError:
                self.Excepcion(f"No se puedo leer (no es texto UTF-8) {ruta}")
            # OSError: problemas del sistema al abrir/leer (permisos, disco, etc.)
            except OSError as e:
                self.Excepcion(f"Error al leer el archivo: {ruta} - {e}")

            # Imprime el contenido. Si ya termina en salto de linea, no agrega otro;
            # si no, le pone un \n al final para que el prompt no quede pegado.
            print(contenido, end="" if contenido.endswith("\n") else "\n")

    def help(self):
        # Texto de ayuda del comando (uso basico)
        print("Uso: cat <archivo> [archivo...]")
        print("Muestra el contenido de uno o mas archivos de texto")
