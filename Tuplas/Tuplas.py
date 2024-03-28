import os
tupla= (4,6,8,10) 
numeros= (1,2,3,4,5,6,7,8)
val=0
while val != 5:
    os.system("cls")
    print("Menú de opciones:")
    print("1= Insertar")
    print("2= Visualizar y la longitud")
    print("3= Eliminar")
    print("4= Modificar")
    print("5= Salir")
    opcion=int(input("¿Que quieres hacer con esta lista? "))
    
    if opcion==1:
        os.system("cls")
        dato=input("Ingresa el nuevo dato: ")
        lista=list(tupla)
        lista.extend([dato])
        tupla=tuple(lista)
        print("El nuevo contenido de la lista es= ",tupla)
        input("Presione <<Enter>> para continuar... ")
    elif opcion ==2:
        os.system("cls")
        print("El contenido de la tupla es= ",tupla)
        print(len(tupla))
        input("Presione <<Enter>> para continuar... ")
    elif opcion==3:
        os.system("cls")
        elemento=int(input("¿Cual numero deseas eliminar? "))
        lista=list(tupla)
        lista.remove(elemento)
        tupla=tuple(lista)
        print("El nuevo contenido de la lista es= ",tupla)
        input("Presione <<Enter>> para continuar... ")
    elif opcion==4:
        os.system("cls")
        print("Menú de opciones:")
        print("1= Cambiar tupla a lista")
        print("2= Intercambiar el contenido de las tuplas")
        modificar=int(input("¿Que quieres hacer con esta tupla? "))

        if modificar==1:
            os.system("cls")
            print("Se va a convertir la tupla a lista")
            lista=list(tupla)
            print("El nuevo contenido de la lista es= ",lista)
            input("Presione <<Enter>> para continuar... ")
        elif modificar==2:
            os.system("cls")
            print("Se va a Intercambiar el contenido de las tuplas ")
            (tupla,numeros)=(numeros,tupla)
            print("El nuevo contenido de tupla es= ",tupla)
            input("Presione <<Enter>> para continuar... ")
        else:
            print("Valor incorrecto ")
            input("Presione <<Enter>> para continuar... ")
    elif opcion==5:
            os.system("cls")
            print("Estas saliendo del programa")
            input("Presione <<Enter>> para continuar... ")
            quit()
