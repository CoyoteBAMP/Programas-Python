import os
lista= [0,1,2,3,4,5] 
print("El contenido de la lista es= ",lista)
val=0
while val != 5:

    print("Menú de opciones:") 
    print("1= Insertar")
    print("2= Visualizar")
    print("3= Eliminar")
    print("4= Salir")
    opcion=int(input("¿Que quieres hacer con esta lista? "))
    
    if opcion==1:
        os.system("cls")
        dato=input("Ingresa el nuevo dato: ")
        lista.extend([dato])
        print("El nuevo contenido de la lista es= ",lista)
    elif opcion ==2:
        os.system("cls")
        print("El contenido de la lista es= ",lista)
    elif opcion==3:
        os.system("cls")
        print("Menú de opciones:")
        print("1= Eliminar al final")
        print("2= Eliminar un valor especifico")
        eliminar=int(input("¿Que quieres hacer con esta lista? "))

        if eliminar==1:
            os.system("cls")
            print("Se va a eliminar el ultimo dato de la lista")
            lista.pop()
            print("El nuevo contenido de la lista es= ",lista)
        elif eliminar==2:
            os.system("cls")
            elemento=int(input("¿Cual numero deseas eliminar? "))
            lista.pop(elemento)
            print("El nuevo contenido de la lista es= ",lista)
        else:
            print("Valor incorrecto ")
    elif opcion==4:
            os.system("cls")
            print("Estas saliendo del programa")
            input("Presione <<Enter>> para continuar... ")
            quit()


 






