import os
def ingresar ():
    num=int(input("¿Cuantos alumnos deseas ingresar?"))
    cal=int(input("¿Cuantos calificaciones tienen?"))
    for num in range(num):
        alumno = input("Nombre del alumno:")
        while alumno in alumnos:
            print("Alumno ya existe.")
            alumno = input("Nombre del alumno:")
        for nu in range (cal):
            notas=[]
            #promedios=[]
            nota = int(input("Dame una nota del alumno:"))
            notas.append(nota)
            prom = float(sum(notas)/len(notas))
            promedios.append(prom)
            #alumnos[alumno] = prom.copy()
            alumnos.setdefault(alumno, prom)

def promGrupo (proms):
    proGruo= (sum(proms)/len(proms))
    print("El promedio del grupo es: ", proGruo)

def PromMayor(prom):
    alto=max(prom)
    print("El promedio mas alto del grupo es: ", alto)

def PromMenor (prom):
    bajo=min(prom)
    print("El promedio mas alto del grupo es: ", bajo)

#def mostrar (alumno,notas,alumnos):
#    for alumno, notas in alumnos.items():
#        print("%s ha sacado de nota media %f" % (alumno,sum(notas)/len(notas)))
def mostrar():
    print(alumnos)

def menu():
    cont=0
    while cont==0:
        os.system("cls")
        print("Opciones:")
        print("1= Insertar")
        print("2= Promedio del grupo")
        print("3= Promedio más alto")
        print("4= Promedio más bajo")
        print("5= Mostrar Diccionario")
        print("6= Salir")
        des=int(input("¿Que quieres hacer? "))

        if des==1:
            os.system("cls")
            ingresar()
            input("Presiona <<enter>> para continuar")
        elif des==2:
            os.system("cls")
            promGrupo(promedios)
            input("Presiona <<enter>> para continuar")
        elif des==3:
            os.system("cls")
            PromMayor(promedios)
            input("Presiona <<enter>> para continuar")
        elif des==4:
            os.system("cls")
            PromMenor(promedios)
            input("Presiona <<enter>> para continuar")
        elif des==5:
            os.system("cls")
            #mostrar(alumno, notas, alumnos)
            mostrar()
            input("Presiona <<enter>> para continuar")
        elif des==6:
            os.system("cls")
            cont=1
            print("Vas a salir del programa")   
            input("Presiona <<enter>> para continuar")


alumnos = {}
#notas=[]
promedios=[]
alumno=""
menu()