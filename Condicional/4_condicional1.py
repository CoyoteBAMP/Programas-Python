#SEntencias condicionales if .. elif .. else
n1 = 10
n2 = 100
n3 = 10
#Obtener el mayor de esos numeros
if n1 > n2 and n1 > n3:
    print("El primero es el mayor")
elif n2 > n1 and n2 > n3:
    print("El segundo es el mayor")
elif n3 > n1 and n3 > n2:
    print("El tercero es el mayor")
else:
    print("Los numeros son iguales")