import os
class Persona():
    
    def __init__(self):
        os.system("cls")
        self.nombre = input("Nombre de la persona: ")
        self.fechaNacimiento = input("Fecha de nacimiento: ") 
        self.horaNacimiento = input("Hora de nacimiento: ")
        self.lugarNacimento = input("Lugar: ")
        self.genero= input("Genero: ")

    def getNombre(self):
        return self.nombre

    def getGenero(self):
        return self.genero
    
    def decir_datos(self):
        print("Nombre: ", self.nombre)
        print("Fecha: ", self.fechaNacimiento)
        print("Hora: ", self.horaNacimiento)
        print("Lugar: ", self.lugarNacimento)
        print("Genero: ", self.genero)

objeto1= Persona()
objeto2= Persona()
input()
os.system("cls")
print("Datos ingresados para la primera persona: ")
objeto1.decir_datos()

input()
os.system("cls")
print("\nDatos ingresados para la segunda persona: ")
objeto2.decir_datos()