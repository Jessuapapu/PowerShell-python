import re
from Comandos.touch import Main_touch

regex = Main_touch.Comando_touch.__init__.__doc__  # just to force import path

# Instantiate by calling validation pieces directly
pattern = (
    r'^touch\s+'
    r'('
    r'[Cc]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]+'
    r'|'
    r'[\w.\\/-]+'
    r')$'
)

tests = [
    'touch archivo.txt',
    'touch Comandos/touch/txt2.txt',
    'touch C:\\Users\\fitor\\Desktop\\archivo.txt',
    'touch C:\\Users\\usuario\\Desktop\\archivo.txt',
    'touch C:/Users/usuario/Desktop/archivo.txt',
    'touch C:\\proyectos-uni\\PowerShell-python\\nuevo.txt',
]

print('--- regex matches ---')
for t in tests:
    m = re.match(pattern, t)
    print(repr(t), '->', m.groups() if m else None)

print('--- live command ---')
for t in tests:
    print('INPUT:', t)
    Main_touch.Comando_touch(t)
    print('---')
