#Utilizando el ciclo for, generar un programa python que 
#permite leer "n" numeros en p.flotante e indique cual es 
#el numero más grande que se haya introducido

#Ejemplo 3, 8, 23, 2, 4 

n=int(input("¿cuantos numeros deseas ingresar? "))
mayor= 0
for indice in range(n):
    numero = float(input("Introduce un numero: "))
    if numero > mayor:
        mayor = numero
    
print("El numero mayor es: ",mayor)

