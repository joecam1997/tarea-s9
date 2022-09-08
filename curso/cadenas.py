texto="Bienvenidos"
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.find("ni"))#posicion
print(texto.count("e"))#cantidad

textoFinal=texto.replace("e","3")
print(textoFinal)

valor=texto.isnumeric()#verdadero o falso si es un numero
print(valor)

cadenaseparada=texto.split(" ")
print(cadenaseparada)