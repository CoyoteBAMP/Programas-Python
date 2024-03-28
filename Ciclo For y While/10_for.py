#La sentencia for permite iterar un mensaje especifico de veces
#Una sentencia o conjunto de sentencias.

n= int(input("¿Cuantos numeros deseas sumar? "))
suma=0
for indice in range(n):
    numero = float(input("Introduce un numero: "))
    suma = suma + numero
    
print("El valor de la suma es: ",suma)

