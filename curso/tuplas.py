"""
tupla: es una estructura de datos prpia de python que permite almacenar distintos valores
,son inmutables ,no cambian.
"""
tupla=(1,2,3,4,5,6,7,8,9)
print(tupla)
tupla2=(2,"joel",True,500.1,35+7j)
print(tupla2)

tupla3=(3,6,9,12,(15,18,21))
print(tupla3)
print(tupla2[3])
#tupla2[3]="eduardo"
print(tupla2[-1])
print(tupla2[0:4])
print(tupla[-2])

#a,b,c =tupla
#print(a)
#print(b)
#print(c)

tuplaFinal=tupla+tupla3
print(tuplaFinal)

print(tuplaFinal.count(5))
print(tuplaFinal.index(3))