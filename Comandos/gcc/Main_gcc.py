from Plantilla import Comando

class Comando_gcc(Comando):

    def __init__(self, StrArgumento: list):
        super().__init__(StrArgumentos=StrArgumento)

        # el Regex sera una propiedad de cada instancia del comando gcc
        self.Regex = r'^gcc\s+([\w.\\/-]+\.c)(?:\s+-o\s+([\w.\\/-]+))?$'
        