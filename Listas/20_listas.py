
lista=[]
n = int(input("¿Cuantos numeros deseas ingresar? "))
for indice in range(n):
    numero = float(input("Introduce un numero: "))
    lista.extend([numero])

suma = 0
for i in range (len(lista)):
    numero=lista[i]
    suma = suma + numero
promedio = suma / n  
maximo=max(lista)
minimo=min(lista)
print("La suma es: ",suma)
print("El promedio es: ",promedio)
print("El valor maximo es: ",maximo)
print("El valor minimo es: ",minimo)
