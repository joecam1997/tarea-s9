class Persona():
    # Propiedades, características o atributos:
    apellidos = ""
    nombres = ""
    edad = 0
    despierta = False

    # Funcionalidades:
    def despertar(self):
        # self: Parámetro que hace referencia a la instancia perteneciente a la clase.
        self.despierta = True
        print("Buen día.")


persona1 = Persona()
persona1.apellidos = "CAMPOVERDE GONZALEZ"
print(persona1.apellidos)
persona1.despertar()
print(persona1.despierta)

persona2 = Persona()
persona2.apellidos = "CAMPOVERDE MARIN"
print(persona2.apellidos)
# persona2.despertar()
print(persona2.despierta)