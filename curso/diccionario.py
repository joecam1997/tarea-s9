diccionario={"Ecuador":"Quito","Colombia":"Medellin","Argentina":"Buenos Aires"}
print(diccionario["Argentina"])
print(diccionario)

diccionario["Venezuela"]="Caracas"
print(diccionario)
diccionario["Colombia"]="Cali"
print(diccionario)


del diccionario["Colombia"]
print(diccionario)

dic2={"Campoverde":"Joel",25:True,"Sueldo":500.50}
print(dic2[25])

llaves=("España","Francia","Inglatera")
dicPaises={llaves[0]:"Madrid",llaves[1]:"Paris",llaves[2]:"Londres"}
print(dicPaises)

datosPersonales={"Apellidos":"Campoverde","anios":{1:2019,2:2020,3:2021,4:2022,5:2023}}
print(datosPersonales)
print(datosPersonales["anios"])

print(datosPersonales.get('Apellido',"Joel"))

print(datosPersonales.keys())
valores=tuple(datosPersonales.values())
print(valores)