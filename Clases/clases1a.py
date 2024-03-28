class Persona(): 
    # Método constructor de la clase
    def __init__(self,nom,fecha,hora,lugar,genero):
        self.nombre = nom
        self.fechaNacimiento= fecha
        self.horaNacimiento= hora
        self.lugarNacimiento= lugar
        self.genero= genero
        
    def getNombre(self):
        return self.nombre
    
    def getGenero(self):
        return self.genero
    
    def decir_datos(self):
        print("Nombre: ", self.nombre)
        print("Fecha : ", self.fechaNacimiento)
        print("Hora :  ", self.horaNacimiento)
        print("Lugar : ", self.lugarNacimiento)
        print("Genero: ", self.genero)
        
    
# Se crea un objeto de la clase persona
objeto1 = Persona("Mary","25-Marzo-2000","14:30", "Tlaxcala","Femenino")

print("Nombre de la persona1 : ", objeto1.getNombre())
print("El genero es: ", objeto1.getGenero())

print("Todos los datos de la persona1 son: ")
objeto1.decir_datos()

objeto2 = Persona("Roberto","20-Junio-2001","10:00", "Apizaco","Masculino")
print("\nTodos los datos de la persona2 son: ")
objeto2.decir_datos()