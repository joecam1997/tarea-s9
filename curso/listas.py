lista1=["joel",25,568.56,True,False,23,45]
print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])


print(lista1[0:3])
print(lista1[:2])
print(lista1[3:])

lista1.append ("joel")
print(lista1)

lista1.insert(4,"Ecuador")
print(lista1)

lista1.extend(["Eduardo",1111000,False])
print(lista1)

print(lista1.index("Ecuador"))

lista1.remove(False)
print(lista1)

lista1.pop()
print(lista1)

lista2=["Genesis","Sara","Nathaniel"]
lista3=lista1+lista2
print(lista3)

print(lista2*4)
print("Ecuador" in lista1)