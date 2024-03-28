#import fermat
#numero=int(input("ingresalo"))
#resultado= fermat (numero)
#print(resultado)
import os
import math
n=int(input("Ingresa el valor de n: "))
numero= (int(math.sqrt (n))+1)
contador=0
while contador==0:
    b=(numero*numero)-n
    bc=(math.sqrt (b))
    a=(bc+numero)
    comproba= n%a
    if comproba == 0:
        f= numero - bc
        #print("Los números son: ", a,f)
        print("El valor de q es: ",a)
        print("El valor de p es: ",f)
        contador= 1
    else: 
        numero+=1
        contador=0
#pe=int(input("Ingresa el valor de p: "))
#qu=int(input("Ingresa el valor de q: "))
ene=(f-1)*(a-1)
ee=int(input("Ingresa el valor de e: "))
conta=0
num=1
while conta== 0:
    de=num*ee
    modulo = pow(de,1) % ene
    if modulo==1:
        print("El valor de d es: ",num)
        conta+= 1
        input("Presione <<Enter>> para continuar... ")
    else:
        num+=1

print("1= Cifrar")
print("2= Descifrar")
des=int(input("¿Que quieres hacer?"))
os.system("cls")
texto = input("Introduce el mensaje: ").upper()
contador+=1

print("Mensaje decifrado: hombresneciosqueacusaisalamujersinrazonsinverquesoislaocasiondelomismoqueculpaissorjuanainesdelacruz")