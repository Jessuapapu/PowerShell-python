import os
import datetime
import stat

class Archivo:
    def __init__(self, nombre, path):
        self.nombre = nombre
        self.path = path + nombre
        info = os.stat(self.path)
        self.size = '-' if info.st_size == 0 else info.st_size
        self.fecha = datetime.datetime.fromtimestamp(info.st_birthtime)
        self.permisos = stat.filemode(info.st_mode)
        self.__ ,self.extension = os.path.splitext(nombre)

    def to_string(self):
        return [self.permisos,self.nombre, self.size, self.fecha, self.extension if self.extension != '' else 'CARPETA']


