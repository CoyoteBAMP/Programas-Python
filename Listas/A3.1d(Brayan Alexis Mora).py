import os
diccionario = {'Brayan':'2074536981','Ximena':'1234567890'}
val=0
while val != 5:
    os.system("cls")
    print("Menú de opciones:")
    print("1= Insertar/Modificar")
    print("2= Buscar")
    print("3= Borrar")
    print("4= Listar")
    print("5= Guardar")
    print("6= Salir")
    opcion=int(input("¿Que quieres hacer con esta lista? "))
    
    if opcion==1:
        os.system("cls")
        nombre=input("Ingresa el nombre: ")
        for keys in diccionario:
            if keys == nombre:
                print("El nombre ya se encuentra en la agenda")
                print(diccionario[nombre])
                print(" Si = S / No = N ")
                opcion=input("¿Desean Modificarlo?" ).upper()
                if opcion == "S":
                    numero=input("Ingresa el nuevo numero:")
                    diccionario[nombre] = numero 
                    print("El contenido de la agenda se actualizo correctamente")
                else: 
                    input("Presione <<Enter>> para continuar... ")
            elif keys != nombre :
                numero=input("Ingresa el numero: ")
                diccionario[nombre] = numero 
                print("El contenido de la agenda se actualizo correctamente")
        input("Presione <<Enter>> para continuar... ")
    elif opcion ==2:
        os.system("cls")
        nombre=input("¿Cual contacto quieres buscar")
        print("Los datos del contacto son:")
        print(diccionario[nombre])
        input("Presione <<Enter>> para continuar... ")
    elif opcion==3:
        os.system("cls")
        elemento=(input("¿Cual persona deseas eliminar? "))
        for keys in diccionario:
            if keys == nombre:
                print("El nombre si esta en la agenda")
                print(diccionario[elemento])
                opcion=input("¿Desean Eliminiralo?"  " Si = S / No = N").upper()
                if opcion == "S":
                    del diccionario[elemento]
                    print("El contenido de la agenda se actualizo correctamente")
            else:
                print("El nombre no se encuentra en la agenda")
        input("Presione <<Enter>> para continuar... ")
    elif opcion==4:
        os.system("cls")
        print("El contenido de la agenda es: ")
        print(diccionario)
        input("Presione <<Enter>> para continuar... ") 
    elif opcion==5:
        os.system("cls")
        with open('Agenda.txt', 'w') as agenda:
            agenda.write(str(diccionario))
    elif opcion==6:
            os.system("cls")
            print("Estas saliendo del programa")
            input("Presione <<Enter>> para continuar... ")
            quit()

