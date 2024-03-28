#Programa de operaciones aritmeticas basaicas utilizando funciones
import os

def sumar(n1,n2):
    os.system("cls")
    return n1 + n2

def restar(n1,n2):
    os.system("cls")
    return n1 - n2

def multiplicar(n1,n2):
    os.system("cls")
    return n1 * n2
    

def dividir(n1,n2):
    os.system("cls")
    return n1 / n2
    


def menu():
    conta=0
    while conta==0:
        os.system("cls")
        print("Opciones")
        print("1= sumar")
        print("2= restar")
        print("3= multiplicar")
        print("4= dividir")
        print("5= salir")
        opcion=int(input("\n¿Qué quieres hacer?"))
        
        if (opcion==1)or(opcion==2)or(opcion==3)or(opcion==4):
            num1=int(input("\nIngresa el PRIMER valor: "))
            num2=int(input("Ingresa el SEGUNDO valor: "))
        
        if opcion==1:
            suma= sumar(num1,num2)
            print("La suma es igual a = ",suma)
            input("Presiona <<enter>> para continuar")
        elif opcion==2:
            resta= restar(num1,num2)
            print("La resta es igual a = ",resta)
            input("Presiona <<enter>> para continuar")
        elif opcion==3:
            multiplicacion= multiplicar(num1,num2)
            print("La multiplicacion es igual a = ",multiplicacion)
            input("Presiona <<enter>> para continuar")
        elif opcion==4:
            division=dividir(num1,num2)
            print("La division es igual a = ",division)
            input("Presiona <<enter>> para continuar")
        elif opcion==5:
            conta=1
            print("Vas a salir")
            input("Presiona <<enter>> para continuar")
        else:
            print("La opción no es valida")



menu()

