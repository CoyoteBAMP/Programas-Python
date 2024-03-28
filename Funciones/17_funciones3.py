#Programa de operaciones aritmeticas basaicas utilizando funciones
import os

def sumar(n1,n2):
    suma = n1 + n2
    print("La suma es igual a = ",suma)

def restar(n1,n2):
    resta = n1 - n2
    print("La resta es igual a = ",resta)



os.system("cls")
num1=int(input("Ingresa el PRIMER valor: "))
num2=int(input("Ingresa el SEGUNDO valor: "))

sumar(num1,num2)
restar(num1,num2)