import os
phone_book= {"Karla":123,"Jaime":254,"Ximena":564} 
val=0
while val != 5:
    os.system("cls")
    print("Menú de opciones:")
    print("1= Insertar")
    print("2= Visualizar")
    print("3= Eliminar")
    print("4= Modificar")
    print("5= Salir")
    opcion=int(input("¿Que quieres hacer con esta lista? "))
    
    if opcion==1:
        os.system("cls")
        nombre=(input("Ingresa el nuevo nombre: "))
        numero=input("Ingresa el nuevo numero: ")
        phone_book[nombre]=numero
        print("El nuevo contenido es= ",phone_book)
        input("Presione <<Enter>> para continuar... ")
    elif opcion ==2:
        os.system("cls")
        print("Menú de opciones:")
        print("1= Visualizar todos los numeros")
        print("2= Visualizar todos los nombres")
        print("3= Visualizar una persona en especifico")
        print("4= Todo")
        opcion=int(input("¿Que quieres hacer con esta lista? "))
        if opcion==1:
            os.system("cls")
            print(phone_book.values())
        elif opcion==2:
            os.system("cls")
            print(phone_book.keys())
        elif opcion==3:
            os.system("cls")
            persona=(input("¿De quien quieres ver el numero? "))
            print(phone_book[persona])
        elif opcion==4:
            print(phone_book)
        input("Presione <<Enter>> para continuar... ")
    elif opcion==3:
        os.system("cls")
        elemento=(input("¿Cual perosna deseas eliminar? "))
        del phone_book[elemento]
        print("El nuevo contenido es= ",phone_book)
        input("Presione <<Enter>> para continuar... ")
    elif opcion==4:
        os.system("cls")
        print("Menú de opciones:")
        print("1= Cambiar un numero")
        print("2= Cambiar nombre y numero")
        modificar=int(input("¿Que quieres hacer con esta tupla? "))
        if modificar==1:
            os.system("cls")
            nombre=input("¿De quien quieres hacer el cambio? ")
            nuenumero=input("Ingresa el nuevo numero: ")
            phone_book[nombre]=nuenumero
        elif modificar==2:
            os.system("cls")
            nombre=input("¿De quien quieres hacer el cambio? ")
            del phone_book[nombre]
            nuenombre=input("Ingresa el nuevo nombre: ")
            nuenumero=input("Ingresa el nuevo numero: ")
            phone_book[nuenombre]=nuenumero

        print("El nuevo contenido es= ",phone_book)
        input("Presione <<Enter>> para continuar... ")
    elif opcion==5:
            os.system("cls")
            print("Estas saliendo del programa")
            input("Presione <<Enter>> para continuar... ")
            quit()

