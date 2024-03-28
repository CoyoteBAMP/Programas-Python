#Programa que permite leer desde teclado "n" numero y hallar su suma

k = 1
n = int(input("¿Cuantos numero deseas ingresar? "))
suma = 0

while (k <= n):
    print("Ingresa el numero ", k,": ")
    numero = int (input())
    suma = suma + numero
    k= k+1

print("La suma de los numeros ingresados es igual a: ",suma)