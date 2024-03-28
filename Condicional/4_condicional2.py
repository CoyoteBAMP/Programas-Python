''' PROGRAMA QUE LEE UN NUMERO DESDE TECLADO E INDICA SI PERTENECE A 
    UNIDADES, DECENAS, CENTAS O MILLARES.
'''

num= int(input("Ingresa un numero: "))

if num > 0 and num < 10000:    #Condicional para validar numero
    if num < 10:               #Condicional multiple para determinar tipo de numero
        print("El numero pertenece a las unidades")
    elif num < 100:
        print("El numero pertenece a las decenas")
    elif num < 1000:
        print("El numero pertenece a las centenas")
    elif num < 10000:
        print("El numero pertenece a los millares")
else:
    print("El numero no es valido")

#Investigar 