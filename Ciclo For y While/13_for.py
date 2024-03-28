n = int(input("¿Cuantos numeros deseas ingresar? "))
suma = 0
mayor = 0
for indice in range(n):
    numero = float(input("Introduce un numero: "))
    suma = suma + numero
    if numero > mayor:
        mayor = numero
promedio = suma / n  
print("\nEl numero mayor es: ",mayor)
print("El valor de la suma es: ",suma)
print("El valor del promedioes: ",promedio)