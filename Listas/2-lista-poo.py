import os
class Vehiculo(object):
    #Metodo constructor 
    def __init__(self, matricula, marca, modelo):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo


    #Metodo para accesar a los datos del objeto y mostrarlos
    def __str__(self):
        return "%s %s %s" % (self.matricula, self.marca, self.modelo)

class GestorVehiculos:
    def __init__(self):
        self.arregVehiculos = []

    def agregar(self,matricula, marca, modelo):
        movil = Vehiculo(matricula, marca, modelo)
        self.arregVehiculos.append(movil)

    def mostrarVehiculos(self):
        for movil in self.arregVehiculos:
            return ("{0} \n{1} \n{2}".format(movil.matricula, movil.marca, movil.modelo))

    #Este metodo permite mostrar el contenido de todos los objetos en el arreglo
    def __str__(self):
        salida = ""
        for movil in self.arregVehiculos:
            salida += str(movil) + "\n"
        return salida

    def buscar (self, clave, por="matricula"):
        for indice, movil in enumerate(self.arregVehiculos):
            if movil.__getattribute__(por) == clave:
                return indice
    
    def remover(self, clave, por="matricula"):
        indice = self.buscar(clave)
        if indice != None:
            self.arregVehiculos.pop(indice)
            return indice

    def mostrar(self):
        salida = ""
        for movil in self.arregVehiculos:
            salida += str(movil) + "\n"
        return salida

#Uso de las clases Vehiculos y GestorVehiculos

arreglo = GestorVehiculos()
os.system("cls")     
op = "S"
while op == "S":
    matricula= input ("Matricula del vehiculo: ")
    marca= input("Marca: ")
    modelo= input("Modelo:  ")
    arreglo.agregar(matricula, marca, modelo)
    op = input("¿Deseas agregar otro vehiculo? ").upper()

print("\n")
print(arreglo)

elemneto = input("\nMatricula del vehiculo a busacar: ")
print("El vehiculo esta registrado en la posición: ", arreglo.buscar(elemneto))

elemento = input("Mateicula del vehiculo a eliminar: ")
print("Se elimina vehiculo en posicion: ", arreglo.remover(elemento))

print("\n")
print(arreglo)

print("Los datos son: ","\n",arreglo.mostrarVehiculos())

