numero=int(input("Ingresa un numero del 1 al 10: "))

if numero > 0 and numero <= 10:
    if numero == 1:
        numero= "I"
    elif numero == 2:
        numero = "II"
    elif numero == 3:
        numero = "III"
    elif numero == 4:
        numero = "IV"
    elif numero == 5:
        numero = "V"
    elif numero == 6:
        numero = "VI"
    elif numero == 7:
        numero = "VII"
    elif numero == 8:
        numero = "VIII"
    elif numero == 9:
        numero = "IX"
    elif numero == 10:
        numero = "X"
    print("El numero en romano es: ",numero)
else:
    print("El numero no es valido")

    

