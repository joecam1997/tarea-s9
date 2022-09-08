texto1="hola"
texto2="Mundo"
textoFinal=texto1+ " "+texto2
print(textoFinal)

print("el saludo es:%s %s" %(texto1,texto2))


saludoFinal="saludo:{0} {1}".format(texto1,texto2)
print(saludoFinal)

saludofinal2="saludo:{x} {y}".format(x=texto1,y=texto2)
print(saludofinal2)