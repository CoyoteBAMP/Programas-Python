lista=["Diana","Pedro","Paco","Luis","Pedro","Pedro"]

n =(input("¿Qué nombre deseas revisar? "))
veces = 0
for indice in range(len(lista)):
    listas=lista[indice]
    if listas == n:
        veces= veces + 1 

print("El numero se repite ",veces," veces")