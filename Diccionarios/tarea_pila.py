from collections import deque
import os
def insertar():
    codigo = input("¿Cual es el codigo de producto? ")
    pila.append(codigo)
    
def mencionar():
    while len (pila) > 0:
        siguiente = pila.pop()
        print("Se quita el producto con codigo ",siguiente)
        input("Presiona <<enter>> para continuar")


def mostrar():
    print("El contenido de la pila es: ",pila)

def menu():
    conta=0
    while conta==0:
        os.system("cls")
        print("Opciones")
        print("1= Apilar producto")
        print("2= Desapilar productos")
        print("3= Mostrar pila")
        print("4= salir")
        opcion=int(input("\n¿Qué quieres hacer?"))
        
        if opcion==1:
            os.system("cls")
            insertar()
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


pila = deque()
menu()

