def cocktail_sort(vector):
    permutation,dirección,actual = True,1,0
    comienzo,fin = 0,len(vector)-2
    while permutation == True:
        permutation = False
        while (actual<fin and dirección==1) or \
        (actual>comienzo and dirección==-1) :
            # Prueba si intercambio
            if vector[actual] > vector[actual + 1]:
                permutation = True
                # Intercambiamos los dos elementos
                vector[actual], vector[actual + 1] = \
                vector[actual + 1],vector[actual]
            actual = actual + dirección
        # Cambiar la dirección de desplazamiento
        if dirección==1:
            fin = fin - 1
        else:
            comienzo = comienzo + 1
        dirección = -dirección
    print(vector)

cocktail_sort([10,2,1,80,9,60])