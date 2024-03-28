diccionario = {'Ricardo':'8971236405','Sergio':'1564789406'}
val=0
while val != 1:
    print("Menú de opciones:")
    print("1= Insertar/Modificar")
    print("2= Buscar")
    print("3= Borrar")
    print("4= Listar")
    print("5= Guardar")
    print("6= Salir")
    opcion=int(input("¿Que quieres hacer con esta lista? "))
    
    if opcion==1:
        nombre=input("Ingresa el nombre: ")
        for keys in diccionario.keys():
            if keys == nombre:
                print("El nombre ya se encuentra en la agenda")
                print(diccionario[nombre])
                opcion=input("¿Desean Modificarlo? ")
                if opcion == "S":
                    numero=input("Ingresa el nuevo numero:")
                    diccionario[nombre] = numero 
                    val=0
                    break
                elif opcion == "N":
                    break
            else:
                numero=input("Ingresa el numero: ")
                diccionario[nombre] = numero 
                break
    elif opcion ==2:
        nombre=input("¿Cual contacto quieres buscar? ")
        for keys in diccionario.keys():
            if keys == nombre:
                print("Los datos del contacto son:")
                print(diccionario[nombre])
                break
            else:
                print("El dato no se encuentra en la agenda")
                break

    elif opcion==3:
        elemento=(input("¿Cual persona deseas eliminar? "))
        for keys in diccionario:
            if keys == elemento:
                print("El nombre si esta en la agenda")
                print(diccionario[elemento])
                print(print(" Si = S / No = N "))
                opcion= input("¿Desean Eliminiralo? ").upper()
                if opcion == "S":
                    del diccionario[elemento]
                    break
                else:
                    break
            else:
                print("El nombre no se encuentra en la agenda")
                break
    elif opcion==4:
        print("El contenido de la agenda es: ")
        print(diccionario) 
    elif opcion==5:
        with open('Agenda.txt', 'w') as agenda:
            agenda.write(str(diccionario))
    elif opcion==6:
            quit()