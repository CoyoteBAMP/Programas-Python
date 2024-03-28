import os
diccionario = {'Brayan':'2074536981','Ximena':'1234567890','Pedro':'4568791501','Jose':'8456971205','Danae':'9865741230','Gabriel':'5316489780','Ricardo':'8971236405','Sergio':'1564789406'}
val=0
while val != 10:
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
        for keys in diccionario.keys():
            if keys == nombre:
                print("El nombre ya se encuentra en la agenda")
                print(diccionario[nombre])
                print(" Si = S / No = N ")
                opcion=input("¿Desean Modificarlo? ").upper()
                if opcion == "S":
                    numero=input("Ingresa el nuevo numero:")
                    diccionario[nombre] = numero 
                    print("El contenido de la agenda se actualizo correctamente")
                    input("Presione <<Enter>> para continuar... ")
                    val=0
                    break
                elif opcion == "N":
                    input("Presione <<Enter>> para regresar al menu... ")
                    break
            else:
                numero=input("Ingresa el numero: ")
                diccionario[nombre] = numero 
                print("El contenido de la agenda se actualizo correctamente")
                input("Presione <<Enter>> para continuar... ")
                break
    elif opcion ==2:
        os.system("cls")
        nombre=input("¿Cual contacto quieres buscar? ")
        for keys in diccionario.keys():
            if keys == nombre:
                print("Los datos del contacto son:")
                print(diccionario[nombre])
                input("Presione <<Enter>> para continuar... ")
                break
            else:
                print("El dato no se encuentra en la agenda")
                input("Presione <<Enter>> para continuar... ")
                break

    elif opcion==3:
        os.system("cls")
        elemento=(input("¿Cual persona deseas eliminar? "))
        for keys in diccionario:
            if keys == elemento:
                print("El nombre si esta en la agenda")
                print(diccionario[elemento])
                print(print(" Si = S / No = N "))
                opcion= input("¿Desean Eliminiralo? ").upper()
                if opcion == "S":
                    del diccionario[elemento]
                    print("El contenido de la agenda se actualizo correctamente")
                    input("Presione <<Enter>> para continuar... ")
                    break
                else:
                    input("Presione <<Enter>> para continuar... ")
                    break
            else:
                print("El nombre no se encuentra en la agenda")
                input("Presione <<Enter>> para continuar... ")
                break
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

