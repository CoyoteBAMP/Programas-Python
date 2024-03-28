from collections import deque
import os
def inserta():
    nombre = input("¿Cual es su nombre? ")
    cola.append(nombre)
    
def mencionar():
    while len (cola) > 0:
        siguiente = cola.popleft()
        print("Es el turno de ",siguiente)
        input("Presiona <<enter>> para continuar")


def mostrar():
    print("El contenido de la cola es: ",cola)

def menu():
    conta=0
    while conta==0:
        os.system("cls")
        print("Opciones")
        print("1= Insertar")
        print("2= Mostrar turnos")
        print("3= Mostrar cola")
        print("4= salir")
        opcion=int(input("\n¿Qué quieres hacer?"))
        
        if opcion==1:
            os.system("cls")
            inserta()
            input("Presiona <<enter>> para continuar")
        elif opcion==2:
            os.system("cls")
            mencionar()
            input("Presiona <<enter>> para continuar")
        elif opcion==3:
            os.system("cls")
            mostrar()
            input("Presiona <<enter>> para continuar")
        elif opcion==4:
            conta=1
            print("Vas a salir")
            input("Presiona <<enter>> para continuar")
        else:
            print("La opción no es valida")


cola = deque()
menu()


