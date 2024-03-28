#Programa que realice mediante un menu 
#Las principales operaciones de listas 
#Menu:
#Insertar elementos
#Buscar un elemento
#Eliminar un elemento
#Mostrar lista
#El menu incluira un ciclo repititivo con una opcion de salir
#Cada opcion se ejecuta en una funcion independiente (def)
import os

def insertar1(elemento):
    print("Vas a ingresar un nuevo elemento")
    lista.append(elemento) #Ingresa solo un elemento al final del lista
    print("El nuevo contedido es: ",lista)
    input("Presiona <<enter>> para continuar")

def insertar2(posi,elemento):
    print("Vas a ingresar un nuevo elemento en la posición ",posi)
    lista.insert(posi,elemento)
    print("El nuevo contedido es: ",lista)
    input("Presiona <<enter>> para continuar")

def buscar(elemento):
    print("Vas a buscar un elemento")
    busca = False
    eleme=elemento
    for i in range (len(lista)):
        bus=lista[i]
        if bus==eleme:
            busca= True
    if busca == True:
        print("El elemento ",elemento," si esta en la lista")
    else:
        print("El elemento ",elemento," no esta en la lista")
    input("Presiona <<enter>> para continuar")

def eliminar1():
    print("Vas a eliminar el ultimo elemento ")
    lista.pop()
    print("El nuevo contedido es: ",lista)
    input("Presiona <<enter>> para continuar")

def eliminar2(valor):
    print("Vas a eliminar un elemento por su valor")
    lista.remove(valor)
    print("El nuevo contedido es: ",lista)
    input("Presiona <<enter>> para continuar")

def mostrar():
    print("Vas a mostrar el contenido de la lista")
    print(lista)
    input("Presiona <<enter>> para continuar")


def menu():
    cont=0
    while cont==0:
        os.system("cls")
        print("Opciones:")
        print("1= Insertar")
        print("2= Buscar elemento")
        print("3= Eliminar")
        print("4= Mostrar lista")
        print("5= Salir")
        des=int(input("¿Que quieres hacer? "))

        if des==1:
            os.system("cls")
            print("Opciones:")
            print("1= Insertar un elemento al final")
            print("2= Insertar un elemento en un lugar en especifico")
            inse=int(input("¿Que quieres hacer? "))
            if inse==1:
                os.system("cls")
                eleme=int(input("¿Qué elemento quieres ingresar?"))
                insertar1(eleme)
            elif inse==2:
                os.system("cls")
                eleme=int(input("¿Qué elemento quieres ingresar?"))
                pos=int(input("¿En que pocisión quieres ingresarlo?"))
                insertar2(pos,eleme)
            else:
                os.system("cls")
                print("Dato no valido")
                input("Presiona <<enter>> para continuar")
        elif des==2:
            os.system("cls")
            eleme= int(input("¿Qué elemento quieres buscar?"))
            buscar(eleme)
        elif des==3:
            os.system("cls")
            print("Opciones:")
            print("1= Eliminar el ultimo elemento de la final")
            print("2= Eliminar un elemento por su valor")
            elim=int(input("¿Que quieres hacer? "))
            if elim==1:
                os.system("cls")
                eliminar1()
            elif elim==2:
                os.system("cls")
                eleme=int(input("¿Qué elemento quieres eliminar?"))
                eliminar2(eleme)
            else:
                os.system("cls")
                print("Dato no valido")
                input("Presiona <<enter>> para continuar")
        elif des==4:
            os.system("cls")
            mostrar()
        elif des==5:
            os.system("cls")
            cont=1
            print("Vas a salir del programa")   
            input("Presiona <<enter>> para continuar")


lista=[]
menu()
            

