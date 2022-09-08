"""
file = open('data1.txt', 'r')
# print(file)
lineas = file.readlines()
print(lineas)
file.close()  # Cerrar el documento.
"""

"""
with open('data2.txt', 'r') as archivo:
    lineas = archivo.readlines()
    # print(lineas)

# print(lineas)
for l in lineas:
    print(l.replace('\n', ''))
"""

"""
with open('data2.txt', 'r') as archivo:
    contenido = archivo.read()
    lineas = contenido.split('\n')
    print(lineas)
"""

"""
with open('data2.txt', 'r') as archivo:
    contenido = archivo.read()
    lineas = contenido.split('\n')
    pos = archivo.tell()
    print(pos)
    print('El archivo tiene {0} caracteres de longitud'.format(pos))
"""

"""
with open('data2.txt', 'r') as archivo:
    archivo.seek(7)
    pos = archivo.tell()
    print(pos)
    contenido = archivo.read()
    lineas = contenido.split('\n')
    print(lineas)
"""

"""
with open('data2.txt', 'r') as archivo:
    siguientes7 = archivo.read(7)
    print(siguientes7)
"""

"""
with open('data2.txt', 'r') as archivo:
    print(type(archivo.read()))

with open('data2.txt', 'rb') as archivo:
    print(type(archivo.read()))
"""

with open('data3.txt','a') as archivo:
    archivo.write('oscar\nalejandro\njoel\ngenesis')

    