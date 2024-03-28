#program orientado a aobjetos que define una clase perosna
#con sus stributos y metodos

class Persona():
    
    def __init__(self):
        self.nombre = "Ana"
        self.fechaNacimiento = "21-10-2020"
        self.horaNacimiento = "14:00"
        self.lugarNacimento = "Apizaco"
        self.genero= "Femenino"
    
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

print("Nombre de la persona creada: ", objeto1.getNombre())
print("El genero es: ",objeto1.getGenero())

print("Todos los datos de la persona son:")
objeto1.decir_datos()