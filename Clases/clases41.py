import os
grupo = []

class Persona():
    def __init__(self, _nombre, _c1, _c2, _c3):
        self.nombre = _nombre
        self.c1 = _c1
        self.c2 = _c2
        self.c3 = _c3
        self.prom = (self.c1+self.c2+self.c3)/3

    def mostrarDatos(self):
        print("{} \t{} \t{} \t{} \t{}".format(self.nombre,self.c1,self.c2,self.c3,"{:.4}".format(self.prom)))

    def modificarNombre(self,nombre):
        self.nombre = nombre
        print("Se modificaron los datos con exito")
        input("Presione <<Enter>> para continuar... ")
    
    def modificarNota1(self,nota1):
        self.c1 = nota1
        self.prom = (self.c1+self.c2+self.c3)/3
        print("Se modificaron los datos con exito")
        input("Presione <<Enter>> para continuar... ")
    
    def modificarNota2(self,nota2):
        self.c2 = nota2
        self.prom = (self.c1+self.c2+self.c3)/3
        print("Se modificaron los datos con exito")
        input("Presione <<Enter>> para continuar... ")
    
    def modificarNota3(self,nota3):
        self.c3 = nota3
        self.prom = (self.c1+self.c2+self.c3)/3
        print("Se modificaron los datos con exito")
        input("Presione <<Enter>> para continuar... ")

def registrarEstudiante():
    os.system("cls")
    print("ESTAS EN EL MODULO DE REGISTRO DE ESTUDIANTES: ")
    nom= input("Ingresa el nombre: ")
    print("\nCalificaciones validas entre 0 a 100")
    cal1= int(input("Ingresa la calificacion 1: "))
    cal2= int(input("Ingresa la calificacion 2: "))
    cal3= int(input("Ingresa la calificacion 3: "))
    objAlumno = Persona(nom, cal1, cal2, cal3)
    grupo.append(objAlumno)
    input("Presione <<Enter>> para continuar... ")

def listadoEstudiantes():
    os.system("cls")
    print("ESTAS EN EL MODULO DE VISUALIZACION DE DATOS: ")
    for objAlumno in grupo:
        objAlumno.mostrarDatos()
    
    input("Presione <<Enter>> para continuar... ")

def buscarEstudiante():
    os.system("cls")
    print("ESTAS EN EL MODULO DE BUSCAR UN ESTUDIANTE: ")
    buscando=input("Ingresa el nombre del alumno a buscar: ")
    for objAlumno in grupo:
        if buscando== objAlumno.nombre:
            objAlumno.mostrarDatos()
    input("Presione <<Enter>> para continuar... ")


def modificarDatos():
    os.system("cls")
    buscando=input("Ingresa el nombre del alumno a modificar: ")
    for objAlumno in grupo:
        if buscando== objAlumno.nombre:
            print("ESTAS EN EL MODULO PARA MODIFICAR DATOS: ")
            print("Menu de opciones")
            print("1= Modificar nombre")
            print("2= Modificar calificacion 1")
            print("3= Modificar calificacion 2")
            print("4= Modificar calificacion 3")
            des=int(input("¿Que quiere hacer? "))

            if des==1:
                os.system("cls")
                nombre= input("Introduce el nuevo nombre: ")
                objAlumno.modificarNombre(nombre)

            elif des==2:
                os.system("cls")
                nota1= int(input("Nueva nota 1: "))
                objAlumno.modificarNota1(nota1)
                
            elif des==3:
                os.system("cls")
                nota2= int(input("Nueva nota 2: "))
                objAlumno.modificarNota2(nota2)
                
            elif des==4:
                os.system("cls")
                nota3= int(input("Nueva nota 3: "))
                objAlumno.modificarNota3(nota3)
            else:
                print("Valor incorrecto")    
    
def eliminarAlumno():
    os.system("cls")
    print("ESTAS EN EL MODULO PARA ELIMINAR DATOS: ")
    buscando=input("Ingresa el nombre del alumno a eliminar: ")
    for objAlumno in grupo:
        if buscando== objAlumno.nombre:
            grupo.pop(grupo.index(objAlumno))
    print("Se elimino al alumno con exito")
    input("Presione <<Enter>> para continuar... ")

def promedioGrupo():
    os.system("cls")
    num=len(grupo)
    print("MODULO DE PROMEDIO DE GRUPO: ")
    suma=0 
    for objAlumno in grupo:
        suma = suma + objAlumno.prom
    promgrup=suma/num
    print("El promedio del grupo es: ","{:.4}".format(promgrup))
    input("Presione <<Enter>> para continuar... ")

def promediAlto():
    os.system("cls")
    promAlto= []
    print("MODULO DE VISUALIZAR PROMEDIO MAS ALTO: ")
    for objAlumno in grupo:
        promAl =0+ objAlumno.prom
        promAlto.extend([promAl])
    max_item= max(promAlto, key=float)
    print( "El promedio mas alto es: ","{:.4}".format(max_item))
    print("\nLos alumnos con este promedio son:")
    for objAlumno in grupo:
        if objAlumno.prom == max_item:
            objAlumno.mostrarDatos()
    input("Presione <<Enter>> para continuar... ")

def promediBajo():
    os.system("cls")
    promBajo= []
    print("MODULO DE VISUALIZAR PROMEDIO MAS BAJO: ")
    for objAlumno in grupo:
        promBa =0+ objAlumno.prom
        promBajo.extend([promBa])
    min_item= min(promBajo, key=float)
    print( "El promedio mas bajo es: ","{:.4}".format(min_item))
    print("\nLos alumnos con este promedio son:")
    for objAlumno in grupo:
        if objAlumno.prom == min_item:
            objAlumno.mostrarDatos()
    input("Presione <<Enter>> para continuar... ")

def noAprobados():
    os.system("cls")
    print("MODULO DE VISUALIZAR ALUMNOS NO APROBADOS : ")
    for objAlumno in grupo:
        if objAlumno.prom < 70:
            objAlumno.mostrarDatos()
    input("Presione <<Enter>> para continuar... ")


def menu():
    val=0
    while val != 6:
        os.system("cls")
        print("Menu de opciones")
        print("1= Ingresar")
        print("2= Vizualizar todos")
        print("3= Buscar Alumno")
        print("4= Modificar")
        print("5= Eliminar")
        print("6= Promedio del Grupo")
        print("7= Promedio mas alto")
        print("8= Promedio mas bajo")
        print("9= Alumnos no aprobados")
        print("10= Salir")
        des=int(input("¿Que quiere hacer? "))

        if des==1:
            registrarEstudiante()

        elif des==2:
            listadoEstudiantes()
        
        elif des==3:
            buscarEstudiante()
        
        elif des==4:
            modificarDatos()
        
        elif des==5:
            eliminarAlumno()
        
        elif des==6:
            promedioGrupo()
        
        elif des==7:
            promediAlto()
        
        elif des==8:
            promediBajo()
        
        elif des==9:
            noAprobados()
        
        elif des==10:
            os.system("cls")
            print("Estas saliendo del programa")
            input("Presione <<Enter>> para continuar... ")
            quit()
            
        else:
            print("valor incorrecto")

menu()