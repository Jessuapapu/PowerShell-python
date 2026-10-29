import platform
import psutil
import subprocess
import re
from ..Plantilla import Comando

ASCII_WINDOWS = [
    "  ########  ########  ",
    "  ########  ########  ",
    "  ########  ########  ",
    "  ########  ########  ",
    "                      ",
    "  ########  ########  ",
    "  ########  ########  ",
    "  ########  ########  ",
    "  ########  ########  "
]

ASCII_LINUX = [
    "      .--.      ",
    "     |o_o |     ",
    "     |:_/ |     ",
    "    //   \\ \\    ",
    "   (|     | )   ",
    "  /'\\_   _/`\\  ",
    "  \\___)=(___/  "
]

class Comando_neofetch(Comando):
    r""" 
        neofetch

        Regex = ^neofetch$

        Imprime información básica del sistema junto a un logo ASCII del OS.
    """

    def __init__(self, StrArgumento: list):
        super().__init__(StrArgumentos=StrArgumento)
        self.Regex = r"^(?P<comando>neofetch)$"
        
        try:
            Argumentos = self._validacion_argumentos(
                StrArgumentos=StrArgumento,
                regex=self.Regex, 
                MsjException="Error en los argumentos, Ejemplo de uso: neofetch"
            )
        except Exception as e:
            print(e)
            return
        
        self.mostrar_estilo_neofetch()

    def obtener_cpu(self, sistema: str) -> str:
        try:
            if sistema == "Windows":
                # Leer el nombre exacto del procesador desde el registro de Windows
                import winreg
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
                cpu_name, _ = winreg.QueryValueEx(key, "ProcessorNameString")
                return cpu_name.strip()
            elif sistema == "Linux":
                output = subprocess.check_output("lscpu | grep 'Model name'", shell=True, text=True)
                return output.split(":")[1].strip()
        except:
            pass
        return platform.processor()
         
    def obtener_gpu(self, sistema: str) -> str:
        try:
            if sistema == "Windows":
                cmd = ["powershell", "-NoProfile", "-Command", "(Get-CimInstance Win32_VideoController).Name"]
                output = subprocess.check_output(cmd, text=True).strip()
                lineas = [l.strip() for l in output.split('\n') if l.strip()]
                return " / ".join(lineas) if lineas else "Desconocida"
            elif sistema == "Linux":
                output = subprocess.check_output("lspci | grep -iE 'vga|3d|display'", shell=True, text=True)
                return output.split(": ")[-1].strip() or "Desconocida"
        except Exception:
            return "No detectada"
        return "Desconocida"

    def mostrar_estilo_neofetch(self):
        sistema = platform.system()
        
        logo = ASCII_WINDOWS if sistema == "Windows" else ASCII_LINUX if sistema == "Linux" else ["   ???   "]
        ancho_logo = len(logo[0])

        try:
            usuario = subprocess.check_output("whoami", shell=True, text=True).strip().split('\\')[-1]
        except Exception:
            usuario = "Usuario"
        
        info = [
            f"{usuario}@{platform.node()}",
            "-" * 25,
            f"OS:  {sistema} {platform.release()} {platform.architecture()[0]}",
            f"CPU: {self.obtener_cpu(sistema)}",
            f"RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB",
            f"GPU: {self.obtener_gpu(sistema)}"
        ]

        print("\n")
        max_lineas = max(len(logo), len(info))
        
        for i in range(max_lineas):
            linea_logo = logo[i] if i < len(logo) else " " * ancho_logo
            linea_info = info[i] if i < len(info) else ""
            print(f"{linea_logo}    {linea_info}")
        print("\n")

    def EmpaquetarArgumentos(self, ArgumentosMatch: re.Match) -> dict:
        return {}

    def mostrar_estilo_neofetch(self):
        sistema = platform.system()
        
        logo = ASCII_WINDOWS if sistema == "Windows" else ASCII_LINUX if sistema == "Linux" else ["   ???   "]
        ancho_logo = len(logo[0])

        try:
            usuario = subprocess.check_output("whoami", shell=True, text=True).strip().split('\\')[-1]
        except Exception:
            usuario = "Usuario"
        
        info = [
            f"{usuario}@{platform.node()}",
            "-" * 25,
            f"OS:  {sistema} {platform.release()} {platform.architecture()[0]}",
            f"CPU: {self.obtener_cpu(sistema)}",
            f"RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB",
            f"GPU: {self.obtener_gpu(sistema)}"
        ]

        print("\n")
        max_lineas = max(len(logo), len(info))
        
        for i in range(max_lineas):
            linea_logo = logo[i] if i < len(logo) else " " * ancho_logo
            linea_info = info[i] if i < len(info) else ""
            print(f"{linea_logo}    {linea_info}")
        print("\n")

    def EmpaquetarArgumentos(self, ArgumentosMatch: re.Match) -> dict:
        return {}