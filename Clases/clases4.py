class Persona():
    def __init__(self, _nombre, _c1, _c2, _c3):
        self.nombre = _nombre
        self.c1 = _c1
        self.c2 = _c2
        self.c3 = _c3
        
    
    def promedio(self):
        return ((self.c1+self.c2+self.c3)/3)
import os
os.system("cls")
nu=int(input("¿Cuantos alumnos deseas registrar? "))
suma=0
num=1
for i in range (nu):
    print("\nAlumno número",num)
    nom= input("Ingresa el nombre: ")
    cal1= int(input("\nIngresa la calificacion 1: "))
    cal2= int(input("Ingresa la calificacion 2: "))
    cal3= int(input("Ingresa la calificacion 3: "))
    objeto = Persona(nom, cal1, cal2, cal3)
    suma = suma + objeto.promedio()
    num= num + 1
    print("El promedio del alumno es= ","{:.3}".format(objeto.promedio()))

promedioGrupo = suma / nu
print("\nEl promedio grupal es: ", "{:.3}".format(promedioGrupo))
