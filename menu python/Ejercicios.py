from ctypes.wintypes import HLOCAL
from Menu import Ejercicios
from Modulos.funcionesMatematicas import *
from Paquete1.funcionesCadena import *
from Paquete1.funcionesNumericas import *
import time
import os

sub = Ejercicios()

videos = ["1) ejercicio 1'", "2) ejercicio 2", "3) ejercicio 3",
          "4) ejercicio 4", "5) ejercicio 5", "6) ejercicio 6", "7) ejercicio 7", "8) ejercicio 8", "9) ejercicio 9",
          "10) ejercicio 10", "11) ejercicio 11", "12) ejercicio 12", "13) ejercicio 13",
          "14) ejercicio 14", "15) ejercicio 15", "16) ejercicio 16", "17) ejercicio 17", "18) ejercicio 18",
          "19) ejercicio 19", "20) ejercicio 20", "21) ejercicio 21", "22) ejercicio 22",
          "23) ejercicio 23", "24) ejercicio 24", "25) ejercicio 25",
          "26) ejercicio 26", "27) ejercicio 27", "28) ejercicio 28",
          "29) ejercicio 29", "30) ejercicio 30", "31) ejercico 31",
          "32) ejercicio 32", "33) ejercicio 33", "34) ejercicio 34",
          "35) ejercicio 35", "36) ejercicio 36", "37) ejercicio 37", "38) salir"  ]
opcion = ""
while opcion != 38:
    os.system("cls")
    opcion = sub.menu(videos, "Menú ")


    if opcion == "1":
        print("Presentar por pantala -HOLA MUNDO-")
        print("Hola Mundo")
        input("Enter para salir")
        os.system("cls")

    elif opcion == "2":
        print("VARIABLES ")
        Nombre = "Joel Campoverde"
        print(Nombre)
        edad = 25
        print(edad)
        edad = True
        print(edad)
        sueldo = 205.10
        print(sueldo)
        time.sleep(2)
        os.system("cls")

    elif opcion == "3":
        print("conversion en python")
        numero1 = "35"
        numero2 = "18"
        print(numero1 + numero2)
        num1 = int(numero1)
        num2 = int(numero2)
        print(numero1 + numero2)
        sueldo = 1200.43
        sueldoEntero = int(sueldo)
        print(sueldoEntero)
        valor = "450.89"
        ValorDecimal = float(valor)
        print(ValorDecimal * 3)
        edad = 100
        print(len(str(edad)))
        time.sleep(1)
        time.sleep(3)
        os.system("cls")

    elif opcion == "4":
        print("operaciones con python")
        entero = 23
        decimal = 31.78
        complejo = 12 + 5j
        # Booleano= True
        """
        Print (entero)
        print (decimal)
        print (boleano)
        """
        num1 = 20
        num2 = 4
        print("suma:", (num1 + num2))
        print("resta:", (num1 - num2))
        print("multiplicacion:", (num1 * num2))
        print("Division:", (num1 / num2))
        print("division exacta:", (num1 // num2))
        print("Potencia:", (num1 ** num2))
        time.sleep(10)
        os.system("cls")

    elif opcion == "5":
        print("CONCATENACION")
        os.system("cls")
        texto1 = "Hola"
        texto2 = "Mundo"
        textoFinal = texto1 + "" + texto2
        print(textoFinal)

        print("El saludo es: %s %s" % (texto1, texto2))

        SaludoFinal = "saludo:{0} {1}".format(texto1, texto2)
        print(SaludoFinal)
        saludoFina12 = "saludo: {y} {x}".format(x=texto1, y=texto2)
        print(saludoFina12)
        time.sleep(10)

    elif opcion == "6":
        print("Funcion de cadenas")
        texto = "Bienvenidos a mi tarea s9 "
        print(texto)
        print(texto.lower())
        print(texto.upper())
        print(texto.title())
        print(texto.find("al"))
        print(texto.count("e"))

        textoFinal = texto.replace("e", "3")
        print(textoFinal)
        valor = texto.isnumeric()
        print(valor)
        cadenaSeparada = texto.split(" ")
        print(cadenaSeparada)
        time.sleep(10)
        os.system("cls")

    elif opcion == "7":
        print("TUPLAS")
        tupla = (1, 2, 3)
        print(tupla)
        tupla2 = (7, "Eduardo,true 4,50.1, 16+ 7j ,15,""Congratulacion,false")
        print(tupla)
        tupla3 = (9, 3, 4, 5, 6)
        print(tupla)
        print(tupla2[1])

        print(tupla2[-1])
        print(tupla2[0:4])
        print(tupla2[-2])

        a, b, c = tupla
        print(a)
        print(b)
        print(c)

        tuplafinal = tupla + tupla3
        print(tuplafinal)

        print(tuplafinal.count(21))
        print(tuplafinal.index(3))
        time.sleep(10)
        os.system("cls")

    elif opcion == "8":
        print("LISTAS ")
        lista1 = ["Genesis", 25, 98.3, True, "Sara", 56.3]
        print(lista1)
        print(lista1[:])
        print(lista1[2])
        print(lista1[-1])

        print(lista1[0:3])
        print(lista1[:2])
        print(lista1[3:])

        lista1.append("GenesisSara")
        print(lista1)

        lista1.insert(4, "Ecuador")
        print(lista1)

        lista1.extend(["Eduardo", 110, False])
        print(lista1)

        print(lista1.index("Eduardo"))

        lista1.remove(56.3)
        print(lista1)

        lista1.pop()
        print(lista1)

        lista2 = ["Milagro", "Quito"]
        lista3 = lista1 + lista2
        print(lista3)

        print(lista2 * 4)

        print("GenesisSara" in lista1)

        time.sleep(10)
        os.system("cls")

    elif opcion == "9":
        print("DICCIONARIO")

        miDiccionario = {"Colombia": "Bogota", "Argentina": "Buenos Aires", "Ecuador": "Quito"}
        print(miDiccionario["Argentina"])
        print(miDiccionario)

        miDiccionario["Colombia"] = "Bogota"
        print(miDiccionario)

        miDiccionario["Ecuador"] = "Quito"
        print(miDiccionario)

        del miDiccionario["Colombia"]
        print(miDiccionario)

        dic2 = {"Eduardo": "Lopez", 25: True, "Sueldo": 150.80}
        print(dic2[25])

        llaves = ("España", "Francia", "Inglaterra")
        dicPaises = {llaves[0]: "Madrid", llaves[1]: "París", llaves[2]: "Londres"}
        print(dicPaises)

        datosPersonales = {"Ape": "Lopez", "Anios": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
        print(datosPersonales)
        print(datosPersonales["Anios"])

        print(datosPersonales.get('Apel', "Eduardo"))

        print(datosPersonales.keys())
        valores = tuple(datosPersonales.values())
        print(valores)
        time.sleep(10)
        os.system("cls")

    elif opcion == "10":
        print("LECTURA DE DATOS POR TECLADO ")
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        sueldo = float(input("Ingrese su sueldo: "))
        print("Hola, " + nombre)
        edadFutura = edad + 20
        print("Tu edad es:", edad)
        print("Tu edad (dentro de 20 años) será:", edadFutura)
        print("Tu sueldo es:", sueldo)
        time.sleep(10)
        os.system("cls")

    elif opcion == "11":
        print("ESTRUCTURA CONDICIONAL ")
        edad = int(input("Ingrese su edad:"))
        if edad >= 18:

            print("Eres Mayor de edad.")
        elif edad == 18:

            print("Tienes 18 años!")

        else:

            print("No eres mayor de edad.")
        time.sleep(10)
        os.system("cls")

    elif opcion == "12":
        print("FUNCIONES ")


        def saludar():

            print("Eduardo")
            print("Campoverde")
            return "Hola"


        print(saludar())


        def evaluarSueldoMinimo(sueldo):

            if sueldo >= 850:
                print("Cumples con el sueldo")
            else:
                print("Ganas menos que el sueldo mínimo")


        evaluarSueldoMinimo(900)
        time.sleep(10)
        os.system("cls")

    elif opcion == "13":
        print("OPERADORES LOGICOS")
        distancia = 1200
        numerohermanos = 4
        salarioPadres = 1500
        tieneBeneficio = False
        if (distancia > 100 and numerohermanos > 2) or salarioPadres:
            tieneBeneficio = True
            print(not tieneBeneficio)
            if (5 > 3) and (8 < 6):
                print("Verdad")
            else:
                print("Falsedad")
        time.sleep(10)
        os.system("cls")

    elif opcion == "14":
        print("OPERADOR TERNARIO")
        sexos = ("Hombre", "Mujer")

        posicion = True
        sexo = sexos[posicion]
        print(sexo)
        time.sleep(2)
        os.system("cls")

        sexo = sexos[not posicion]
        print(sexo)
        time.sleep(2)
        os.system("cls")

    elif opcion == "15":
        print("RANGE")
        numeros = range(5)
        print(numeros[1])
        numeros1 = range(4, 10)
        print(numeros1[5])
        numeros2 = range(10, 100, 8)
        print(numeros2[9])
        time.sleep(10)
        os.system("cls")

    elif opcion == "16":
        print("BUCLE FOR EN PYTHON")
        for i in range(1, 13):
            print("{} x {} es: {}".format(i, i, (i * i)))
        time.sleep(2)
        os.system("cls")

        for nom in ["Eduardo", "Joel", "Gonzalez", "Campoverde"]:
            print("Cantidad de letras de {} es: {}".format(nom, len(nom)))
        time.sleep(10)
        os.system("cls")

    elif opcion == "17":
        print("IF CON TUPLAS Y LISTAS ")
        print("***** Curso *****")
        print("Matematica - Biologia - Lenguaje -Ciencias")
        curso = input("Ingrese el curso deseado: ")

        if curso in ("Matematica", "Biologia", "Lenguaje", "Ciencias"):
            print("Curso {0} seleccionado.".format(curso))
        else:
            print("No existe ese curso...")
        time.sleep(10)
        os.system("cls")

    elif opcion == "18":
        print("FACTORIAL DE UN NUMERO ")
        numero = int(input("Ingrese un número: "))
        factorial = 1
        for n in range(1, (numero + 1)):
            factorial *= n
        print("El factorial de {} es: {}".format(numero, factorial))
        time.sleep(10)
        os.system("cls")

    elif opcion == "19":
        print("BUCLE WHILE ")
        indice = 1
        while indice < 10:
            print("El número actual es: {}".format(indice))
            indice = 1 + indice

        print("Programa finalizado")
        time.sleep(3)
        os.system("cls")

        inicio = 2
        while inicio <= 100:
            print("El número actual es: {}".format(inicio))
            inicio = inicio + 2

        print("Programa finalizado")
        time.sleep(10)
        os.system("cls")

    elif opcion == "20":
        print("---Break---")
        # Break: Permite salir de un bucle cuando se cumple una condición.
        for numero in range(1, 6):
            if numero == 3:
                break
            print("El número es: {0}".format(numero))
            print("Bucle terminado.")
        # Continue: Omite una parte del bucle cuando se cumple una condición y
        # continúa con el resto.
        print("---Continue---")
        for numero in range(1, 6):
            if numero == 3:
                continue  # Continúa con el resto del bucle.
            print("El número es: {0}".format(numero))
            print("Bucle terminado.")
        # Pass: Permite continuar con una sentencia o función que ya no tiene
        # o aún no tiene un bloque de código útil.
        print("Pass")
        for numero in range(1, 6):
            if numero <= 3:
                # Aquí no pasa nada y el bucle sigue trabajando.
                pass
        else:
            print("El siguiente valor es mayor a 3:")
            print("El número es: {0}".format(numero))
            print("Bucle terminado.")


            def funcionSinImplementar():
                pass
        time.sleep(10)
        os.system("cls")

    elif opcion == "21":
        print("GENERADORES")
        """
        def generaMultiplos7(limite):
            numero = 1
            listaNumeros = []
            while numero <= limite:
            listaNumeros.append(numero * 7)
            numero = numero + 1
            return listaNumeros  # Retorna toda la lista creada.
            print(generaMultiplos7(10))
         """


        def generadorMultiplos7(limite):

            numero = 1
            while numero <= limite:
                yield numero * 7  # Ceder. La instrucción "yield" genera un objeto iterable.
                numero = numero + 1


        obtieneMultiplos7 = generadorMultiplos7(10)
        """
        print(obtieneMultiplos7)
            for n in obtieneMultiplos7:
            print(n)
        """
        # next(): Retorna el siguiente elemento de un objeto iterable:
        print(next(obtieneMultiplos7))
        print("Acá hay 300 líneas de código...")
        print(next(obtieneMultiplos7))
        print("Acá hay 1000 líneas de código...")
        print(next(obtieneMultiplos7))

        time.sleep(10)
        os.system("cls")

    elif opcion == "22":
        print("GENERADORES PARTE 2 ")


        def devuelveLenguaje(*Lenguajes):
            for leng in Lenguajes:
                yield from leng


        lenguajesObt = devuelveLenguaje("Python", "Java", "PHP", "Ruby", "JavaScript")
        print(next(lenguajesObt))
        print(next(lenguajesObt))
        time.sleep(10)
        os.system("cls")

    elif opcion == "23":
        print("EXCEPCIONES")
        numero1 = 20
        numero2 = 2

        try:
            print("La visión de {} entre {} es: {}".format(numero1, numero2, (numero1 / numero2)))
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
        finally:
            print("El programa ha finalizado")
        time.sleep(10)
        os.system("cls")

    elif opcion == "24":
        print("SENTENCIA RAISE ")


        def evaluarNota(nota):
            if nota < 0:
                raise ValueError("Valor incorrecto...")
            elif nota >= 16:
                print("Excelente")
            elif nota >= 11:
                print("Aprobado")
            else:
                print("Desaprobado")

            evaluarNota(19)
            print("Este es el fin de mi programa.")


        time.sleep(10)
        os.system("cls")

    elif opcion == "25":
        print("MODULOS ")
        from Modulos.funcionesMatematicas import multiplicar, sumar

        print(sumar(5, 6))
        print(multiplicar(5, 6))

        time.sleep(10)
        os.system("cls")

    elif opcion == "26":
        print("PAQUETES ")


        class Persona():
            apellidos = ""
            nombres = ""
            edad = 0
            despierta = False

            def despertar(self):
                self.despierta = True
                print("Buenos días")


        persona1 = Persona()
        persona1.apellidos = "Campoverde Gonzalez"
        print(persona1.apellidos)
        persona1.despertar()
        persona2 = Persona()
        persona2.apellidos = "Joel Eduardo"
        print(persona2.apellidos)
        time.sleep(10)

    elif opcion == "27":
        print("CONSTRUCTORES DE CLASE ")


        class Curso():

            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro


        curso1 = Curso("Matemáticas", 5, "Ingeniería civil")
        print(curso1.nombre)
        curso2 = Curso("Lenguaje", 4, "Ingeniería industrial")
        print(curso2.nombre)
        time.sleep(10)

    elif opcion == "28":
        print("Encapsulamiento de variables ")


        class Curso():

            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Presencial"

            def mostrarDatos(self):
                dat = "Nombre: {} / Créditos: {} / Modo de impartición: {}"
                print(dat.format(self.nombre, self.creditos, self.__imparticion))


        cur = Curso("Matemáticas", 5, "Ingeniería civil")
        cur.mostrarDatos()
        time.sleep(10)

    elif opcion == "29":
        print("ENCAPSULAMIENTO DE METODOS ")


        class Curso():

            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Presencial"

            def mostrarDatos(self):
                dat = "Nombre: {} / Créditos: {} / Modo de impartición: {}"
                print(dat.format(self.nombre, self.creditos, self.__imparticion))
                docenteAsig = self.__verificarDocente()
                if docenteAsig:
                    print("Existe el docente")
                    time.sleep(2)
                    os.system("cls")
                else:
                    print("No es necesario asignar un docente")

            def __verificarDocente(self):
                print("Verificando si existe un docente asignado")
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False


        curso = Curso("Matemáticas", 5, "Ingeniería civil")
        curso.mostrarDatos()
        time.sleep(3)

    elif opcion == "30":
        print("METODOS ACCESORES GET AND SET ")


        class Cuenta():

            def __init__(self, pro, sal, mon):
                self.__propietario = pro
                self.__saldo = sal
                self.__moneda = mon

            # Getters (métodos GET)
            def get_Saldo(self):
                return self.__saldo

            def get_Propietario(self):
                return self.__propietario

            def get_Moneda(self):
                return self.__moneda

            # Setters (métodos SET)
            def set_Moneda(self, moneda):
                self.__moneda = moneda


        cuenta1 = Cuenta("JOEL CAMPOVERDE", 15000, "pesos")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_Moneda("Dólares")
        print(cuenta1.get_Moneda())
        time.sleep(10)

    elif opcion == "31":
        print("METODOS DE CLASE")


        class Curso():

            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Presencial"

            def mostrarDatos(self):
                dat = "Nombre: {} / Créditos: {} / Modo de impartición: {}"
                print(dat.format(self.nombre, self.creditos, self.__imparticion))
                docenteAsig = self.__verificarDocente()
                if docenteAsig:
                    print("Existe el docente")
                    time.sleep(2)
                    os.system("cls")
                else:
                    print("No es necesario asignar un docente")

            def __verificarDocente(self):
                print("Verificando si existe un docente asignado")
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False

            def __str__(self):
                texto = "Nombre: {} Créditos {}"
                return texto.format(self.nombre, self.creditos)


        curso = Curso("Matemáticas", 5, "Ingeniería civil")
        print("Método __str__")
        print(curso)
        curso.mostrarDatos()
        time.sleep(10)

    elif opcion == "32":
        print("Herencia ")


        class Persona():
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.nomrbreMaterno = apeMat
                self.nombres = nom

            def mostrarNombreCompleto(self):
                txt = "{} {},{}"
                return txt.format(self.apellidoPaterno, self.nomrbreMaterno, self.nombres)


        class Estudiante(Persona):
            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro


        # estu1 = Estudiante("Torres", "López", "Juan", "Ingeniería Civil")
        per1 = Persona("Torres", "López", "Juan")
        # print(estu1.mostrarNombreCompleto())
        # print(estu1.profesion)
        # estu1.datos()

        print(isinstance(per1, Estudiante))
        time.sleep(3)

    elif opcion == "33":
        print("SOBREESCRITURA DE METODOS")


        class Persona():
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.nomrbreMaterno = apeMat
                self.nombres = nom

            def mostrarNombre(self):
                txt = "{} {},{}"
                return txt.format(self.apellidoPaterno, self.nomrbreMaterno, self.nombres)

            def datos(self):
                print(self.mostrarNombre())


        class Estudiante(Persona):
            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("La profesión es: {}".format(self.profesion))


        estu = Estudiante("Joel ", "Eduardo", "Campoverde", "Ingeniero software")
        estu.datos()
        time.sleep(3)

    elif opcion == "34":
        print("PRINCIPIO DE SUSTITUCION ")


        class Persona():
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.nomrbreMaterno = apeMat
                self.nombres = nom

            def mostrarNombre(self):
                txt = "{} {},{}"
                return txt.format(self.apellidoPaterno, self.nomrbreMaterno, self.nombres)

            def datos(self):
                print(self.mostrarNombre())


        class Estudiante(Persona):
            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("La profesión es: {}".format(self.profesion))


        per = Persona("joel", "eduardo", "campoverde")
        print("Es el objeto 'per' instancia de la clase Estudiante?")
        print(isinstance(per, Estudiante))
        time.sleep(10)

    elif opcion == "35":
        print("HERENCIA MULTIPLE ")


        class ClaseA():
            def __init__(self, par1, par2):
                self.parametro1 = par1
                self.parametro2 = par2

            def mostrar(self):
                print(self.parametro1 + self.parametro2)


        class ClaseB():
            def __init__(self, par3, par4, par5):
                self.parametro3 = par3
                self.parametro4 = par4
                self.parametro5 = par5


        class ClaseX(ClaseA, ClaseB):
            pass


        cX1 = ClaseX(15, 21)
        cX1.mostrar()
        time.sleep(10)

    elif opcion == "36":
        print("POLIMORFISMO ")


        class Estudiante():

            def describir(self):
                print("Soy  un estudiante.")


        class Docente():

            def describir(self):
                print("Me dedico a enseñar cursos.")


        class Trabajador():

            def describir(self):
                print("Trabajo dentro de una gran empresa.")


        def describirPersona(persona):
            persona.describir()


        doc1 = Trabajador()
        describirPersona(doc1)
        time.sleep(4)

    elif opcion == "37":
        print("RELACIONES ENTRE CLASES")


        class Pais():

            def __init__(self, nom, pre):
                self.nombre = nom
                self.presidente = pre

            def __str__(self):
                txt = "País: {0} - Presidente: {1}"
                return txt.format(self.nombre, self.presidente)


        class Ciudad():

            def __init__(self, nom, hab, pai):
                self.nombre = nom
                self.habitantes = hab
                self.pais = pai

            def __str__(self):
                txt = "Ciudad: {0} - N° Habitantes: {1} ({2})"
                return txt.format(self.nombre, self.habitantes, self.pais)


        class Urbanizacion():

            def __init__(self, nom, ciu):
                self.nombre = nom
                self.ciudad = ciu

            def __str__(self):
                txt = "Urbanización: {0} ({1})"
                return txt.format(self.nombre, self.ciudad)


        pais1 = Pais("Ecuador", "joel campoverde")
        print(pais1)

        ciudad1 = Ciudad("Quito", 150000, pais1)
        print(ciudad1)

        urba1 = Urbanizacion("Las Pilas", ciudad1)
        print(urba1)
        time.sleep(10)
    input("ha salido")
