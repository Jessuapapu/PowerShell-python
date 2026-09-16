import os  # nos da funciones para manejar rutas y crear carpetas en el sistema
from ..Plantilla import Comando  # clase base de la que heredamos validacion y Excepcion


class Comando_mkdir(Comando):
    """
    mkdir <directorio>

    ejemplos: (solo permite crear un directorio a la vez)
    mkdir new_folder
    mkdir new_folder/sub_folder
    """

    def __init__(self, StrArgumento: list):
        # llamamos al init de la plantilla para dejar lista la base del comando
        super().__init__(StrArgumentos=StrArgumento)

        # guardamos en self.Regex el patron que acepta este comando:
        # - rutas absolutas de Windows en C: (ej: C:\Users\User\Desktop\new_folder)
        # - o rutas relativas tipo new_folder / new_folder/sub_folder
        # el grupo (...) es lo que despues vamos a sacar como Argumentos[0]
        self.Regex = (
            r'^mkdir\s+'
            r'('
            r'[Cc]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]+'
            r'|'
            r'[\w.\\/-]+'
            r')$'
        )

        try:
            # Argumentos guarda lo que retorna _validacion_argumentos:
            # si el texto del usuario hace match con el regex, nos da una tupla
            # con los grupos capturados; si no, lanza Excepcion con el mensaje de uso
            Argumentos = self._validacion_argumentos(
                StrArgumentos=StrArgumento,
                regex=self.Regex,
                MsjException="Uso: mkdir <directorio>\n"
                "Ejemplos: mkdir new_folder | mkdir C:\\Users\\User\\Desktop\\new_folder"
            )

            # guardamos el valor de Argumentos[0] (la ruta del directorio capturada
            # por el regex) en un atributo propio de la clase, para usarlo despues
            # en ejecucion() sin volver a tocar Argumentos
            self.directorio = Argumentos[0]

            # una vez validado y guardado, mandamos a crear la carpeta
            self.ejecucion()

        # si algo fallo (uso incorrecto, ruta invalida, etc.), solo imprimimos el error
        except Exception as e:
            print(e)

    def ejecucion(self):
        # en ruta se guarda el valor retornado por os.path.normpath:
        # limpia la ruta (ej: "a/b/../c" -> "a\\c") 
        ruta = os.path.normpath(self.directorio)

        # os.path.isabs retorna True si la ruta es absoluta (empieza con unidad, ej: C:\...)
        if os.path.isabs(ruta):
            # os.path.splitdrive separa la unidad del resto de la ruta
            # unidad = "C:", resto = "\Users\User\Desktop\new_folder"
            unidad, resto = os.path.splitdrive(ruta)

            # solo permitimos crear carpetas en la unidad C:
            if unidad.upper() != "C:":
                self.Excepcion(
                    f"Solo se permite crear directorios en la unidad C: (Windows)"
                )

            # si resto es solo "\" o "/" o vacio, estarian intentando crear
            # la raiz de la unidad, y eso no lo dejamos
            if resto in ("\\", "/", ""):
                self.Excepcion(
                    f"La ruta no puede terminar en '\\' o '/' o estar vacia"
                )

        # os.path.exists retorna True si ya hay algo (archivo o carpeta) en esa ruta;
        # si ya existe, no creamos nada y lanzamos error
        if os.path.exists(ruta):
            self.Excepcion(f"Ya existe: {ruta}")

        # en padre se guarda lo que retorna os.path.dirname:
        # la carpeta "de arriba" de la ruta (ej: "new_folder/sub" -> "new_folder")
        # si la ruta no trae padre, dirname retorna "" (string vacio)
        padre = os.path.dirname(ruta)

        # si hay padre y ese padre no existe como carpeta, fallamos:
        # este mkdir solo crea UN nivel, no crea la cadena completa
        if padre and not os.path.isdir(padre):
            self.Excepcion(
                f"No existe el directorio padre: {padre}\n"
                "Crea primero el directorio padre"
            )

        try:
            # os.mkdir crea UNA sola carpeta en la ruta dada
            # (no crea padres intermedios; eso seria os.makedirs)
            os.mkdir(ruta)
        # OsError: problemas del sistema al crear (permisos, disco, etc.)
        except OsError as e:
            self.Excepcion(f"No se pudo crear {ruta} - {e}")

        # confirmamos al usuario que la carpeta quedo creada
        print(f"Directorio creado: {ruta}")

    def help(self):
        # texto de ayuda basico del comando
        print("Uso: mkdir <directorio>")
        print("Crea un nuevo directorio en la ruta especificada")
