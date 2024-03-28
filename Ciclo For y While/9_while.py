''' UTILIZANDO EL CICLO WHILE, GENERA LA SIGUIENTE SALIDA
PARA "N" LINEAS:
*
**
***
****
*****
'''

filas = int(input("¿Cuantas filas quieres mostrar? "))
i=1
p="* "
p1="* "
j=1
while i <= filas: #Cilco que controla las filas 
    #p1="*"
    print("Estas en la fila ", i)
    while j <= i: #Cilclo que permite imprimir el numero de * que corresponde
        print(p)
        p= p+p1
        j= j+1
    i=i+1
