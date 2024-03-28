

lista1= [1,2,3,4,5,7,9]
lista2= [2,4,6,8]
c1= set(lista1)
c2= set(lista2)

print (c1)
print (c2)
input()

union=c1|c2
diferenciaC1menosC2= c1-c2
diferenciaC2menosC1= c2-c1
interseccion= c1 & c2
print("Elementos que aparecen en las dos listas (Unión).",union)
print("Elemenos que aparecen en la primer lista pero no en la segunda (Diferencia)",diferenciaC1menosC2)
print("Elemenos que aparecen en la segunda lista pero no en la primera (Diferencia)",diferenciaC2menosC1)
print("Elementos que aparecen en ambas listas (interseccion)",interseccion)
