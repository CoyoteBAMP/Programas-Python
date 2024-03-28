class Persona():
    def __init__(self, nomb,fecha,hora,lugar,gen):
        self.nombre = nomb
        self.fechaNacimiento = fecha
        self.horaNacimiento = hora
        self.lugarNacimiento = lugar
        self.genero = gen

    def getNombre(self):
        return self.nombre
        
    
    def getGenero(self):
        return self.genero

    def decir_datos(self):
        print("Nombre: ", self.nombre)
        print("Fecha: ", self.fechaNacimiento)
        print("Hora:  ", self.horaNacimiento)
        print("Lugar: ", self.lugarNacimiento)
        print("Genero: ", self.genero)


#Se crea un objeto de la clase persona
objeto1= Persona("Ramiro","20-Agosot-2000","14:00","Apizaco","Masculino")
print("\nTodos los datos de la persona son: ")
objeto1.decir_datos()

input()
objeto2= Persona("Ana","20-Enero-2000","05:00","Tlaxcala","Femenino")
print("\nTodos los datos de la persona son: ")
objeto2.decir_datos()

input()
nom= input("Nombre de la persona: ")
fecha= input("Su fecha de naciemiento: ")
hora= input("Y la hora?: ")
lugar= input("Lugar de naciemiento: ")
gen= input("su genero?")
objeto3= Persona(nom,fecha,hora,lugar,gen)
print("\nTodos los datos de la persona son: ")
objeto2.decir_datos()

print("El nombre de la ultima persona es: ",objeto3.getNombre())