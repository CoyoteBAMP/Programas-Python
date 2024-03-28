#Imprimir primeros 5 numero utilizando recursividad

def imprimir(x):
        print(x)
        imprimir(x-1)

def imprimir2(x):
    if x>0:
        print(x)
        imprimir2(x-1)

def imprimir3(x):
    if x>0:
        imprimir2(x-1)
        print(x)
        

#imprimir(2)
imprimir2(5)
print ("\nSegunda ejecución")
imprimir3(4)


