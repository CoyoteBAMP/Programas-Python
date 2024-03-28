class Persona(): 
    # Método constructor de la clase
    def __init__(self,nom,fecha,hora,lugar,genero):
        self.nombre = nom
        self.fechaNacimiento= fecha
        self.horaNacimiento= hora
        self.lugarNacimiento= lugar
        self.genero= genero
        
    
    def getGenero(self):
        return self.genero
    
    def decir_datos(self):
        print("Nombre: ", self.nombre)
        print("Fecha: ", self.fechaNacimiento)
        print("Hora:  ", self.horaNacimiento)
        print("Lugar: ", self.lugarNacimiento)
        print("Genero: ", self.genero)

#se crea un objeto de la clase persona
nombre=input("Nombre: ")
fecha=input("Fecha: ")
hora=input("Hora: ")
lugar=input("Lugar: ")
genero=input("Genero: ")
objeto1 = Persona(nombre,fecha,hora,lugar,genero)

print("\nTodos los datos de la persona son: ")
objeto1.decir_datos()
        