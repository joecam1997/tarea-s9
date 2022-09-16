class Ejercicios:
    secuencia = 0
    def menu(self, opciones, título):
        print("/"*20, título, "/"*20)
        for i in opciones:
            print(i)
        opc = input("Elija un Numero del 1 al {}: ".format(len(opciones)))
        return opc

        # valor2 = int(input("Ingrese su primer valor: "))
        # valor3 = int(input("Ingrese su segundo valor: "))
        #
        # sum = sumar(valor2,valor3)
        # print("La suma de esos valores son: ",sum)
        # mul = multiplicar(valor2,valor3)
        # print("Y la multiplicación es: ",mul)